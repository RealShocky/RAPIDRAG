# RAG Chatbot - Project Overview

## 📋 Project Summary

A complete, production-ready **Retrieval-Augmented Generation (RAG) chatbot** built with Haystack framework. Features privacy-first architecture with support for both cloud-based (OpenAI) and local LLM options (Ollama, HuggingFace).

**Built with:** Python, Haystack 2.x, Sentence Transformers  
**Status:** ✅ Complete and ready to use

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG Chatbot System                        │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Documents   │───▶│  Ingestion   │───▶│  Document    │
│  (.txt, .md) │    │  Pipeline    │    │    Store     │
└──────────────┘    └──────────────┘    └──────────────┘
                           │                     │
                           │                     │
                    [Embeddings]          [Stored with
                    Generated              embeddings]
                    Locally                     │
                                               │
                                               ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│     User     │───▶│  RAG Query   │◀───│  Retriever   │
│    Query     │    │   Pipeline   │    │  (Semantic)  │
└──────────────┘    └──────────────┘    └──────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  LLM Model   │
                    │  (Configur-  │
                    │   able)      │
                    └──────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Response   │
                    └──────────────┘
```

---

## 📁 Project Structure

```
RAG/
├── 📄 Core Application Files
│   ├── config.py                 # Configuration management
│   ├── ingest_documents.py       # Document ingestion pipeline
│   ├── rag_pipeline.py           # RAG query pipeline
│   └── chatbot.py                # Interactive CLI interface
│
├── 🛠️ Setup & Testing
│   ├── setup.py                  # Interactive setup wizard
│   ├── test_setup.py             # System verification tests
│   └── requirements.txt          # Python dependencies
│
├── 📚 Documentation
│   ├── README.md                 # Main documentation
│   ├── QUICKSTART.md             # 5-minute quick start
│   ├── PRIVACY.md                # Privacy & security guide
│   └── PROJECT_OVERVIEW.md       # This file
│
├── ⚙️ Configuration
│   ├── .env.example              # Configuration template
│   ├── .env                      # Your config (not in git)
│   └── .gitignore                # Git exclusions
│
└── 📂 Data Directories
    ├── documents/                # Your documents go here
    │   └── README.md             # Document guide
    └── data/                     # Generated data (auto-created)
        └── document_store.json   # Vector database
```

---

## 🔑 Key Features

### ✅ Privacy-First Design
- **Local embeddings**: All text embedding runs on your machine
- **Choice of LLMs**: Use cloud (OpenAI) or local (Ollama/HuggingFace)
- **No vendor lock-in**: Switch providers via configuration
- **Data control**: Your documents never leave your infrastructure (with local models)

### ✅ Easy to Use
- **Interactive setup**: Wizard guides configuration
- **Sample documents**: Test with built-in examples
- **Beautiful CLI**: Rich terminal interface with colors
- **Simple commands**: `help`, `history`, `info`, `exit`

### ✅ Production Ready
- **Error handling**: Graceful error management
- **Configuration validation**: Catches issues early
- **Modular design**: Easy to extend and customize
- **Type hints**: Well-documented code

### ✅ Flexible Architecture
- **Multiple LLM providers**: OpenAI, Ollama, HuggingFace
- **Pluggable components**: Swap document stores, retrievers, embedders
- **Environment-based config**: Easy deployment across environments
- **Format support**: Text, Markdown (easy to extend)

---

## 🚀 Quick Start (3 Steps)

```bash
# 1. Install
pip install -r requirements.txt
python setup.py

# 2. Add knowledge base
python ingest_documents.py --samples

# 3. Chat!
python chatbot.py
```

Full guide: [QUICKSTART.md](QUICKSTART.md)

---

## 🔧 Core Components

### 1. Configuration Management (`config.py`)
- Environment-based configuration
- Multi-provider support
- Validation and error checking
- Safe secret handling

### 2. Document Ingestion (`ingest_documents.py`)
- Loads documents from directory
- Generates embeddings locally
- Stores in document store
- Supports metadata

**Key Functions:**
- `load_documents_from_directory()` - Scan and load files
- `embed_and_store_documents()` - Create embeddings
- `save_document_store()` - Persist to disk

### 3. RAG Pipeline (`rag_pipeline.py`)
- Query processing
- Semantic retrieval
- Context-aware generation
- Multiple LLM support

**Pipeline Flow:**
1. User query → Text embedder
2. Embedding → Retriever (find relevant docs)
3. Retrieved docs → Prompt builder (create context)
4. Context + Query → LLM (generate answer)

### 4. Interactive Chatbot (`chatbot.py`)
- Beautiful CLI interface
- Conversation management
- Command system
- Real-time feedback

**Commands:**
- `help` - Show help
- `info` - System information  
- `history` - Conversation history
- `clear` - Clear history
- `exit` - Quit

---

## 🔒 Privacy & Security

### Data Flow - Local Models (Ollama/HuggingFace)
```
Your Documents ──▶ [Local Processing] ──▶ Document Store (Local)
                           │
