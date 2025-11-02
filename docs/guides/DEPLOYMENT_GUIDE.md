# RAPIDRAG Deployment Guide

Complete guide to deploying RAPIDRAG for different scenarios.

---

## 🎯 Deployment Scenarios

### **1. Solo Use (Local)**
- **Complexity:** ⭐ Easy
- **Security:** ✅ Maximum
- **Setup time:** 1 minute
- **Cost:** Free

### **2. Team/Office (LAN)**
- **Complexity:** ⭐⭐ Easy
- **Security:** ✅ High
- **Setup time:** 2 minutes
- **Cost:** Free

### **3. Remote Team (Internet)**
- **Complexity:** ⭐⭐⭐ Medium
- **Security:** ⚠️ Requires work
- **Setup time:** 15-30 minutes
- **Cost:** Free - $$

### **4. Public/Production**
- **Complexity:** ⭐⭐⭐⭐ Advanced
- **Security:** ⚠️⚠️ Critical
- **Setup time:** 1-4 hours
- **Cost:** $ - $$$

---

## 🚀 Quick Start Deployments

### **Scenario 1: Solo Developer**

```bash
# Just run locally
start-webapp.bat
```

**Perfect for:**
- Personal use
- Development
- Testing
- Maximum privacy

---

### **Scenario 2: Office Team (Same Network)**

```bash
# Enable network access
start-webapp-network.bat

# Shows your IP:
Your IP: 192.168.1.100
Share: http://192.168.1.100:8501
```

**Perfect for:**
- Team collaboration
- Office environment
- Shared knowledge base
- Real-time updates

**Setup:**
1. Run `start-webapp-network.bat`
2. Note the IP shown
3. Share with team
4. Done!

**Security:** Protected by office firewall ✅

---

### **Scenario 3: External Access (You have port forwarding)**

```bash
# Enable external access
start-webapp-external.bat

# Configure:
1. Port forward 8501 on router
2. Share public IP
3. Access from anywhere
```

**Perfect for:**
- Remote work
- Client demos
- Field access
- Mobile access

**Requirements:**
- Router with port forwarding
- Static IP or Dynamic DNS
- Understanding of security risks

**Security:** ⚠️ Exposed - use with caution

**See:** [`docs/NETWORK_SHARING.md`](docs/NETWORK_SHARING.md) for details

---

## 🌐 Cloud Deployment Options

### **Option 1: Streamlit Cloud (Easiest)**

**Pros:**
- ✅ Free hosting
- ✅ Automatic SSL/HTTPS
- ✅ Built-in authentication
- ✅ Auto-deploys from GitHub
- ✅ No server management

**Cons:**
- ❌ Public (less private)
- ❌ Resource limits
- ❌ Cold starts

**Steps:**
```bash
# 1. Push to GitHub
git init
git add .
git commit -m "RAPIDRAG deployment"
git push origin main

# 2. Deploy
1. Visit share.streamlit.io
2. Connect GitHub repo
3. Select webapp.py
4. Deploy!

# 3. Share URL
https://rapidrag.streamlit.app
```

**Cost:** Free

**🎉 RAPIDRAG is deployed at: https://rapidrag.streamlit.app**

---

### **Option 2: AWS (Full Control)**

**Using EC2:**
```bash
# 1. Launch EC2 instance (t2.medium recommended)
# 2. SSH into instance
ssh -i key.pem ubuntu@your-ec2-ip

# 3. Install dependencies
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt

# 4. Run RAPIDRAG
py -m streamlit run webapp.py --server.port 8501 --server.address 0.0.0.0

# 5. Configure security group
Allow inbound: Port 8501 from your IP/range
```

**With authentication (recommended):**
```bash
# Use AWS IAM or reverse proxy with auth
```

**Cost:** ~$20-50/month

---

### **Option 3: Docker (Portable)**

**Create `Dockerfile`:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "webapp.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Deploy:**
```bash
# Build
docker build -t rapidrag .

# Run locally
docker run -p 8501:8501 rapidrag

# Or deploy to cloud
docker push your-registry/rapidrag
# Deploy on AWS ECS, Azure Container Instances, etc.
```

---

### **Option 4: Heroku (Simple)**

**Create `Procfile`:**
```
web: streamlit run webapp.py --server.port=$PORT --server.address=0.0.0.0
```

**Deploy:**
```bash
# Install Heroku CLI
# Login
heroku login

# Create app
heroku create rapidrag-yourname

# Deploy
git push heroku main

# Open
heroku open
```

**Cost:** Free tier available, ~$7/month for hobby

---

## 🔐 Adding Authentication

### **Option 1: Streamlit-Authenticator**

**Install:**
```bash
pip install streamlit-authenticator
```

