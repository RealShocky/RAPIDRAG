# Supported File Formats

Complete guide to all supported document formats for the RAG knowledge base.

---

## 📋 Format Summary

| Format | Extension | Status | Best For |
|--------|-----------|--------|----------|
| Plain Text | `.txt` | ✅ Full Support | Simple text content |
| Markdown | `.md` | ✅ Full Support | Formatted documentation |
| PDF | `.pdf` | ✅ Full Support | Reports, papers, books |
| Word | `.docx` | ✅ Full Support | Office documents |
| Excel | `.xlsx`, `.xls` | ✅ Full Support | Spreadsheets, data tables |
| PowerPoint | `.pptx` | ✅ Full Support | Presentations, slides |
| CSV | `.csv` | ✅ Full Support | Data files, tables |
| HTML | `.html`, `.htm` | ✅ Full Support | Web pages, articles |
| XML | `.xml` | ✅ Full Support | Structured data |
| JSON | `.json` | ✅ Full Support | Structured data |
| RTF | `.rtf` | ✅ Full Support | Rich text documents |
| EPUB | `.epub` | ✅ Full Support | E-books |
| **Code Files** | `.py`, `.js`, `.java`, etc. | ✅ Full Support | Source code, config files |

**Total:** 40+ file types supported!

---

## 📝 Plain Text Files (.txt)

**Best for:** Simple notes, logs, basic documentation

### Features
- ✅ Fast processing
- ✅ No dependencies
- ✅ UTF-8 encoding support
- ✅ Any size

### Example
```
documents/
└── notes.txt
```

### Limitations
- No formatting preservation
- Plain text only

---

## 📄 Markdown Files (.md)

**Best for:** Technical documentation, README files, formatted notes

### Features
- ✅ Formatting preserved as text
- ✅ Code blocks maintained
- ✅ Headers and lists
- ✅ Links extracted

### Example
```
documents/
├── README.md
└── api-docs.md
```

### Limitations
- Images not processed
- Rendered as plain text

---

## 📕 PDF Files (.pdf)

**Best for:** Reports, academic papers, books, official documents

### Requirements
```bash
pip install pypdf>=3.0.0
```

### Features
- ✅ Multi-page extraction
- ✅ Text layer reading
- ✅ Preserves document structure
- ✅ Large files supported

### Example
```
documents/
├── report_2024.pdf
└── whitepaper.pdf
```

### Limitations
- ⚠️ Scanned PDFs (images) won't extract text
- ⚠️ Complex tables may lose structure
- ⚠️ Images and graphics skipped
- ⚠️ Encrypted PDFs not supported

### Troubleshooting
**Issue:** No text extracted
- **Solution:** PDF may be scanned images. Use OCR software first.

**Issue:** Garbled text
- **Solution:** PDF may have encoding issues. Try re-saving.

---

## 📘 Word Documents (.docx)

**Best for:** Office documents, reports, proposals

### Requirements
```bash
pip install python-docx>=1.0.0
```

### Features
- ✅ Paragraph extraction
- ✅ Multi-section documents
- ✅ Headers and footers
- ✅ Fast processing

### Example
```
documents/
├── company-policies.docx
└── meeting-notes.docx
```

### Limitations
- ⚠️ Formatting removed
- ⚠️ Tables converted to text
- ⚠️ Images not processed
- ⚠️ Only `.docx` (not old `.doc` format)

### Troubleshooting
**Issue:** Old `.doc` files not supported
- **Solution:** Convert to `.docx` in Word

---

## 🌐 HTML Files (.html, .htm)

**Best for:** Web pages, online articles, documentation sites

### Requirements
```bash
pip install beautifulsoup4>=4.12.0
pip install lxml>=4.9.0
```

### Features
- ✅ Text content extraction
- ✅ Script/style removal
- ✅ Clean whitespace handling
- ✅ Nested structure support

### Example
```
documents/
├── article.html
└── docs.htm
```

### Limitations
- ⚠️ JavaScript content not executed
- ⚠️ Dynamic content skipped
- ⚠️ Images not processed
- ⚠️ CSS styling removed

### Processing Notes
- Scripts and styles automatically removed
- Links extracted as text
- Tables converted to text
- Clean formatting applied

---

## 🔧 JSON Files (.json)

**Best for:** Configuration data, structured information, API responses

