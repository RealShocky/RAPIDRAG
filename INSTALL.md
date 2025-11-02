# Installation Guide

Complete installation instructions for all platforms.

---

## 🪟 Windows - Automatic Installation (Recommended)

### **Method 1: One-Click Setup**

1. **Double-click `START.bat`**
2. Press `Y` when prompted
3. Wait 3-5 minutes
4. Done!

**Everything is installed automatically:**
- ✅ All Python dependencies
- ✅ OpenAI integration
- ✅ Ollama integration (ready for local use)
- ✅ All document processors (PDF, DOCX, HTML, etc.)
- ✅ Sample documents loaded
- ✅ System configured

---

### **Method 2: Menu System**

1. **Double-click `rag-menu.bat`**
2. **Select Option 1:** "First-Time Setup"
3. Follow prompts
4. Done!

---

## 🐧 Linux / 🍎 macOS - Manual Installation

### **Step 1: Install Python Dependencies**

```bash
# Ensure Python 3.8+ is installed
python3 --version

# Install all dependencies
pip3 install -r requirements.txt
```

**What gets installed:**
- Core: `haystack-ai`, `sentence-transformers`, `torch`
- LLMs: `openai`, `ollama-haystack`
- Formats: `pypdf`, `python-docx`, `beautifulsoup4`, `lxml`
- Utils: `python-dotenv`, `rich`, `datasets`

---

### **Step 2: Run Configuration Wizard**

```bash
python3 setup.py
```

**This will:**
- Create `.env` configuration file
- Let you choose LLM provider (OpenAI or Ollama)
- Set up API keys (if using OpenAI)
- Configure paths and settings

---

### **Step 3: Load Sample Documents**

```bash
python3 ingest_documents.py --samples
```

**This adds:**
- 4 sample documents about RAG and AI
- Creates vector database with embeddings
- Ready for testing

---

### **Step 4: Verify Installation**

```bash
python3 tests/test_setup.py
```

**Checks:**
- ✅ All packages installed
- ✅ File structure correct
- ✅ Configuration valid
- ✅ System ready

---

## 📦 What Gets Installed

### Core Framework (~1.5 GB)

```
haystack-ai>=2.0.0              # RAG framework
sentence-transformers>=3.0.0    # Embeddings (local)
torch>=2.0.0                    # ML backend
```

### LLM Integrations (~50 MB)

```
openai>=1.0.0                   # OpenAI API (cloud)
ollama-haystack>=1.0.0          # Ollama (local) ✨ INCLUDED
```

### Document Processing (~20 MB)

```
pypdf>=3.0.0                    # PDF files
python-docx>=1.0.0              # Word documents
beautifulsoup4>=4.12.0          # HTML pages
lxml>=4.9.0                     # XML/HTML parsing
markdown>=3.4.0                 # Enhanced markdown
```

### Utilities (~10 MB)

```
python-dotenv>=1.0.0            # Configuration
rich>=13.0.0                    # Beautiful CLI
datasets>=2.6.1                 # Data handling
```

**Total:** ~2 GB (mostly PyTorch)

---

## 🤖 Installing Ollama (Optional - For Local LLM)

### Why Ollama?
- ✅ 100% private (no data leaves your machine)
- ✅ Free forever
- ✅ No API keys needed
- ✅ Works offline

### Installation

**Windows:**
1. Download: https://ollama.ai/download/windows
2. Run installer
3. Use menu: `rag-menu.bat` → Option 3
4. Or manually: `ollama pull llama3.2`

**macOS:**
```bash
# Install Ollama
brew install ollama

# Download model
ollama pull llama3.2
```

**Linux:**
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Download model
ollama pull llama3.2
```

**Model size:** ~2 GB (llama3.2)

---

## 🔑 OpenAI Setup (Optional - For Cloud LLM)

### Why OpenAI?
- ✅ Fastest responses
- ✅ Most capable models
- ✅ No local resources needed

### Setup

1. **Get API key:** https://platform.openai.com/api-keys
2. **Edit `.env` file:**
   ```bash
   OPENAI_API_KEY=sk-proj-your-key-here
   LLM_PROVIDER=openai
   ```
3. **Done!**

**Cost:** ~$0.01 per 1000 messages (gpt-4o-mini)

---

## ✅ Verification Steps

### 1. Test Package Installation

```bash
python tests/test_setup.py
```

**Expected output:**
```
✓ Haystack AI
✓ Sentence Transformers
✓ Python-dotenv
✓ Rich
✓ All tests passed!
```

---

### 2. Test Document Ingestion

```bash
python ingest_documents.py --samples
```

**Expected output:**
```
✓ Loaded 4 sample documents
✓ Embedder initialized
✓ Stored 4 document(s) with embeddings
✅ Document ingestion completed successfully!
```

---

### 3. Test RAG Pipeline

```bash
python tests/test_chat.py
```

**Expected output:**
```
Q1: What is RAG and why is it useful?
A1: Retrieval-Augmented Generation (RAG) is a technique...

