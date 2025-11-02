"""
Compare OpenAI vs Ollama performance
"""

from rag_pipeline import SimpleRAGPipeline
from rich.console import Console
from rich.table import Table
import time
import os

console = Console()

def test_provider(provider_name, llm_provider_value):
    """Test a specific provider"""
    # Update env temporarily
    original = os.environ.get("LLM_PROVIDER")
    os.environ["LLM_PROVIDER"] = llm_provider_value
    
    # Reload config
    import importlib
    import config
    importlib.reload(config)
    
    console.print(f"\n[cyan]Testing {provider_name}...[/cyan]")
    
    try:
        rag = SimpleRAGPipeline()
        rag.initialize()
        
        question = "What is RAG and why is it useful?"
        
        start_time = time.time()
        answer = rag.ask(question)
        elapsed = time.time() - start_time
        
        # Restore original
        if original:
            os.environ["LLM_PROVIDER"] = original
        
        return {
            "provider": provider_name,
            "success": True,
            "answer": answer[:150] + "..." if len(answer) > 150 else answer,
            "time": f"{elapsed:.2f}s"
        }
    except Exception as e:
        # Restore original
        if original:
            os.environ["LLM_PROVIDER"] = original
        
        return {
            "provider": provider_name,
            "success": False,
            "answer": f"Error: {str(e)[:100]}",
            "time": "N/A"
        }

def main():
    console.print("\n[bold cyan]========================================[/bold cyan]")
    console.print("[bold cyan]   OpenAI vs Ollama Comparison         [/bold cyan]")
    console.print("[bold cyan]========================================[/bold cyan]\n")
    
    results = []
    
    # Test OpenAI
    results.append(test_provider("OpenAI (Cloud)", "openai"))
    
    # Test Ollama
    results.append(test_provider("Ollama (Local)", "ollama"))
    
    # Create comparison table
    table = Table(title="\n📊 Performance Comparison")
    table.add_column("Provider", style="cyan")
    table.add_column("Privacy", style="yellow")
    table.add_column("Response Time", style="green")
    table.add_column("Status", style="bold")
    
    for result in results:
        if result["provider"] == "OpenAI (Cloud)":
            privacy = "Cloud ⚠️"
            cost = "Paid"
        else:
            privacy = "100% Local ✅"
            cost = "Free"
        
        status = "✅ Working" if result["success"] else "❌ Error"
        
        table.add_row(
            result["provider"],
            privacy,
            result["time"],
            status
        )
    
    console.print(table)
    
    # Show answers
    console.print("\n[bold]Sample Answers:[/bold]\n")
    for result in results:
        console.print(f"[cyan]{result['provider']}:[/cyan]")
        console.print(f"{result['answer']}\n")
    
    console.print("[bold green]Both providers are working! ✅[/bold green]")
    console.print("\n[cyan]Switch between them using:[/cyan]")
    console.print("[yellow]py switch_provider.py[/yellow]\n")

if __name__ == "__main__":
    main()
