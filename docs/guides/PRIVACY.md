# Privacy & Security Guide

## 🔒 Data Privacy Options

This RAG chatbot gives you full control over your data privacy. Choose the option that best fits your security requirements.

### Option 1: Maximum Privacy (Recommended)

**Use Ollama or HuggingFace with local models**

✅ **Benefits:**
- All data stays on your machine
- No external API calls
- No data sent to third parties
- Complete control over your infrastructure
- No API keys or accounts needed
- Free to use

❌ **Considerations:**
- Requires adequate computing resources (GPU recommended)
- Slightly slower than cloud APIs
- May need to download large models (GBs)

**Setup:**
```bash
# Install Ollama
# Visit: https://ollama.ai

# Pull a model
ollama pull llama3.2

# Configure .env
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2
```

### Option 2: Cloud-Based (OpenAI)

**Use OpenAI API**

✅ **Benefits:**
- Fastest response times
- Most capable models
- No local resource requirements
- Easy setup

❌ **Privacy Considerations:**
- Data sent to OpenAI servers
- Requires API account
- Costs money (pay per use)
- Subject to OpenAI's data policies

**OpenAI's Data Policy:**
- API data is NOT used for training by default
- Data may be retained for 30 days for abuse monitoring
- Enterprise agreements offer additional protections
- See: https://openai.com/enterprise-privacy

**Setup:**
```bash
# Get API key from OpenAI
# Visit: https://platform.openai.com/api-keys

# Configure .env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
```

## 🛡️ Security Best Practices

### 1. API Key Management

**DO:**
- ✅ Store API keys in `.env` file
- ✅ Add `.env` to `.gitignore` (already done)
- ✅ Use environment variables
- ✅ Rotate keys regularly
- ✅ Use read-only keys when possible

**DON'T:**
- ❌ Hardcode API keys in source code
- ❌ Commit `.env` to version control
- ❌ Share API keys in chat/email
- ❌ Use production keys for testing
- ❌ Store keys in plain text files outside .env

### 2. Document Security

**Sensitive Documents:**
- Review documents before ingestion
- Consider using local-only models for sensitive data
- Be aware of document metadata
- Regularly audit your knowledge base

**Document Store:**
- Stored locally at `./data/document_store.json`
- Contains document content and embeddings
- Not encrypted by default
- Backup regularly

### 3. Embeddings Privacy

**Good News:**
- Embeddings ALWAYS run locally
- Uses sentence-transformers library
- No data sent to external services
- True regardless of LLM choice

**What are embeddings?**
- Vector representations of text
- Used for semantic search
- Generated on your machine
- Stored in local document store

## 🔐 Privacy Comparison Table

| Feature | Ollama/HuggingFace | OpenAI API |
|---------|-------------------|------------|
| Data Location | Local only | Sent to OpenAI |
| API Keys | Not required | Required |
| Training Data | Data stays private | Not used for training* |
| Cost | Free | Pay per use |
| Processing | Your hardware | Cloud servers |
| Privacy Level | **Maximum** | Moderate |
| Embeddings | Local | Local |
| Document Store | Local | Local |

*Per OpenAI API terms of service

## 📊 What Data is Shared?

### With Local Models (Ollama/HuggingFace):
- ❌ Nothing - All processing is local
- ✅ Complete data privacy

### With OpenAI:
- ✅ Your questions
- ✅ Retrieved document excerpts (context)
- ✅ Generated responses
- ❌ NOT your full document store
- ❌ NOT used for model training

## 🏢 Enterprise/Compliance Considerations

### For Maximum Compliance:
1. **Use local models** (Ollama/HuggingFace)
2. **Deploy on private infrastructure**
3. **Encrypt document store at rest**
4. **Use VPCs/private networks**
5. **Audit all data access**

### Compliance Frameworks:
- **GDPR**: Local models recommended
- **HIPAA**: Use local models + encryption
- **SOC 2**: Both options viable with proper controls
- **ISO 27001**: Risk assessment required for cloud APIs

## 🤝 Recommendations by Use Case

### Public/Non-Sensitive Data:
- **Recommendation**: OpenAI for speed
- Documentation, public FAQs, general knowledge

### Internal Company Data:
- **Recommendation**: Ollama locally
- Policies, procedures, internal docs

### Confidential/PII Data:
- **Recommendation**: Ollama locally + encryption
- Customer data, medical records, financial info

### Development/Testing:
- **Recommendation**: Sample documents + Ollama
- Quick testing without privacy concerns

## 📞 Questions?

- Review your organization's data policies
- Consult with security/legal teams
- Test with non-sensitive data first
- Choose privacy level based on data sensitivity

**Remember**: You can always switch providers by changing `.env` configuration!
