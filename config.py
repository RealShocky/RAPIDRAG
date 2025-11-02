"""
Configuration management for RAG Chatbot
Loads settings from .env file and provides configuration objects
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Main configuration class"""
    
    # LLM Provider Settings
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    
    # Ollama Configuration
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    
    # HuggingFace Configuration
    HUGGINGFACE_MODEL = os.getenv("HUGGINGFACE_MODEL", "HuggingFaceH4/zephyr-7b-beta")
    
    # Embedding Configuration (runs locally)
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    
    # Retrieval Settings
    TOP_K_RETRIEVAL = int(os.getenv("TOP_K_RETRIEVAL", "3"))
    
    # Paths
    PROJECT_ROOT = Path(__file__).parent
    DOCUMENTS_DIR = PROJECT_ROOT / "documents"
    DATA_DIR = PROJECT_ROOT / "data"
    DOCUMENT_STORE_PATH = Path(os.getenv("DOCUMENT_STORE_PATH", str(DATA_DIR / "document_store.json")))
    
    @classmethod
    def validate(cls):
        """Validate configuration"""
        errors = []
        
        # Validate LLM provider
        valid_providers = ["openai", "ollama", "huggingface"]
        if cls.LLM_PROVIDER not in valid_providers:
            errors.append(f"LLM_PROVIDER must be one of {valid_providers}, got '{cls.LLM_PROVIDER}'")
        
        # Validate OpenAI configuration
        if cls.LLM_PROVIDER == "openai" and not cls.OPENAI_API_KEY:
            errors.append("OPENAI_API_KEY is required when using OpenAI provider")
        
        # Create directories
        cls.DOCUMENTS_DIR.mkdir(exist_ok=True)
        cls.DATA_DIR.mkdir(exist_ok=True)
        
        if errors:
            raise ValueError("\n".join(errors))
        
        return True
    
    @classmethod
    def get_llm_config(cls):
        """Get LLM configuration based on provider"""
        if cls.LLM_PROVIDER == "openai":
            return {
                "provider": "openai",
                "model": cls.OPENAI_MODEL,
                "api_key": cls.OPENAI_API_KEY
            }
        elif cls.LLM_PROVIDER == "ollama":
            return {
                "provider": "ollama",
                "model": cls.OLLAMA_MODEL,
                "base_url": cls.OLLAMA_BASE_URL
            }
        elif cls.LLM_PROVIDER == "huggingface":
            return {
                "provider": "huggingface",
                "model": cls.HUGGINGFACE_MODEL
            }
        else:
            raise ValueError(f"Unknown LLM provider: {cls.LLM_PROVIDER}")
    
    @classmethod
    def display_config(cls):
        """Display current configuration (safe - no secrets)"""
        print("=" * 60)
        print("RAG Chatbot Configuration")
        print("=" * 60)
        print(f"LLM Provider:     {cls.LLM_PROVIDER}")
        if cls.LLM_PROVIDER == "openai":
            print(f"OpenAI Model:     {cls.OPENAI_MODEL}")
            print(f"API Key Set:      {'Yes' if cls.OPENAI_API_KEY else 'No'}")
        elif cls.LLM_PROVIDER == "ollama":
            print(f"Ollama Model:     {cls.OLLAMA_MODEL}")
            print(f"Ollama URL:       {cls.OLLAMA_BASE_URL}")
        elif cls.LLM_PROVIDER == "huggingface":
            print(f"HF Model:         {cls.HUGGINGFACE_MODEL}")
        
        print(f"Embedding Model:  {cls.EMBEDDING_MODEL}")
        print(f"Top K Retrieval:  {cls.TOP_K_RETRIEVAL}")
        print(f"Documents Dir:    {cls.DOCUMENTS_DIR}")
        print(f"Data Dir:         {cls.DATA_DIR}")
        print("=" * 60)
        print()


# Validate configuration on import
try:
    Config.validate()
except ValueError as e:
    print(f"\n⚠️  Configuration Error:\n{e}\n")
    print("Please check your .env file and ensure all required settings are configured.")
    print("Copy .env.example to .env and fill in the values.\n")
