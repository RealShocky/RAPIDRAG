# Out-of-the-Box Quick Start Guide

Get your RAG Chatbot running in **under 5 minutes** with zero configuration!

---

## 🚀 Fastest Way to Start (Windows)

### **Option 1: Double-Click START.bat (Easiest)**

1. **Double-click `START.bat`**
2. Select "Y" for automatic setup
3. Wait 2-5 minutes for installation
4. Start chatting!

That's it! The script handles everything automatically.

---

### **Option 2: Using Menu System**

1. **Double-click `rag-menu.bat`**
2. **Select option 1**: "First-Time Setup"
3. Wait for installation to complete
4. **Select option 6**: "Start Chatbot"

---

## 📋 What Gets Installed Automatically

### ✅ Installed with `pip install -r requirements.txt`:

**Core Framework:**
- `haystack-ai` - RAG framework
- `sentence-transformers` - Local embeddings
- `torch` - ML backend

**LLM Integrations (Both Included!):**
- `openai` - For OpenAI API (cloud)
- `ollama-haystack` - For Ollama (local) ✨

**Document Processing (6 Formats):**
- `pypdf` - PDF files
- `python-docx` - Word documents
- `beautifulsoup4` + `lxml` - HTML pages
- `markdown` - Enhanced markdown
- Built-in: TXT, JSON

**Utilities:**
- `python-dotenv` - Configuration
- `rich` - Beautiful CLI
- `datasets` - Data handling

**Total:** ~15 packages + dependencies (~2GB)

---

## 🎯 Complete Setup Options

### Menu System (`rag-menu.bat`)

```
========================================================================
                    RAG CHATBOT - CONTROL PANEL
========================================================================

  [SETUP]
  1. First-Time Setup (Install dependencies + configure)
  2. Install/Update Python Dependencies
  3. Install Ollama + Download Model
  4. Run Setup Wizard (Configure .env)

  [OPERATIONS]
  5. Ingest Documents (Add to knowledge base)
  6. Start Chatbot (Interactive chat)
  7. Switch LLM Provider (OpenAI <-> Ollama)

  [TESTING]
  8. Test System Setup
  9. Quick Q&A Test
  10. Compare OpenAI vs Ollama

  [UTILITIES]
  11. View Documentation
  12. Open Documents Folder
  13. View System Status
```

---

## 🔧 First-Time Setup (Option 1)

### What It Does:

**Step 1: Install Dependencies** (2-3 minutes)
- Installs all Python packages from `requirements.txt`
- Includes both OpenAI and Ollama support
- All document format processors

**Step 2: Configuration Wizard** (1 minute)
- Creates `.env` file
- Lets you choose LLM provider
- Sets up API keys (optional)

**Step 3: Load Sample Documents** (30 seconds)
- Adds 4 sample documents about RAG
- Creates vector database
- Ready for testing

**Total Time:** 3-5 minutes

---

## 🤖 LLM Provider Options

### Option A: Ollama (100% Local - Recommended)

**Pros:**
- ✅ 100% private - no data leaves your machine
- ✅ Free forever
- ✅ No API keys needed
- ✅ Already included in setup

**Installation:**
1. Download Ollama: https://ollama.ai/download/windows
2. Run `rag-menu.bat` → Option 3
3. Downloads llama3.2 model (~2GB)

**Total time:** 5-10 minutes (one-time)

---

### Option B: OpenAI (Cloud - Faster)

**Pros:**
- ✅ Fastest responses
- ✅ Most capable model
- ✅ No local resource usage

**Setup:**
1. Get API key: https://platform.openai.com/api-keys
2. Edit `.env` file: `OPENAI_API_KEY=your_key_here`
3. Set: `LLM_PROVIDER=openai`

**Cost:** ~$0.01 per 1000 messages

---

## 📂 Adding Your Documents

### Automatic Detection - Just Drop Files!

**Supported formats (all auto-detected):**

```
documents/
├── report.pdf          ✅ Auto-processed
├── notes.docx          ✅ Auto-processed
├── webpage.html        ✅ Auto-processed
├── readme.md           ✅ Auto-processed
├── data.json           ✅ Auto-processed
└── text.txt            ✅ Auto-processed
```

**Then:**
- Run `rag-menu.bat` → Option 5
- Or run: `py ingest_documents.py`

**That's it!** All formats processed automatically.

---

## ⚡ Quick Reference

### Essential Commands

| Action | Menu Option | Command |
|--------|-------------|---------|
| **First Setup** | Option 1 | Auto-installs everything |
| **Add Documents** | Option 5 | Processes all formats |
| **Start Chat** | Option 6 | Interactive chatbot |
| **Test System** | Option 8 | Verify installation |
| **Get Ollama** | Option 3 | Download local model |

