"""
Interactive RAG Chatbot
A command-line interface for chatting with your knowledge base
"""

import sys
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.table import Table

from config import Config
from rag_pipeline import SimpleRAGPipeline


class InteractiveChatbot:
    """Interactive chatbot with CLI interface"""
    
    def __init__(self):
        self.console = Console()
        self.rag = SimpleRAGPipeline()
        self.conversation_history = []
        self.initialized = False
        
    def display_header(self):
        """Display chatbot header"""
        self.console.print("\n")
        header = """
================================================================
                                                              
         🤖  RAG Chatbot - Knowledge Base Assistant          
                                                              
              Ask questions about your documents              
                                                              
================================================================
        """
        self.console.print(header, style="bold cyan")
    
    def display_config_info(self):
        """Display current configuration"""
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="green")
        
        llm_config = Config.get_llm_config()
        
        table.add_row("LLM Provider", llm_config["provider"].upper())
        if llm_config["provider"] == "openai":
            table.add_row("Model", llm_config["model"])
        elif llm_config["provider"] == "ollama":
            table.add_row("Model", llm_config["model"])
            table.add_row("URL", llm_config["base_url"])
        
        table.add_row("Embedding Model", Config.EMBEDDING_MODEL)
        table.add_row("Retrieval Docs", str(Config.TOP_K_RETRIEVAL))
        
        self.console.print(table)
        self.console.print()
    
    def initialize_system(self):
        """Initialize the RAG system"""
        self.console.print("[cyan]🔧 Initializing RAG system...[/cyan]")
        
        try:
            with self.console.status("[bold cyan]Loading knowledge base..."):
                num_docs = self.rag.initialize()
            
            self.initialized = True
            self.console.print(f"[green]✓ Knowledge base loaded with {num_docs} documents[/green]")
            self.console.print()
            return True
            
        except FileNotFoundError as e:
            self.console.print(f"\n[red]❌ Error: {e}[/red]\n")
            self.console.print("[yellow]Please run the document ingestion first:[/yellow]")
            self.console.print("[cyan]  python ingest_documents.py --samples[/cyan]")
            self.console.print("[dim]  (or add your own documents to ./documents/)[/dim]\n")
            return False
            
        except Exception as e:
            self.console.print(f"\n[red]❌ Initialization error: {e}[/red]\n")
            return False
    
    def display_help(self):
        """Display help information"""
        help_text = """
**Available Commands:**

• Type your question and press Enter to ask
• `help` - Show this help message
• `info` - Display system information
• `history` - Show conversation history
• `clear` - Clear conversation history
• `exit` or `quit` - Exit the chatbot

**Tips:**

• Ask specific questions about your documents
• The system will retrieve relevant context automatically
• More detailed questions usually get better answers
        """
        self.console.print(Panel(Markdown(help_text), title="Help", border_style="cyan"))
    
    def display_info(self):
        """Display system information"""
        info_table = Table(title="System Information", box=None)
        info_table.add_column("Component", style="cyan")
        info_table.add_column("Status", style="green")
        
        info_table.add_row("RAG System", "✓ Initialized" if self.initialized else "✗ Not initialized")
        info_table.add_row("Conversations", str(len(self.conversation_history)))
        info_table.add_row("LLM Provider", Config.LLM_PROVIDER.upper())
        info_table.add_row("Privacy Mode", "✓ Local" if Config.LLM_PROVIDER != "openai" else "Cloud (OpenAI)")
        
        self.console.print()
        self.console.print(info_table)
        self.console.print()
    
    def display_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            self.console.print("[yellow]No conversation history yet.[/yellow]\n")
            return
        
        self.console.print("\n[bold cyan]Conversation History:[/bold cyan]\n")
        
        for i, conv in enumerate(self.conversation_history, 1):
            self.console.print(f"[yellow]#{i} Q:[/yellow] {conv['question']}")
            self.console.print(f"[green]   A:[/green] {conv['answer'][:200]}...")
            self.console.print()
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        self.console.print("[green]✓ Conversation history cleared[/green]\n")
    
    def ask_question(self, question: str):
        """Process a user question"""
        # Show thinking indicator
        with self.console.status("[bold cyan]🤔 Thinking..."):
            try:
                result = self.rag.ask_detailed(question)
            except Exception as e:
                self.console.print(f"\n[red]❌ Error: {e}[/red]\n")
                return
        
        # Display answer
        answer = result["answer"]
        self.console.print()
        self.console.print(Panel(
            answer,
            title="[bold green]🤖 Answer[/bold green]",
            border_style="green",
            padding=(1, 2)
        ))
        
        # Display metadata
        self.console.print(f"[dim]📚 Retrieved {result['num_documents']} relevant document(s)[/dim]")
        self.console.print()
        
        # Save to history
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "answer": answer,
            "num_docs": result["num_documents"]
        })
    
    def run(self):
        """Run the interactive chatbot"""
        # Display header
        self.display_header()
        
        # Display configuration
        self.display_config_info()
        
        # Initialize system
        if not self.initialize_system():
            return
        
        # Display welcome message
        self.console.print("[cyan]💬 Ready to chat! Type 'help' for commands or 'exit' to quit.[/cyan]\n")
        
        # Main chat loop
        while True:
            try:
                # Get user input
                question = Prompt.ask("\n[bold yellow]You[/bold yellow]")
                
                # Handle empty input
                if not question.strip():
                    continue
                
                # Handle commands
                command = question.strip().lower()
                
                if command in ["exit", "quit"]:
                    self.console.print("\n[cyan]👋 Goodbye! Thanks for chatting.[/cyan]\n")
                    break
                
                elif command == "help":
                    self.display_help()
                    continue
                
                elif command == "info":
                    self.display_info()
                    continue
                
                elif command == "history":
                    self.display_history()
                    continue
                
                elif command == "clear":
                    self.clear_history()
                    continue
                
                # Process as question
                self.ask_question(question)
                
            except KeyboardInterrupt:
                self.console.print("\n\n[cyan]👋 Goodbye! Thanks for chatting.[/cyan]\n")
                break
            
            except Exception as e:
                self.console.print(f"\n[red]❌ Unexpected error: {e}[/red]\n")
                self.console.print("[yellow]Type 'exit' to quit or continue chatting.[/yellow]\n")


def main():
    """Main entry point"""
    chatbot = InteractiveChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