### Features
- ✅ Full structure preserved
- ✅ Pretty-printed output
- ✅ Nested objects supported
- ✅ Arrays handled

### Example
```
documents/
├── config.json
└── api-response.json
```

### Usage Example
Input:
```json
{
  "product": "RAG Chatbot",
  "features": ["embeddings", "retrieval", "generation"]
}
```

Stored as:
```
{
  "product": "RAG Chatbot",
  "features": [
    "embeddings",
    "retrieval",
    "generation"
  ]
}
```

### Limitations
- Stored as formatted text, not structured
- Best for smaller JSON files
- Large files may impact performance

---

## 🚀 Installation

### Install All Format Support
```bash
pip install -r requirements.txt
```

This installs:
- `pypdf` - PDF support
- `python-docx` - Word documents
- `beautifulsoup4` + `lxml` - HTML support

### Install Specific Formats
```bash
# PDF only
pip install pypdf>=3.0.0

# Word only
pip install python-docx>=1.0.0

# HTML only
pip install beautifulsoup4>=4.12.0 lxml>=4.9.0
```

---

## 📥 Usage

### Basic Ingestion
```bash
# Process all supported formats in documents/
python ingest_documents.py
```

### What Gets Processed
The ingestion scans for:
- `.txt` - Plain text
- `.md` - Markdown
- `.pdf` - PDF documents
- `.docx` - Word documents
- `.html`, `.htm` - HTML files
- `.json` - JSON data

### Nested Directories
All subdirectories are scanned recursively:
```
documents/
├── folder1/
│   ├── file1.pdf
│   └── subfolder/
│       └── file2.docx
└── folder2/
    └── file3.txt
```
All files will be found and processed!

---

## 🔍 Format Detection

Format is automatically detected by file extension:

```python
# Automatic detection
file.txt   → Plain text handler
file.md    → Markdown handler
file.pdf   → PDF extractor
file.docx  → Word extractor
file.html  → HTML parser
file.json  → JSON processor
```

---

## ⚡ Performance Tips

### File Size
- **Small files** (<1MB): Fastest processing
- **Medium files** (1-10MB): Good performance
- **Large files** (>10MB): May take longer, but supported

### Recommendations
- ✅ Split very large PDFs into chapters
- ✅ Use plain text when possible (fastest)
- ✅ Organize by topic in subfolders
- ✅ Re-run ingestion only when adding new files

---

## 🛠️ Troubleshooting

### "Module not found" Errors
```bash
# Install missing dependencies
pip install pypdf python-docx beautifulsoup4 lxml
```

### File Not Processing
Check:
1. File extension is supported
2. File is not empty
3. File encoding is UTF-8
4. No file permission errors

### Garbled Text
- Check file encoding (should be UTF-8)
- For PDFs, ensure it's not a scanned image
- For Word docs, try re-saving

### Empty Results
- File may be scanned images (PDF)
- File may be protected/encrypted
- Check console output for specific errors

---

## 🎯 Best Practices

### File Organization
```
documents/
├── policies/          # Company policies
│   └── hr.pdf
├── technical/         # Technical docs
│   ├── api.md
│   └── architecture.docx
└── reference/         # Reference materials
    └── glossary.txt
```

### Naming Conventions
- ✅ Use descriptive names: `employee-handbook.pdf`
- ✅ Avoid special characters
- ✅ Use hyphens or underscores
- ❌ Avoid spaces in filenames

### Content Quality
- Keep documents focused on one topic
- Remove unnecessary files before ingestion
- Update knowledge base regularly
- Test with samples first

---

## 📚 Examples

See the `examples/` folder for sample files in each format (if available), or run:

```bash
python ingest_documents.py --samples
```

This loads sample documents to test the system.

---

## 🔄 Adding New Formats

Want to support more formats? Edit `ingest_documents.py`:

1. Add import for new processor
2. Add extension to `supported_extensions`
3. Create `load_<format>()` method
4. Update this documentation

Example formats to add:
- `.csv` - CSV files
- `.xml` - XML documents
- `.epub` - E-books
- `.pptx` - PowerPoint

---

## 📞 Need Help?

- Check [`docs/guides/QUICKSTART.md`](QUICKSTART.md)
- Review error messages in console
- Ensure dependencies installed
- Test with sample files first
