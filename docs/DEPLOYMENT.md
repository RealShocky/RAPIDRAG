# 🚀 RAPIDRAG Deployment Information

## Live Deployment

**RAPIDRAG is live and accessible at:**

### 🌐 https://rapidrag.streamlit.app

---

## Deployment Details

**Platform:** Streamlit Cloud  
**Repository:** https://github.com/RealShocky/RAPIDRAG  
**Branch:** main  
**Main File:** webapp.py  
**Status:** ✅ Live

---

## Features Available in Cloud

✅ **Full Web Interface**
- Lightning fast RAPIDRAG UI
- Document upload (all 6 formats)
- Interactive chat
- Analytics dashboard
- Real-time updates

✅ **Powered by OpenAI**
- Uses OpenAI for LLM (cloud requirement)
- Local embeddings still work
- Fast response times

✅ **Secure & Encrypted**
- HTTPS/SSL automatic
- GitHub OAuth
- Secrets encrypted

---

## Differences from Local

| Feature | Local | Cloud |
|---------|-------|-------|
| **LLM** | OpenAI + Ollama | OpenAI only |
| **Access** | Your network | Internet |
| **Auth** | None | GitHub OAuth |
| **Privacy** | Maximum | Standard cloud |
| **Offline** | Yes (Ollama) | No |
| **Cost** | Free | Free |

---

## Auto-Deploy

**Every push to main branch triggers auto-deploy:**

```bash
# Make changes
git add .
git commit -m "Update features"
git push origin main

# Streamlit Cloud auto-deploys
# Wait 1-2 minutes
# Changes live!
```

---

## Monitoring

**Check deployment status:**
- Dashboard: https://share.streamlit.io
- Logs: Available in Streamlit Cloud dashboard
- Metrics: Built-in analytics

---

## URLs

**Production:** https://rapidrag.streamlit.app  
**Repository:** https://github.com/RealShocky/RAPIDRAG  
**Documentation:** https://github.com/RealShocky/RAPIDRAG/tree/main/docs

---

## Support

**For deployment issues:**
1. Check Streamlit Cloud logs
2. Review [DEPLOYMENT_GUIDE.md](guides/DEPLOYMENT_GUIDE.md)
3. Check [NETWORK_SHARING.md](NETWORK_SHARING.md)

---

**RAPIDRAG is deployed and ready to use!** ⚡🚀
