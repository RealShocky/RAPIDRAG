# RAG Chatbot with Haystack

A privacy-focused Retrieval-Augmented Generation (RAG) chatbot built with Haystack framework. Supports both cloud-based (OpenAI) and local LLM options for maximum data privacy.

## 🔒 Privacy Options

### Cloud Option (OpenAI)
- Uses OpenAI API (data sent to OpenAI servers)
- OpenAI doesn't use API data for training
- Fastest and most capable responses

### Local Options (Maximum Privacy)
- **Ollama**: Run models like Llama, Mistral locally
- **HuggingFace**: Run open-source models on your hardware
- **All data stays on your machine**
- Embeddings always run locally regardless of LLM choice

## 🏗️ Architecture

```
User Query → Text Embedder → Retriever → Prompt Builder → LLM → Response
                    ↓
            Document Store (with embeddings)
```

### Components
- **Document Store**: InMemoryDocumentStore (stores documents + embeddings)
- **Embedder**: SentenceTransformers (all-MiniLM-L6-v2) - runs locally
- **Retriever**: Semantic search using embeddings
- **Generator**: OpenAI GPT / Ollama / HuggingFace (configurable)

## 📦 Installation

1. **Clone and setup**
```bash
cd c:\Users\markv\Downloads\RAG
pip install -r requirements.txt
```

2. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your settings
```

3. **Choose your LLM provider**

**Option A: OpenAI (Cloud)**
- Set `LLM_PROVIDER=openai` in `.env`
- Add your OpenAI API key

**Option B: Ollama (Local - Recommended for Privacy)**
- Install Ollama: https://ollama.ai
- Pull a model: `ollama pull llama3.2`
- Set `LLM_PROVIDER=ollama` in `.env`
- No API key needed!

**Option C: HuggingFace (Local)**
- Set `LLM_PROVIDER=huggingface` in `.env`
- Models download automatically

## 🚀 Usage

### 1. Ingest Documents
```bash
python ingest_documents.py --source ./documents
```

Add your documents to `./documents` folder (supports .txt, .pdf, .docx, etc.)

### 2. Run Chatbot
```bash
python chatbot.py
```

### 3. Interactive Chat
```
You: What is the capital of France?
Bot: Based on the documents, Paris is the capital of France...

You: exit  # to quit
```

## 📁 Project Structure

```
RAG/
├── requirements.txt          # Python dependencies
├── .env.example             # Configuration template
├── README.md                # This file
├── config.py                # Configuration management
├── ingest_documents.py      # Document ingestion pipeline
├── rag_pipeline.py          # RAG query pipeline
├── chatbot.py               # Interactive chatbot interface
├── documents/               # Place your documents here
└── data/                    # Document store (auto-created)
```

## 🔧 Configuration

Edit `.env` to customize:
- `LLM_PROVIDER`: Choose between "openai", "ollama", or "huggingface"
- `EMBEDDING_MODEL`: Change embedding model
- `TOP_K_RETRIEVAL`: Number of documents to retrieve
- Model-specific settings

## 🛡️ Security Best Practices

1. **Never commit `.env` file** (already in .gitignore)
2. **For maximum privacy**: Use Ollama or HuggingFace models
3. **API keys**: Store in `.env`, never hardcode
4. **Embeddings**: Always run locally (no data sent to cloud)

## 📚 Adding Your Knowledge Base

1. Place documents in `./documents/` folder
2. Run `python ingest_documents.py`
3. Documents are embedded and stored locally
4. Start chatting with `python chatbot.py`

## 🎯 Features

- ✅ Multiple LLM provider support (OpenAI, Ollama, HuggingFace)
- ✅ Local embeddings (privacy-first)
- ✅ Semantic search with RAG
- ✅ Easy document ingestion
- ✅ Interactive chat interface
- ✅ Configuration management
- ✅ Beautiful CLI output

## 📖 Documentation

- [Haystack Documentation](https://haystack.deepset.ai/)
- [RAG Tutorial](https://haystack.deepset.ai/tutorials/27_first_rag_pipeline)
- [Ollama Models](https://ollama.ai/library)

## 🤝 Support

For issues or questions, refer to:
- Haystack Discord: https://discord.com/invite/xYvH6drSmA
- GitHub Discussions: https://github.com/deepset-ai/haystack/discussions
