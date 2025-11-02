# RAG Chatbot with Haystack

A privacy-focused Retrieval-Augmented Generation (RAG) chatbot built with Haystack framework. Supports both cloud-based (OpenAI) and local LLM options (Ollama) for maximum data privacy.

## 🚀 Quick Start

### **Windows Users (Easiest!)**

**Just double-click:** `START.bat`

That's it! The menu system handles everything automatically.

### **Web Interface (Beautiful Dashboard!)**

**Launch RAPIDRAG web UI:**
```batch
start-webapp.bat              # Local access (you only)
start-webapp-network.bat      # Network access (team sharing)
start-webapp-external.bat     # External access (internet) ⚠️
```

Features stunning space-themed interface with animations, chat, document upload, and analytics!

**Share with team:** Use network mode to allow LAN access!

### **Manual Setup (All Platforms)**

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure (interactive wizard)
python setup.py

# 3. Add knowledge base
python ingest_documents.py --samples

# 4. Start chatting!
python chatbot.py
```

**See:** [`docs/OUT_OF_BOX_GUIDE.md`](docs/OUT_OF_BOX_GUIDE.md) for zero-config setup!

---

## 📁 Project Structure

```
RAG/
├── 📄 Core Application
│   ├── chatbot.py              # Interactive CLI chatbot
│   ├── ingest_documents.py     # Document ingestion pipeline
│   ├── rag_pipeline.py         # RAG query pipeline
│   ├── config.py               # Configuration management
│   └── setup.py                # Interactive setup wizard
│
├── 📚 Documentation
│   ├── docs/
│   │   ├── README.md           # Main documentation
│   │   ├── PROJECT_OVERVIEW.md # Technical architecture
│   │   ├── GET_STARTED.txt     # Quick reference
│   │   └── guides/
│   │       ├── QUICKSTART.md   # 5-minute guide
│   │       └── PRIVACY.md      # Privacy & security
│
├── 🧪 Tests
│   └── tests/
│       ├── test_setup.py       # System verification
│       ├── test_chat.py        # Quick Q&A test
│       └── compare_models.py   # OpenAI vs Ollama
│
├── 📂 Data & Documents
│   ├── documents/              # 👈 PUT YOUR FILES HERE
│   │   └── README.md           # Format guide
│   └── data/                   # Generated (auto-created)
│       └── document_store.json # Vector database
│
└── ⚙️ Configuration
    ├── .env                    # Your settings (not in git)
    ├── .env.example            # Configuration template
    ├── requirements.txt        # Python dependencies
    └── .gitignore              # Git exclusions
```

---

## 📚 Adding Your Knowledge Base

### Where to Put Files
**Place all documents in the `documents/` folder:**

```bash
documents/
├── your-file.txt
├── your-file.md
├── your-file.pdf      # PDF support
├── your-file.docx     # Word documents
├── your-file.html     # HTML pages
└── subfolder/
    └── more-docs.txt  # Supports nested folders
```

### Supported Formats

| Format | Extension | Support |
|--------|-----------|---------|
| Plain Text | `.txt` | ✅ Full |
| Markdown | `.md` | ✅ Full |
| PDF | `.pdf` | ✅ Full |
| Word | `.docx` | ✅ Full |
| HTML | `.html`, `.htm` | ✅ Full |
| JSON | `.json` | ✅ Full |

### Ingest Your Documents

```bash
# Ingest all files from documents/ folder
python ingest_documents.py

# Or test with samples first
python ingest_documents.py --samples
```

---

## 🔒 Privacy Options

### Maximum Privacy (Recommended)
**Use Ollama - 100% Local**
- All processing on your machine
- No external API calls
- No data leaves your infrastructure
- Free to use
- **Currently active!** ✅

### Cloud Option
**Use OpenAI API**
- Faster responses
- Most capable model
- Requires API key
- Data sent to OpenAI servers

**Switch anytime:**
```bash
python switch_provider.py
```

Or edit `.env` file: `LLM_PROVIDER=ollama` or `LLM_PROVIDER=openai`

---

## 🎯 Common Commands

### **Windows - Use Menu System (Recommended)**

```batch
# Launch menu system
rag-menu.bat

# Or quick launcher
START.bat
```

**Menu includes (16 options):**
- First-time setup (auto-install everything)
- Document ingestion
- Start chatbot (CLI)
- **Start web interface (3 modes: Local/Network/External)**
- System tests
- Provider switching
- Documentation viewer
- And more!

### **Manual Commands (All Platforms)**

```bash
# Start interactive chatbot
python chatbot.py

# Add documents to knowledge base
python ingest_documents.py

# Test system status
python tests/test_setup.py

# Quick Q&A test
python tests/test_chat.py

# Compare OpenAI vs Ollama
python tests/compare_models.py

# Switch between providers
python switch_provider.py

# Setup wizard
python setup.py
```

---

## 💬 Using the Chatbot

Start the chatbot:
```bash
python chatbot.py
```

Available commands:
- Type your question and press Enter
- `help` - Show available commands
- `info` - Display system information
- `history` - Show conversation history
- `clear` - Clear conversation history
- `exit` or `quit` - Exit chatbot

---

## 🏗️ Architecture

```
User Query → Text Embedder (local) → Retriever → Documents
                                                      ↓
              LLM (Ollama/OpenAI) ← Prompt Builder ← Context
                                                      ↓
                                                   Answer
```

**Components:**
- **Document Store**: InMemoryDocumentStore (stores documents + embeddings)
- **Embedder**: SentenceTransformers (all-MiniLM-L6-v2) - runs locally
- **Retriever**: Semantic search using embeddings
- **Generator**: Ollama (llama3.2) or OpenAI GPT (configurable)

---

## 📖 Documentation

- **Quick Start**: [`docs/GET_STARTED.txt`](docs/GET_STARTED.txt)
- **Full Guide**: [`docs/guides/QUICKSTART.md`](docs/guides/QUICKSTART.md)
- **Privacy**: [`docs/guides/PRIVACY.md`](docs/guides/PRIVACY.md)
- **Technical Details**: [`docs/PROJECT_OVERVIEW.md`](docs/PROJECT_OVERVIEW.md)

---

## 🔧 Configuration

Edit `.env` to customize:
- `LLM_PROVIDER` - Choose "openai" or "ollama"
- `EMBEDDING_MODEL` - Change embedding model
- `TOP_K_RETRIEVAL` - Number of documents to retrieve (default: 3)
- Model-specific settings (API keys, URLs, etc.)

---

## 🛡️ Security Best Practices

1. ✅ Never commit `.env` file (already in .gitignore)
2. ✅ For maximum privacy: Use Ollama (100% local)
3. ✅ API keys: Store in `.env`, never hardcode
4. ✅ Embeddings: Always run locally

---

## 🎓 Learn More

- [Haystack Documentation](https://haystack.deepset.ai/)
- [RAG Tutorial](https://haystack.deepset.ai/tutorials/27_first_rag_pipeline)
- [Ollama Models](https://ollama.ai/library)
- [Haystack Discord](https://discord.com/invite/xYvH6drSmA)

---

## 📊 System Status

✅ **All packages installed**  
✅ **Knowledge base ready** (4 sample documents)  
✅ **OpenAI integration** (cloud, fast)  
✅ **Ollama integration** (local, private, active)  
✅ **Multi-format support** (TXT, MD, PDF, DOCX, HTML, JSON)  
✅ **Complete documentation**

---

**Ready to build your knowledge base!** 🚀

Place your documents in `documents/` folder and run `python ingest_documents.py`