**Add to `webapp.py`:**
```python
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load config
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Login widget
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    # Show RAPIDRAG interface
    main()
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
```

**Create `config.yaml`:**
```yaml
credentials:
  usernames:
    admin:
      email: admin@example.com
      name: Admin User
      password: $2b$12$... # hashed password
cookie:
  name: rapidrag_auth
  key: secret_key_here
  expiry_days: 30
```

---

### **Option 2: Nginx Reverse Proxy**

**Install Nginx:**
```bash
sudo apt install nginx apache2-utils
```

**Create password file:**
```bash
sudo htpasswd -c /etc/nginx/.htpasswd admin
```

**Configure Nginx (`/etc/nginx/sites-available/rapidrag`):**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        auth_basic "RAPIDRAG Access";
        auth_basic_user_file /etc/nginx/.htpasswd;
        
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

---

## 🔒 SSL/HTTPS Setup

### **Option 1: Let's Encrypt (Free)**

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal
sudo certbot renew --dry-run
```

---

### **Option 2: Cloudflare Tunnel (Easy)**

```bash
# Install cloudflared
# Download from: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/

# Login
cloudflared tunnel login

# Create tunnel
cloudflared tunnel create rapidrag

# Configure
cloudflared tunnel route dns rapidrag your-domain.com

# Run
cloudflared tunnel run rapidrag
```

**Benefits:**
- ✅ Free SSL
- ✅ DDoS protection
- ✅ No port forwarding needed
- ✅ Secure tunnel

---

## 📊 Monitoring & Logging

### **Basic Monitoring:**

```python
# Add to webapp.py
import logging

logging.basicConfig(
    filename='rapidrag.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log events
logging.info(f"User query: {prompt}")
logging.info(f"Document uploaded: {filename}")
```

### **Advanced: Prometheus + Grafana:**

```python
# Add metrics
from prometheus_client import Counter, Histogram

query_counter = Counter('rapidrag_queries_total', 'Total queries')
upload_counter = Counter('rapidrag_uploads_total', 'Total uploads')
query_duration = Histogram('rapidrag_query_duration_seconds', 'Query duration')

# Track metrics
query_counter.inc()
with query_duration.time():
    response = pipeline.ask(prompt)
```

---

## 🔧 Performance Optimization

### **1. Caching:**
```python
# Already implemented
@st.cache_resource
def get_rag_pipeline():
    ...
```

### **2. Resource Limits:**
```bash
# Limit Streamlit memory
streamlit run webapp.py --server.maxUploadSize=200
```

### **3. Database Optimization:**
```python
# Use persistent store for production
from haystack.document_stores.elasticsearch import ElasticsearchDocumentStore
# Instead of InMemoryDocumentStore
```

---

## 💾 Backup & Restore

### **Backup Knowledge Base:**
```bash
# Backup documents and embeddings
cp -r documents/ backup/documents-$(date +%Y%m%d)/
cp data/document_store.json backup/store-$(date +%Y%m%d).json
```

### **Automated Backup:**
```bash
# Add to crontab
0 2 * * * /path/to/backup_script.sh
```

---

## 🚨 Troubleshooting Production

### **High Memory Usage:**
```bash
# Reduce embedding batch size
# Limit concurrent users
# Use production document store (not in-memory)
```

### **Slow Response:**
```bash
# Cache embeddings
# Use GPU for inference
# Optimize retrieval (reduce top_k)
```

### **Connection Issues:**
```bash
# Check firewall
# Verify port forwarding
# Test with curl
curl http://your-ip:8501
```

---

## 📋 Deployment Checklist

**Before going to production:**

- [ ] Authentication enabled
- [ ] HTTPS/SSL configured
- [ ] Backups automated
- [ ] Monitoring in place
- [ ] Logging configured
- [ ] Rate limiting enabled (if public)
- [ ] Resource limits set
- [ ] Documentation updated
- [ ] Team trained
- [ ] Rollback plan ready
- [ ] Security audit done
- [ ] Performance tested
- [ ] Disaster recovery plan

---

## ✨ Summary

**Choose your deployment:**

| Scenario | Solution | Complexity | Cost |
|----------|----------|------------|------|
| Solo | Local | ⭐ | Free |
| Team/Office | Network mode | ⭐ | Free |
| Remote Team | VPN + Network | ⭐⭐ | Free |
| Small Production | Streamlit Cloud | ⭐⭐ | Free |
| Enterprise | AWS/Azure + Auth | ⭐⭐⭐⭐ | $$ |

**Most common:** Start with **Network mode** for teams, then move to cloud if needed!

---

*For detailed network sharing instructions, see [`docs/NETWORK_SHARING.md`](docs/NETWORK_SHARING.md)*
