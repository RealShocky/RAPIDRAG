# Project Structure

Complete overview of the RAG Chatbot project organization.

---

## 📂 Directory Layout

```
RAG/
│
├── 📄 Core Application Files (Root)
│   ├── chatbot.py              # Interactive chatbot interface
│   ├── ingest_documents.py     # Document processing & embedding
│   ├── rag_pipeline.py         # RAG query pipeline
│   ├── config.py               # Configuration management
│   ├── setup.py                # Interactive setup wizard
│   └── switch_provider.py      # Toggle OpenAI ↔ Ollama
│
├── 📚 Documentation (docs/)
│   ├── README.md               # Main documentation
│   ├── PROJECT_OVERVIEW.md     # Technical architecture
│   ├── GET_STARTED.txt         # Quick reference card
│   ├── STRUCTURE.md            # This file
│   └── guides/                 # Detailed guides
│       ├── QUICKSTART.md       # 5-minute walkthrough
│       ├── PRIVACY.md          # Privacy & security guide
│       └── FILE_FORMATS.md     # Supported formats guide
│
├── 🧪 Tests (tests/)
│   ├── test_setup.py           # System verification
│   ├── test_chat.py            # Automated Q&A test
│   └── compare_models.py       # OpenAI vs Ollama comparison
│
├── 📂 User Data
│   ├── documents/              # 👈 YOUR KNOWLEDGE BASE FILES GO HERE
│   │   ├── README.md           # Format & usage guide
│   │   ├── *.txt               # Plain text files
│   │   ├── *.md                # Markdown files
│   │   ├── *.pdf               # PDF documents
│   │   ├── *.docx              # Word documents
│   │   ├── *.html              # HTML pages
│   │   └── ...                 # Any subfolder structure
│   │
│   └── data/                   # Generated data (auto-created)
│       └── document_store.json # Embedded knowledge base
│
├── ⚙️ Configuration
│   ├── .env                    # Your settings (gitignored)
│   ├── .env.example            # Configuration template
│   ├── requirements.txt        # Python dependencies
│   └── .gitignore              # Git exclusions
│
└── 🛠️ Utility Scripts
    └── reorganize.py           # Project reorganization script

```

---

## 📄 Core Application Files

### `chatbot.py`
**Interactive chatbot interface**

- Rich CLI with colors and formatting
- Command system (help, info, history, clear, exit)
- Real-time question answering
- Conversation history tracking
- Error handling and user feedback

**Usage:**
```bash
python chatbot.py
```

---

### `ingest_documents.py`
**Document ingestion pipeline**

- Multi-format support (TXT, MD, PDF, DOCX, HTML, JSON)
- Recursive directory scanning
- Embedding generation (local)
- Document store persistence
- Progress indicators

**Usage:**
```bash
# Ingest from documents/ folder
python ingest_documents.py

# Load sample documents
python ingest_documents.py --samples

# Specify custom source
python ingest_documents.py --source /path/to/docs
```

**Key Functions:**
- `load_pdf()` - Extract text from PDFs
- `load_docx()` - Process Word documents
- `load_html()` - Parse HTML pages
- `load_json()` - Handle JSON data
- `load_documents_from_directory()` - Main ingestion logic
- `save_document_store()` - Persist embeddings

---

### `rag_pipeline.py`
**RAG query processing pipeline**

- Query embedding generation
- Semantic document retrieval
- Prompt building with context
- LLM response generation
- Provider abstraction (OpenAI/Ollama)

**Classes:**
- `RAGPipeline` - Full RAG implementation
- `SimpleRAGPipeline` - Convenient wrapper

**Usage:**
```python
from rag_pipeline import SimpleRAGPipeline

rag = SimpleRAGPipeline()
rag.initialize()
answer = rag.ask("What is RAG?")
```

---

### `config.py`
**Configuration management**

- Environment variable loading (.env)
- Multi-provider configuration
- Path management
- Validation and error checking
- Safe secret handling

**Key Settings:**
- `LLM_PROVIDER` - openai / ollama / huggingface
- `EMBEDDING_MODEL` - Sentence transformer model
- `TOP_K_RETRIEVAL` - Number of documents to retrieve
- Provider-specific configs (API keys, URLs, models)

---

### `setup.py`
**Interactive setup wizard**

- Provider selection (OpenAI/Ollama/HuggingFace)
- API key configuration
- .env file creation
- Directory setup
- Guided onboarding

**Usage:**
```bash
python setup.py
```

---

### `switch_provider.py`
**LLM provider switcher**

- Toggle between OpenAI ↔ Ollama
- Update .env configuration
- Display current status
- Interactive confirmation

**Usage:**
```bash
python switch_provider.py
```

---

## 📚 Documentation

### docs/README.md
Main project documentation with quick start, architecture, and usage.

