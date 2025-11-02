"""
RAG Pipeline - Retrieval-Augmented Generation
Handles query processing, retrieval, and response generation
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

from haystack import Pipeline, Document
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage
from haystack.components.generators.chat import OpenAIChatGenerator

from config import Config


class RAGPipeline:
    """RAG Pipeline for question answering"""
    
    def __init__(self):
        self.config = Config
        self.document_store = InMemoryDocumentStore()
        self.pipeline = None
        self.llm_generator = None
        
    def load_document_store(self):
        """Load document store from disk"""
        if not self.config.DOCUMENT_STORE_PATH.exists():
            raise FileNotFoundError(
                f"Document store not found at {self.config.DOCUMENT_STORE_PATH}\n"
                "Please run 'python ingest_documents.py' first to create the knowledge base."
            )
        
        # Load documents from JSON
        with open(self.config.DOCUMENT_STORE_PATH, 'r', encoding='utf-8') as f:
            docs_data = json.load(f)
        
        # Recreate documents with embeddings
        documents = []
        for doc_dict in docs_data:
            doc = Document(
                id=doc_dict["id"],
                content=doc_dict["content"],
                meta=doc_dict.get("meta", {}),
                embedding=doc_dict.get("embedding")
            )
            documents.append(doc)
        
        # Write to document store
        self.document_store.write_documents(documents)
        
        return len(documents)
    
    def initialize_llm_generator(self):
        """Initialize LLM generator based on configuration"""
        llm_config = self.config.get_llm_config()
        
        if llm_config["provider"] == "openai":
            # OpenAI Generator
            os.environ["OPENAI_API_KEY"] = llm_config["api_key"]
            self.llm_generator = OpenAIChatGenerator(
                model=llm_config["model"]
            )
            
        elif llm_config["provider"] == "ollama":
            # Ollama Generator (requires ollama-haystack integration)
            try:
                from haystack_integrations.components.generators.ollama import OllamaChatGenerator
                self.llm_generator = OllamaChatGenerator(
                    model=llm_config["model"],
                    url=llm_config["base_url"]
                )
            except ImportError:
                raise ImportError(
                    "Ollama integration not installed. Install with:\n"
                    "pip install ollama-haystack"
                )
                
        elif llm_config["provider"] == "huggingface":
            # HuggingFace Generator
            try:
                from haystack.components.generators.chat import HuggingFaceTGIChatGenerator
                self.llm_generator = HuggingFaceTGIChatGenerator(
                    model=llm_config["model"]
                )
            except ImportError:
                raise ImportError(
                    "HuggingFace integration issue. Please check your installation."
                )
        else:
            raise ValueError(f"Unknown LLM provider: {llm_config['provider']}")
    
    def build_pipeline(self):
        """Build the RAG pipeline"""
        
        # Initialize components
        
        # 1. Text Embedder - converts user query to embedding
        text_embedder = SentenceTransformersTextEmbedder(
            model=self.config.EMBEDDING_MODEL
        )
        
        # 2. Retriever - finds relevant documents
        retriever = InMemoryEmbeddingRetriever(
            document_store=self.document_store,
            top_k=self.config.TOP_K_RETRIEVAL
        )
        
        # 3. Prompt Builder - creates the prompt with context
        template = [
            ChatMessage.from_user(
                """You are a helpful assistant that answers questions based on the provided context.
Use the context below to answer the question. If you cannot answer based on the context, say so.

Context:
{% for document in documents %}
{{ document.content }}
---
{% endfor %}

Question: {{question}}

Answer:"""
            )
        ]
        prompt_builder = ChatPromptBuilder(template=template)
        
        # 4. LLM Generator - generates the answer
        self.initialize_llm_generator()
        
        # Build pipeline
        pipeline = Pipeline()
        
        # Add components
        pipeline.add_component("text_embedder", text_embedder)
        pipeline.add_component("retriever", retriever)
        pipeline.add_component("prompt_builder", prompt_builder)
        pipeline.add_component("llm", self.llm_generator)
        
        # Connect components
        pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
        pipeline.connect("retriever.documents", "prompt_builder.documents")
        pipeline.connect("prompt_builder.prompt", "llm.messages")
        
        self.pipeline = pipeline
    
    def query(self, question: str) -> Dict[str, Any]:
        """
        Query the RAG pipeline
        
        Args:
            question: User question
            
        Returns:
            Dictionary with answer and metadata
        """
        if not self.pipeline:
            raise RuntimeError("Pipeline not built. Call build_pipeline() first.")
        
        # Run pipeline
        result = self.pipeline.run({
            "text_embedder": {"text": question},
            "prompt_builder": {"question": question}
        })
        
        # Extract answer
        answer = result["llm"]["replies"][0].text
        
        # Extract retrieved documents
        retrieved_docs = result.get("retriever", {}).get("documents", [])
        
        return {
            "question": question,
            "answer": answer,
            "retrieved_documents": retrieved_docs,
            "num_documents": len(retrieved_docs)
        }
    
    def initialize(self):
        """Initialize the complete RAG system"""
        # Load document store
        num_docs = self.load_document_store()
        
        # Build pipeline
        self.build_pipeline()
        
        return num_docs


class SimpleRAGPipeline:
    """
    Simplified RAG Pipeline for direct usage
    This is a convenience wrapper around RAGPipeline
    """
    
    def __init__(self):
        self.rag = RAGPipeline()
        self.initialized = False
    
    def initialize(self):
        """Initialize the RAG system"""
        if not self.initialized:
            num_docs = self.rag.initialize()
            self.initialized = True
            return num_docs
        return 0
    
    def ask(self, question: str) -> str:
        """
        Ask a question and get an answer
        
        Args:
            question: User question
            
        Returns:
            Answer string
        """
        if not self.initialized:
            self.initialize()
        
        result = self.rag.query(question)
        return result["answer"]
    
    def ask_detailed(self, question: str) -> Dict[str, Any]:
        """
        Ask a question and get detailed results
        
        Args:
            question: User question
            
        Returns:
            Dictionary with answer and metadata
        """
        if not self.initialized:
            self.initialize()
        
        return self.rag.query(question)


# Example usage
if __name__ == "__main__":
    from rich.console import Console
    
    console = Console()
    
    console.print("\n[bold cyan]Testing RAG Pipeline[/bold cyan]\n")
    
    try:
        # Initialize pipeline
        console.print("[cyan]Initializing RAG system...[/cyan]")
        rag = SimpleRAGPipeline()
        num_docs = rag.initialize()
        console.print(f"[green]✓ Loaded {num_docs} documents[/green]\n")
        
        # Test questions
        test_questions = [
            "What is RAG?",
            "How does Haystack work?",
            "What are embeddings?"
        ]
        
        for question in test_questions:
            console.print(f"[yellow]Q: {question}[/yellow]")
            
            result = rag.ask_detailed(question)
            
            console.print(f"[green]A: {result['answer']}[/green]")
            console.print(f"[dim]Retrieved {result['num_documents']} documents[/dim]\n")
            
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
        console.print("\n[yellow]Run this first:[/yellow]")
        console.print("[cyan]python ingest_documents.py --samples[/cyan]\n")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
