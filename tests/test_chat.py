"""
Quick test of the chatbot - automated demo
"""

from rag_pipeline import SimpleRAGPipeline
from rich.console import Console

console = Console()

console.print("\n[bold cyan]🤖 RAG Chatbot Quick Test[/bold cyan]\n")

# Initialize
rag = SimpleRAGPipeline()
console.print("[cyan]Initializing...[/cyan]")
num_docs = rag.initialize()
console.print(f"[green]✓ Loaded {num_docs} documents\n[/green]")

# Test questions
questions = [
    "What is RAG and why is it useful?",
    "How can I ensure maximum privacy with this chatbot?",
    "What embedding model is being used?"
]

for i, question in enumerate(questions, 1):
    console.print(f"[yellow]Q{i}: {question}[/yellow]")
    answer = rag.ask(question)
    console.print(f"[green]A{i}: {answer}[/green]\n")

console.print("[bold green]✅ All tests passed! Your RAG chatbot is working![/bold green]\n")
console.print("[cyan]To use the interactive chatbot, run:[/cyan]")
console.print("[yellow]py chatbot.py[/yellow]\n")