User Query ────▶ [Local Embeddings] ──▶ Retrieval (Local)
                           │
Retrieved Context ──▶ [Local LLM] ──▶ Response
                           │
                    [NO EXTERNAL CALLS]
```

### Data Flow - OpenAI
```
Your Documents ──▶ [Local Processing] ──▶ Document Store (Local)
                           │
User Query ────▶ [Local Embeddings] ──▶ Retrieval (Local)
                           │
Retrieved Context ──▶ [OpenAI API] ──▶ Response
                         (Cloud)
```

**Important**: Embeddings ALWAYS run locally regardless of LLM choice.

Full privacy guide: [PRIVACY.md](PRIVACY.md)

---

## 🎯 Use Cases

### ✅ Perfect For:
- Internal knowledge bases
- Document Q&A systems
- Customer support bots
- Research assistants
- Technical documentation chat
- Training & onboarding

### ✅ Works With:
- Company policies & procedures
- Technical documentation
- FAQs and help articles
- Research papers
- Meeting notes
- Any text-based content

---

## 📊 Technical Specifications

### Dependencies
- **haystack-ai** ≥2.0.0 - Core RAG framework
- **sentence-transformers** ≥3.0.0 - Local embeddings
- **torch** ≥2.0.0 - ML backend
- **openai** ≥1.0.0 - OpenAI integration (optional)
- **python-dotenv** - Configuration
- **rich** - Beautiful CLI

### System Requirements
- **Python**: 3.8+
- **RAM**: 4GB minimum (8GB+ recommended)
- **Storage**: ~2GB for embedding models
- **GPU**: Optional (faster local models)

### Supported Formats
- Plain text (`.txt`)
- Markdown (`.md`)
- Easy to extend for PDF, DOCX, etc.

---

## 🛠️ Configuration Options

### LLM Providers
```bash
# OpenAI (Cloud)
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4o-mini

# Ollama (Local)
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2
OLLAMA_BASE_URL=http://localhost:11434

# HuggingFace (Local)
LLM_PROVIDER=huggingface
HUGGINGFACE_MODEL=HuggingFaceH4/zephyr-7b-beta
```

### Embedding & Retrieval
```bash
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
TOP_K_RETRIEVAL=3  # Number of documents to retrieve
```

---

## 🧪 Testing

Run system verification:
```bash
python test_setup.py
```

This checks:
- ✅ Package installation
- ✅ File structure
- ✅ Configuration validity
- ✅ Directory setup

---

## 📈 Extending the System

### Add New Document Formats
Edit `ingest_documents.py`:
```python
supported_extensions = ['.txt', '.md', '.pdf', '.docx']
```

### Change Document Store
Replace `InMemoryDocumentStore` with:
- **Elasticsearch** - Production scale
- **Qdrant** - Vector-optimized
- **Weaviate** - GraphQL interface
- **Pinecone** - Managed cloud

### Custom Prompt Templates
Edit prompt in `rag_pipeline.py`:
```python
template = [
    ChatMessage.from_user("Your custom prompt here...")
]
```

---

## 📞 Support & Resources

### Documentation
- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [PRIVACY.md](PRIVACY.md) - Privacy & security

### External Resources
- **Haystack Docs**: https://haystack.deepset.ai/
- **Haystack Discord**: https://discord.com/invite/xYvH6drSmA
- **Ollama**: https://ollama.ai/
- **Sentence Transformers**: https://www.sbert.net/

---

## ✅ Project Status

| Component | Status | Notes |
|-----------|--------|-------|
| Core Framework | ✅ Complete | Haystack 2.x based |
| Document Ingestion | ✅ Complete | TXT, MD support |
| RAG Pipeline | ✅ Complete | Multi-LLM support |
| Chatbot Interface | ✅ Complete | Rich CLI |
| Configuration | ✅ Complete | Environment-based |
| Documentation | ✅ Complete | Comprehensive guides |
| Testing | ✅ Complete | Setup verification |
| Privacy Features | ✅ Complete | Local + Cloud options |

---

## 🎉 Summary

You now have a **complete, production-ready RAG chatbot** with:

✅ Full knowledge base functionality  
✅ Privacy-focused architecture  
✅ Multiple LLM options (cloud + local)  
✅ Beautiful interactive interface  
✅ Comprehensive documentation  
✅ Easy setup and deployment  

**Ready to use immediately!**

Start chatting:
```bash
python setup.py          # One-time setup
python ingest_documents.py --samples  # Load knowledge
python chatbot.py        # Start chatting!
```

---

**Built with ❤️ using Haystack framework**  
For questions about data privacy, see [PRIVACY.md](PRIVACY.md)
