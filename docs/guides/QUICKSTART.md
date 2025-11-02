# Quick Start Guide - RAG Chatbot

Get your RAG chatbot running in 5 minutes!

## 🚀 Installation

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run setup wizard (interactive)
python setup.py
```

The setup wizard will help you:
- Choose between OpenAI (cloud) or Ollama/HuggingFace (local)
- Configure API keys if needed
- Set up your environment

## 📚 Add Knowledge Base

### Option A: Use Sample Documents (Quick Test)
```bash
python ingest_documents.py --samples
```

This loads sample documents about RAG, Haystack, embeddings, and privacy.

### Option B: Use Your Own Documents
```bash
# 1. Add your .txt or .md files to ./documents/
# 2. Run ingestion
python ingest_documents.py
```

## 💬 Start Chatting

```bash
python chatbot.py
```

That's it! Start asking questions about your documents.

## 🔒 Privacy Options

### Maximum Privacy - Use Ollama (Recommended)

1. **Install Ollama**: https://ollama.ai
2. **Pull a model**:
   ```bash
   ollama pull llama3.2
   ```
3. **Set in .env**:
   ```
   LLM_PROVIDER=ollama
   OLLAMA_MODEL=llama3.2
   ```

**Benefits**: All data stays on your machine, no API keys needed!

### Cloud Option - OpenAI

1. **Get API key**: https://platform.openai.com/api-keys
2. **Set in .env**:
   ```
   LLM_PROVIDER=openai
   OPENAI_API_KEY=your_key_here
   ```

**Benefits**: Fastest responses, most capable model

## 📋 Example Session

```
You: What is RAG?
Bot: Retrieval-Augmented Generation (RAG) is a technique that combines
     information retrieval with text generation...

You: How does it work?
Bot: RAG works by first retrieving relevant documents from a knowledge
     base, then using those documents as context...

You: exit
```

## 🛠️ Commands

- `help` - Show available commands
- `info` - Display system information
- `history` - Show conversation history
- `clear` - Clear conversation history
- `exit` - Quit chatbot

## 🎯 Tips

- Ask specific questions for better answers
- The system automatically retrieves relevant context
- Adjust `TOP_K_RETRIEVAL` in .env to control context size
- Add more documents anytime and re-run ingestion

## ❓ Troubleshooting

### "Document store not found"
→ Run `python ingest_documents.py --samples` first

### "OPENAI_API_KEY is required"
→ Add your API key to .env or switch to Ollama

### "Ollama connection error"
→ Make sure Ollama is running: `ollama serve`

## 📖 Learn More

- Full README: [README.md](README.md)
- Haystack Docs: https://haystack.deepset.ai/
- Ollama Models: https://ollama.ai/library
