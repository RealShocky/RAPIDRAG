"""
Test setup script to verify all components are working
"""

from rich.console import Console
from rich.panel import Panel
import sys

console = Console()


def test_imports():
    """Test if all required packages are installed"""
    console.print("\n[cyan]Testing package imports...[/cyan]")
    
    required_packages = [
        ("haystack", "Haystack AI"),
        ("sentence_transformers", "Sentence Transformers"),
        ("dotenv", "Python-dotenv"),
        ("rich", "Rich"),
    ]
    
    all_good = True
    for package, name in required_packages:
        try:
            __import__(package)
            console.print(f"[green]✓[/green] {name}")
        except ImportError:
            console.print(f"[red]✗[/red] {name} - NOT INSTALLED")
            all_good = False
    
    return all_good


def test_config():
    """Test if configuration is valid"""
    console.print("\n[cyan]Testing configuration...[/cyan]")
    
    try:
        from config import Config
        
        # Check if .env exists
        from pathlib import Path
        env_exists = Path(".env").exists()
        
        if env_exists:
            console.print("[green]✓[/green] .env file found")
        else:
            console.print("[yellow]⚠[/yellow] .env file not found (run setup.py)")
        
        # Test configuration
        Config.validate()
        console.print("[green]✓[/green] Configuration valid")
        
        return True
        
    except Exception as e:
        console.print(f"[red]✗[/red] Configuration error: {e}")
        return False


def test_file_structure():
    """Test if required files exist"""
    console.print("\n[cyan]Testing file structure...[/cyan]")
    
    from pathlib import Path
    
    required_files = [
        "requirements.txt",
        "README.md",
        "config.py",
        "ingest_documents.py",
        "rag_pipeline.py",
        "chatbot.py",
        "setup.py",
        ".env.example",
        ".gitignore"
    ]
    
    all_good = True
    for filename in required_files:
        if Path(filename).exists():
            console.print(f"[green]✓[/green] {filename}")
        else:
            console.print(f"[red]✗[/red] {filename} - MISSING")
            all_good = False
    
    return all_good


def test_directories():
    """Test if required directories exist"""
    console.print("\n[cyan]Testing directories...[/cyan]")
    
    from pathlib import Path
    
    required_dirs = ["documents", "data"]
    
    all_good = True
    for dirname in required_dirs:
        path = Path(dirname)
        if path.exists():
            console.print(f"[green]✓[/green] {dirname}/ directory exists")
        else:
            console.print(f"[yellow]⚠[/yellow] {dirname}/ directory missing (will be created)")
            path.mkdir(parents=True, exist_ok=True)
            console.print(f"[green]✓[/green] Created {dirname}/ directory")
    
    return all_good


def main():
    """Run all tests"""
    console.print("\n[bold cyan]========================================[/bold cyan]")
    console.print("[bold cyan]   RAG Chatbot - Setup Test            [/bold cyan]")
    console.print("[bold cyan]========================================[/bold cyan]")
    
    results = []
    
    # Run tests
    results.append(("Package Imports", test_imports()))
    results.append(("File Structure", test_file_structure()))
    results.append(("Directories", test_directories()))
    results.append(("Configuration", test_config()))
    
    # Summary
    console.print("\n" + "=" * 60)
    console.print("[bold]Test Summary:[/bold]")
    console.print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "[green]PASS[/green]" if passed else "[red]FAIL[/red]"
        console.print(f"{test_name}: {status}")
        if not passed:
            all_passed = False
    
    console.print("=" * 60)
    
    # Final verdict
    if all_passed:
        console.print("\n[bold green]✅ All tests passed! Your system is ready.[/bold green]\n")
        console.print("[cyan]Next steps:[/cyan]")
        console.print("1. If you haven't configured .env, run: [yellow]python setup.py[/yellow]")
        console.print("2. Add documents: [yellow]python ingest_documents.py --samples[/yellow]")
        console.print("3. Start chatting: [yellow]python chatbot.py[/yellow]\n")
    else:
        console.print("\n[bold red]❌ Some tests failed. Please fix the issues above.[/bold red]\n")
        console.print("Common fixes:")
        console.print("- Install packages: [yellow]pip install -r requirements.txt[/yellow]")
        console.print("- Run setup: [yellow]python setup.py[/yellow]\n")


if __name__ == "__main__":
    main()
