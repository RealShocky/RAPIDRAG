"""
Quick setup script for RAG Chatbot
Helps users get started quickly
"""

import os
import shutil
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm

console = Console()


def create_env_file():
    """Create .env file from template"""
    env_path = Path(".env")
    env_example_path = Path(".env.example")
    
    if env_path.exists():
        console.print("[yellow]⚠️  .env file already exists[/yellow]")
        overwrite = Confirm.ask("Do you want to overwrite it?", default=False)
        if not overwrite:
            return
    
    console.print("\n[bold cyan]RAG Chatbot Setup[/bold cyan]\n")
    console.print("Let's configure your chatbot. You can change these settings later in .env\n")
    
    # Choose LLM provider
    console.print("[cyan]Choose your LLM provider:[/cyan]")
    console.print("  1. OpenAI (requires API key, cloud-based)")
    console.print("  2. Ollama (free, runs locally, best for privacy)")
    console.print("  3. HuggingFace (free, runs locally)\n")
    
    choice = Prompt.ask("Enter choice", choices=["1", "2", "3"], default="2")
    
    if choice == "1":
        provider = "openai"
        console.print("\n[yellow]OpenAI selected - You'll need an API key[/yellow]")
        api_key = Prompt.ask("Enter your OpenAI API key (or leave blank to set later)", default="")
        model = Prompt.ask("OpenAI model", default="gpt-4o-mini")
        
        config = f"""# OpenAI Configuration
OPENAI_API_KEY={api_key}
OPENAI_MODEL={model}

# Model Selection
LLM_PROVIDER=openai

# Embedding model (runs locally)
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Retrieval settings
TOP_K_RETRIEVAL=3

# Document store path
DOCUMENT_STORE_PATH=./data/document_store.json
"""
    
    elif choice == "2":
        provider = "ollama"
        console.print("\n[green]Ollama selected - Privacy-focused local LLM[/green]")
        console.print("[dim]Make sure Ollama is installed: https://ollama.ai[/dim]")
        
        model = Prompt.ask("Ollama model", default="llama3.2")
        base_url = Prompt.ask("Ollama URL", default="http://localhost:11434")
        
        config = f"""# Ollama Configuration
OLLAMA_MODEL={model}
OLLAMA_BASE_URL={base_url}

# Model Selection
LLM_PROVIDER=ollama

# Embedding model (runs locally)
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Retrieval settings
TOP_K_RETRIEVAL=3

# Document store path
DOCUMENT_STORE_PATH=./data/document_store.json
"""
    
    else:  # HuggingFace
        provider = "huggingface"
        console.print("\n[green]HuggingFace selected - Open source local LLM[/green]")
        
        model = Prompt.ask("HuggingFace model", default="HuggingFaceH4/zephyr-7b-beta")
        
        config = f"""# HuggingFace Configuration
HUGGINGFACE_MODEL={model}

# Model Selection
LLM_PROVIDER=huggingface

# Embedding model (runs locally)
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Retrieval settings
TOP_K_RETRIEVAL=3

# Document store path
DOCUMENT_STORE_PATH=./data/document_store.json
"""
    
    # Write .env file
    with open(env_path, 'w') as f:
        f.write(config)
    
    console.print(f"\n[green]✓ Created .env file with {provider} configuration[/green]")


def create_directories():
    """Create required directories"""
    dirs = ["documents", "data"]
    
    for dir_name in dirs:
        path = Path(dir_name)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            console.print(f"[green]✓ Created {dir_name}/ directory[/green]")


def display_next_steps():
    """Display next steps for the user"""
    console.print("\n[bold green]✅ Setup complete![/bold green]\n")
    console.print("[cyan]Next steps:[/cyan]\n")
    console.print("1. [yellow]Add documents to knowledge base:[/yellow]")
    console.print("   [cyan]python ingest_documents.py --samples[/cyan]")
    console.print("   [dim](or add your own files to ./documents/ and run without --samples)[/dim]\n")
    console.print("2. [yellow]Start chatting:[/yellow]")
    console.print("   [cyan]python chatbot.py[/cyan]\n")
    console.print("3. [yellow]Optional - Install local LLM (if using Ollama):[/yellow]")
    console.print("   [cyan]ollama pull llama3.2[/cyan]\n")


def main():
    console.print("\n[bold cyan]========================================[/bold cyan]")
    console.print("[bold cyan]   RAG Chatbot - Quick Setup           [/bold cyan]")
    console.print("[bold cyan]========================================[/bold cyan]\n")
    
    # Create .env file
    create_env_file()
    
    # Create directories
    console.print()
    create_directories()
    
    # Display next steps
    display_next_steps()


if __name__ == "__main__":
    main()