✅ All tests passed!
```

---

### 4. Test Chatbot

```bash
python chatbot.py
```

**Should see:**
```
🤖  RAG Chatbot - Knowledge Base Assistant

You: What is RAG?
Bot: [Detailed answer about RAG...]
```

---

## 🐛 Troubleshooting

### "Python not found"

**Solution:**
- Install Python 3.8+ from python.org
- Or use `py` instead of `python` on Windows

---

### "pip not found"

**Solution:**
```bash
# Windows
py -m pip install -r requirements.txt

# Linux/Mac
python3 -m pip install -r requirements.txt
```

---

### "Module 'haystack' not found"

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or specific package
pip install haystack-ai
```

---

### "torch installation fails"

**Solution:**
```bash
# Install CPU version (smaller, no GPU)
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

---

### "Ollama connection error"

**Solution:**
1. Check Ollama is installed: `ollama --version`
2. Ensure model is downloaded: `ollama pull llama3.2`
3. Check Ollama is running: `ollama serve`

---

### "OpenAI API error"

**Solution:**
1. Check API key in `.env` file
2. Verify key at: https://platform.openai.com/api-keys
3. Ensure `LLM_PROVIDER=openai` in `.env`

---

### "No documents found"

**Solution:**
1. Add files to `documents/` folder
2. Run: `python ingest_documents.py`
3. Or load samples: `python ingest_documents.py --samples`

---

## 📊 Installation Checklist

After installation, you should have:

- [x] Python 3.8+ installed
- [x] All pip packages installed (~2GB)
- [x] `.env` configuration file created
- [x] Sample documents loaded (optional)
- [x] Vector database created
- [x] Ollama installed + model downloaded (if using local)
- [x] OR OpenAI API key configured (if using cloud)
- [x] All tests passing

**Run this to verify:**
```bash
python tests/test_setup.py
```

---

## 🚀 Post-Installation

### Next Steps:

1. **Add your documents:**
   ```bash
   # Copy files to documents/
   cp your-files.pdf documents/
   
   # Ingest them
   python ingest_documents.py
   ```

2. **Start chatting:**
   ```bash
   python chatbot.py
   ```

3. **Explore features:**
   - Switch providers: `python switch_provider.py`
   - Compare models: `python tests/compare_models.py`
   - View docs: `docs/` folder

---

## 🔄 Updating

### Update Python Packages

```bash
pip install -r requirements.txt --upgrade
```

### Update Ollama Model

```bash
ollama pull llama3.2
```

### Update Project

```bash
git pull  # If using git
# Or download latest release
```

---

## 💾 Disk Space Requirements

| Component | Size | Required |
|-----------|------|----------|
| Python packages | ~2 GB | ✅ Yes |
| Ollama (app) | ~500 MB | Optional |
| Ollama model (llama3.2) | ~2 GB | Optional |
| Document embeddings | Varies | Auto-created |
| **Total (with Ollama)** | **~4.5 GB** | - |
| **Total (OpenAI only)** | **~2 GB** | - |

---

## 🌐 Network Requirements

### Initial Setup:
- **Required:** Internet to download Python packages (~2 GB)
- **Optional:** Download Ollama model (~2 GB)

### After Setup:
- **OpenAI:** Requires internet for API calls
- **Ollama:** Works completely offline! ✅

---

## ⚡ Performance Notes

### Minimum Requirements:
- **CPU:** Any modern processor
- **RAM:** 4 GB minimum, 8 GB recommended
- **Disk:** 5 GB free space
- **GPU:** Optional (speeds up embeddings)

### With Ollama:
- **RAM:** 8 GB recommended
- **CPU:** Better CPU = faster responses
- **GPU:** Can use GPU if available

---

## 📖 Additional Resources

- **Quick Start:** [`docs/OUT_OF_BOX_GUIDE.md`](docs/OUT_OF_BOX_GUIDE.md)
- **File Formats:** [`docs/guides/FILE_FORMATS.md`](docs/guides/FILE_FORMATS.md)
- **Privacy Guide:** [`docs/guides/PRIVACY.md`](docs/guides/PRIVACY.md)
- **Full Documentation:** [`docs/`](docs/) folder

---

## ✨ Out-of-Box Features

**This installation includes EVERYTHING:**

✅ **Both LLM options** (OpenAI + Ollama)
✅ **6 file formats** (TXT, MD, PDF, DOCX, HTML, JSON)
✅ **Local embeddings** (100% private)
✅ **Complete documentation**
✅ **Menu system** (Windows)
✅ **All tests included**
✅ **Sample data ready**
✅ **Zero additional config needed**

**Just install and use!** 🎉

---

**Questions? Check the troubleshooting section or see [`docs/guides/QUICKSTART.md`](docs/guides/QUICKSTART.md)**
