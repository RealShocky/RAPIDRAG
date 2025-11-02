"""
Quick script to switch between OpenAI and Ollama
"""

import sys
from pathlib import Path
from rich.console import Console
from rich.prompt import Confirm

console = Console()

def read_env():
    """Read current .env file"""
    env_path = Path(".env")
    if not env_path.exists():
        console.print("[red]Error: .env file not found[/red]")
        sys.exit(1)
    
    with open(env_path, 'r') as f:
        return f.read()

def switch_to_ollama():
    """Switch to Ollama provider"""
    env_content = read_env()
    
    # Update provider
    env_content = env_content.replace("LLM_PROVIDER=openai", "LLM_PROVIDER=ollama")
    
    with open(".env", 'w') as f:
        f.write(env_content)
    
    console.print("[green]✓ Switched to Ollama (local, private)[/green]")
    console.print("\n[cyan]Next steps:[/cyan]")
    console.print("1. Install Ollama from: https://ollama.ai/download")
    console.print("2. Run: [yellow]ollama pull llama3.2[/yellow]")
    console.print("3. Test: [yellow]py chatbot.py[/yellow]\n")

def switch_to_openai():
    """Switch to OpenAI provider"""
    env_content = read_env()
    
    # Update provider
    env_content = env_content.replace("LLM_PROVIDER=ollama", "LLM_PROVIDER=openai")
    
    with open(".env", 'w') as f:
        f.write(env_content)
    
    console.print("[green]✓ Switched to OpenAI (cloud, fast)[/green]")
    console.print("\n[cyan]Make sure your API key is set in .env[/cyan]")
    console.print("Test: [yellow]py chatbot.py[/yellow]\n")

def main():
    console.print("\n[bold cyan]LLM Provider Switcher[/bold cyan]\n")
    
    env_content = read_env()
    
    # Detect current provider
    if "LLM_PROVIDER=openai" in env_content:
        current = "OpenAI"
        switch_to = "Ollama (local, private)"
    else:
        current = "Ollama"
        switch_to = "OpenAI (cloud, fast)"
    
    console.print(f"[yellow]Current provider: {current}[/yellow]")
    console.print(f"[cyan]Available: {switch_to}[/cyan]\n")
    
    if Confirm.ask(f"Switch to {switch_to}?"):
        if current == "OpenAI":
            switch_to_ollama()
        else:
            switch_to_openai()
    else:
        console.print("[yellow]No changes made[/yellow]\n")

if __name__ == "__main__":
    main()