---

## 🎯 Usage Examples

### Example 1: Quick Test (No Setup)

```batch
1. Double-click START.bat
2. Choose "Y" for setup
3. Wait 3-5 minutes
4. Start chatting!
```

**Total time:** 5 minutes to first chat

---

### Example 2: With Your Documents

```batch
1. Copy your PDFs/DOCX/HTML to documents/
2. Run rag-menu.bat
3. Option 1 (First-Time Setup)
4. Option 5 (Ingest Documents)
5. Option 6 (Start Chatbot)
```

**Total time:** 10 minutes to chat with your files

---

### Example 3: Maximum Privacy (Ollama)

```batch
1. Download Ollama from https://ollama.ai
2. Run rag-menu.bat → Option 3 (Download model)
3. Option 4 (Setup wizard) → Choose Ollama
4. Option 6 (Start chatting)
```

**Total time:** 15 minutes (includes model download)

---

## 🔍 System Status Check

**Menu Option 13** shows:
- Python version
- Ollama installation status
- Configuration status
- Knowledge base status
- Document count

---

## 🛠️ Troubleshooting

### "Python not found"
**Solution:** Install Python 3.8+ from python.org

### "pip not found"
**Solution:** Use `py -m pip` instead of `pip`

### "Module not found"
**Solution:** Run menu option 2 (Install Dependencies)

### "Ollama not found"
**Solution:** 
1. Download from https://ollama.ai
2. Run menu option 3 to download model

### "No documents found"
**Solution:**
1. Add files to `documents/` folder
2. Run menu option 5 (Ingest Documents)

---

## 📊 What's Included Out-of-Box

| Component | Status | Notes |
|-----------|--------|-------|
| Python Framework | ✅ Auto-install | haystack-ai + dependencies |
| OpenAI Support | ✅ Included | Requires API key |
| Ollama Support | ✅ Included | Requires Ollama install |
| Embeddings | ✅ Included | 100% local |
| PDF Support | ✅ Included | Auto-install |
| Word Support | ✅ Included | Auto-install |
| HTML Support | ✅ Included | Auto-install |
| JSON Support | ✅ Included | Built-in |
| Sample Data | ✅ Included | Loaded in setup |
| Documentation | ✅ Included | docs/ folder |
| Tests | ✅ Included | tests/ folder |
| Menu System | ✅ Included | rag-menu.bat |

---

## 🎓 Next Steps

### After First Setup:

1. **Test the system:**
   - Menu option 9 (Quick Q&A Test)
   - Asks 3 sample questions

2. **Add your documents:**
   - Drop files in `documents/`
   - Menu option 5 (Ingest)

3. **Start chatting:**
   - Menu option 6 (Start Chatbot)
   - Type questions, get answers!

4. **Explore features:**
   - Menu option 7 (Switch providers)
   - Menu option 10 (Compare models)
   - Menu option 11 (View docs)

---

## 🚀 Production Deployment

### For Team Use:

1. **Share the entire folder**
2. **Each user runs:** `START.bat`
3. **Add team documents** to `documents/`
4. **Everyone uses same knowledge base**

### For Privacy:

1. **Use Ollama** (100% local)
2. **No internet required** after setup
3. **All data stays on machine**

---

## 📖 Additional Resources

- **Full guide:** `docs/guides/QUICKSTART.md`
- **File formats:** `docs/guides/FILE_FORMATS.md`
- **Privacy info:** `docs/guides/PRIVACY.md`
- **Architecture:** `docs/PROJECT_OVERVIEW.md`

---

## ✅ Success Checklist

After running first-time setup, you should have:

- [x] All Python packages installed
- [x] `.env` configuration file created
- [x] Sample documents loaded
- [x] Vector database created (`data/document_store.json`)
- [x] System tested and verified

**You're ready to chat!** 🎉

---

## 🎯 TL;DR - Absolute Fastest Start

```batch
# 1. Double-click this file:
START.bat

# 2. Press Y when asked

# 3. Wait 5 minutes

# 4. Start chatting!
```

**That's literally it.** Everything else is automatic! 🚀

---

## 💡 Pro Tips

1. **Test first** with sample documents (option 1 does this)
2. **Use menu option 13** to check system status
3. **Both OpenAI and Ollama** are installed - switch anytime
4. **Add more documents** anytime - just re-run ingestion
5. **All 6 file formats** work out-of-box

---

**The RAG Chatbot is designed to work immediately with zero manual configuration!**

Just run `START.bat` and you're good to go! 🎉