### docs/PROJECT_OVERVIEW.md
Technical deep-dive including:
- System architecture
- Component details
- Data flow diagrams
- Configuration options
- Extending the system

### docs/GET_STARTED.txt
Quick reference card for immediate use.

### docs/STRUCTURE.md
This file - complete project organization guide.

### docs/guides/QUICKSTART.md
5-minute walkthrough from install to first chat.

### docs/guides/PRIVACY.md
Privacy and security comprehensive guide:
- OpenAI vs Local comparison
- Data flow diagrams
- Security best practices
- Compliance considerations

### docs/guides/FILE_FORMATS.md
Complete guide to supported file formats:
- Format capabilities
- Requirements
- Limitations
- Troubleshooting

---

## 🧪 Tests

### tests/test_setup.py
**System verification tests**

Checks:
- Package imports
- File structure
- Directory existence
- Configuration validity

**Usage:**
```bash
python tests/test_setup.py
```

---

### tests/test_chat.py
**Automated Q&A testing**

- Runs predefined questions
- Validates answers
- Performance checking
- Quick system test

**Usage:**
```bash
python tests/test_chat.py
```

---

### tests/compare_models.py
**Provider comparison**

- Tests both OpenAI and Ollama
- Performance metrics
- Side-by-side answers
- Feature comparison table

**Usage:**
```bash
python tests/compare_models.py
```

---

## 📂 Data Directories

### documents/
**Your knowledge base files**

- Place all documents here
- Supports nested folders
- Multiple formats supported
- See `documents/README.md` for details

**Supported:**
- `.txt` - Plain text
- `.md` - Markdown
- `.pdf` - PDF documents
- `.docx` - Word files
- `.html`, `.htm` - HTML pages
- `.json` - JSON data

---

### data/
**Generated data (auto-created)**

- `document_store.json` - Embedded document database
- Created automatically during ingestion
- Persists between runs
- Contains documents + embeddings

---

## ⚙️ Configuration Files

### .env
**Your private configuration**

- LLM provider selection
- API keys (not in git)
- Model settings
- Paths and options
- Created by `setup.py`

**Example:**
```bash
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
TOP_K_RETRIEVAL=3
```

---

### .env.example
**Configuration template**

- Sample configuration
- All available options
- Default values
- Comment annotations

---

### requirements.txt
**Python dependencies**

- Core framework (Haystack)
- Embeddings (sentence-transformers)
- LLM integrations
- Document processors
- CLI utilities

**Install:**
```bash
pip install -r requirements.txt
```

---

### .gitignore
**Git exclusions**

Excludes:
- `.env` (secrets)
- `__pycache__/`
- `data/` (generated)
- `*.pyc`
- OS-specific files

---

## 🔄 Data Flow

### Document Ingestion Flow
```
documents/
    ↓
ingest_documents.py
    ├→ load_pdf/docx/html/json()
    ├→ SentenceTransformersDocumentEmbedder
    ├→ InMemoryDocumentStore
    └→ data/document_store.json
```

### Query Flow
```
User Question
    ↓
chatbot.py
    ↓
rag_pipeline.py
    ├→ SentenceTransformersTextEmbedder (local)
    ├→ InMemoryEmbeddingRetriever
    ├→ ChatPromptBuilder
    └→ LLM (OpenAI/Ollama)
        ↓
    Answer
```

---

## 🛠️ Development Files

### reorganize.py
Project reorganization utility (used once during setup).

---

## 📊 File Statistics

**Total Files:**
- Core: 6 files
- Docs: 7 files
- Tests: 3 files
- Config: 4 files
- Total: ~20 files

**Lines of Code:**
- Core application: ~1,500 lines
- Documentation: ~2,000 lines
- Tests: ~500 lines

---

## 🎯 Quick Navigation

**Want to...**

| Task | Go to |
|------|-------|
| Start chatting | Run `chatbot.py` |
| Add documents | `documents/` folder |
| Configure system | Edit `.env` |
| Read docs | `docs/README.md` |
| Test system | Run `tests/test_setup.py` |
| Switch LLM | Run `switch_provider.py` |
| Learn formats | `docs/guides/FILE_FORMATS.md` |
| Privacy info | `docs/guides/PRIVACY.md` |

---

## 🔍 Finding Things

### Configuration
```
.env                    # Your settings
.env.example            # Template
config.py               # Config loader
```

### Documentation
```
docs/README.md          # Start here
docs/guides/            # All guides
```

### Code
```
*.py                    # Root directory
tests/*.py              # Test files
```

### Data
```
documents/              # Your files
data/                   # Generated
```

---

## 📝 Notes

1. **Never edit `data/document_store.json` manually** - regenerate with ingestion
2. **Keep `.env` private** - it's in .gitignore
3. **Documents folder is for you** - organize however you like
4. **Tests are safe to run** - they won't modify data

---

**This structure keeps everything organized and easy to find!** 🎯
