# Network Sharing Guide for RAPIDRAG

Complete guide to sharing RAPIDRAG with others - locally, on your network, and externally.

---

## 🌐 Three Access Modes

### **1. Local Access (Solo Use)**
- **Who:** Only you
- **URL:** `http://localhost:8501`
- **Launcher:** `start-webapp.bat`
- **Security:** Maximum (not exposed)
- **Use case:** Personal use, development

### **2. Network Access (LAN/Team)**
- **Who:** Anyone on your local network
- **URL:** `http://YOUR-LOCAL-IP:8501`
- **Launcher:** `start-webapp-network.bat`
- **Security:** Safe (firewall protected)
- **Use case:** Office, home network, team collaboration

### **3. External Access (Internet)**
- **Who:** Anyone with your public IP
- **URL:** `http://YOUR-PUBLIC-IP:8501`
- **Launcher:** `start-webapp-external.bat`
- **Security:** ⚠️ Exposed (requires caution)
- **Use case:** Remote access, public demos

---

## 🚀 Quick Start

### **Local Access (Default)**
```bash
# Option 1: Quick launcher
start-webapp.bat

# Option 2: Menu system
rag-menu.bat → Option 7

# Option 3: Manual
py -m streamlit run webapp.py
```

**Access:** `http://localhost:8501`

---

### **Network Access (Team Sharing)**
```bash
# Option 1: Quick launcher
start-webapp-network.bat

# Option 2: Menu system
rag-menu.bat → Option 8

# Option 3: Manual
py -m streamlit run webapp.py --server.address 0.0.0.0
```

**The launcher will show:**
```
Your IP Address: 192.168.1.100
Share this URL: http://192.168.1.100:8501
```

**Share that URL with your team!**

---

### **External Access (Internet)**
```bash
# Option 1: Quick launcher
start-webapp-external.bat

# Option 2: Menu system
rag-menu.bat → Option 9

# Option 3: Manual
py -m streamlit run webapp.py --server.address 0.0.0.0 --server.port 8501
```

**Requirements:**
- Port 8501 forwarded on router
- Public IP or Dynamic DNS
- Understanding of security risks

**Access:**
1. Find public IP: https://whatismyipaddress.com
2. Share: `http://YOUR-PUBLIC-IP:8501`

---

## 📋 Finding Your IP Addresses

### **Local IP (for LAN sharing)**

**Windows:**
```bash
ipconfig
# Look for "IPv4 Address": 192.168.X.X
```

**Mac/Linux:**
```bash
ifconfig
# or
ip addr show
```

### **Public IP (for external sharing)**
```bash
# Visit any of these:
https://whatismyipaddress.com
https://ifconfig.me
https://api.ipify.org
```

---

## 🔧 Port Forwarding Setup

**For external access, configure your router:**

### **Step 1: Access Router Settings**
- Open browser to `192.168.1.1` or `192.168.0.1`
- Login with admin credentials

### **Step 2: Find Port Forwarding**
- Usually under: Advanced → NAT → Port Forwarding
- Or: Security → Port Forwarding

### **Step 3: Add Rule**
```
Service Name: RAPIDRAG
External Port: 8501
Internal Port: 8501
Internal IP: YOUR-LOCAL-IP (e.g., 192.168.1.100)
Protocol: TCP
```

### **Step 4: Save and Apply**
- Save settings
- Restart router if needed
- Test access with public IP

---

## 🔒 Security Considerations

### **Local Access (Safe) ✅**
- **Exposure:** None
- **Risk:** None
- **Authentication:** Not needed
- **Recommendation:** Use for solo work

### **Network Access (Safe) ✅**
- **Exposure:** Your local network only
- **Risk:** Low (protected by firewall)
- **Authentication:** Not needed (trusted network)
- **Recommendation:** Use for office/team

### **External Access (Risky) ⚠️**
- **Exposure:** Entire internet
- **Risk:** High without protection
- **Authentication:** None built-in
- **Recommendation:** Use with caution

---

## ⚠️ External Access Risks

### **Security Concerns:**
1. **No authentication** - Anyone can access
2. **Data exposure** - Documents visible to anyone
3. **Resource abuse** - Server can be overloaded
4. **Vulnerabilities** - Potential attack surface
5. **Privacy** - Queries and uploads visible

### **Mitigation Strategies:**

#### **Option 1: VPN (Recommended)**
```bash
# Setup VPN (e.g., Tailscale, ZeroTier, WireGuard)
1. Install VPN software
2. Team connects to VPN
3. Access via VPN IP (treated as LAN)
4. Secure and encrypted
```

#### **Option 2: Reverse Proxy with Auth**
```bash
# Use Nginx/Caddy with authentication
1. Setup reverse proxy
2. Add basic auth or OAuth
3. SSL/HTTPS encryption
4. Rate limiting
```

#### **Option 3: Cloud Deployment**
```bash
# Deploy to platform with built-in auth
- Streamlit Cloud (free, built-in auth)
- AWS/Azure with IAM
- Heroku with add-ons
- Custom authentication layer
```

#### **Option 4: IP Whitelist**
```bash
# Router/Firewall: Only allow specific IPs
1. Get team member IPs
2. Configure firewall rules
3. Only allowed IPs can access
```

---

## 👥 Multi-User Behavior

### **What's Shared:**
- ✅ **Knowledge base** - All documents
- ✅ **Document store** - Vector embeddings
- ✅ **System settings** - LLM provider, models
- ✅ **File uploads** - Everyone's contributions

### **What's Separate:**
- ✅ **Chat history** - Per browser session
- ✅ **Query count** - Per session
- ✅ **Session state** - Independent sessions

### **Concurrent Access:**
- Multiple users can chat simultaneously
- Uploads affect everyone's knowledge base
- Analytics show aggregate statistics
- No user management (all anonymous)

---

## 🎯 Use Case Scenarios

### **Scenario 1: Solo Developer**
```bash
start-webapp.bat
# Local only, maximum security
```

### **Scenario 2: Office Team (Same Building)**
```bash
start-webapp-network.bat

Share: http://192.168.1.100:8501
Team accesses from their desks
Safe behind office firewall
```

### **Scenario 3: Remote Team**
```bash
# Option A: VPN (Best)
Setup VPN → Team connects → Access like LAN

# Option B: Cloud Deploy
Deploy to Streamlit Cloud → Share cloud URL

# Option C: External (If needed)
start-webapp-external.bat → Share public IP
⚠️ Use with caution!
```

### **Scenario 4: Client Demo**
```bash
# Option A: Screen sharing (Safest)
Run local, share screen in Zoom/Teams

# Option B: Temporary external access
start-webapp-external.bat
Demo session only
Close after demo
```

---

## 📊 Network Comparison

| Feature | Local | Network | External |
|---------|-------|---------|----------|
| **Access** | You only | LAN users | Anyone |
| **Setup** | None | None | Port forward |
| **Security** | Maximum | High | ⚠️ Low |
| **Speed** | Fastest | Fast | Depends |
| **Firewall** | Protected | Protected | ⚠️ Exposed |
| **Auth needed** | No | No | ⚠️ Yes (recommended) |
| **Cost** | Free | Free | Free |
| **Best for** | Solo | Team/Office | Remote (with VPN) |

---

## 🛠️ Troubleshooting

### **Can't Access on Network**

**Check firewall:**
```bash
# Windows: Allow Python through firewall
1. Windows Security → Firewall
2. Allow an app → Python
3. Check both Private and Public
```

**Check IP:**
```bash
# Ensure you're using correct IP
ipconfig
# Share the IPv4 address shown
```

**Check port:**
```bash
# Ensure Streamlit is running
netstat -an | findstr 8501
# Should show LISTENING
```

### **External Access Not Working**

**Verify port forwarding:**
```bash
# Test from external network
# Use mobile data or ask friend to try
http://YOUR-PUBLIC-IP:8501
```

**Check router:**
- Port 8501 forwarded correctly
- To correct internal IP
- Not blocked by ISP

**Check firewall:**
- Router firewall allows 8501
- Windows firewall allows Python
- No additional security software blocking

---

## 💡 Best Practices

### **For Network Sharing:**
1. ✅ Use descriptive hostnames
2. ✅ Document the URL for team
3. ✅ Keep system running during work hours
4. ✅ Backup knowledge base regularly
5. ✅ Monitor uploads and usage

### **For External Access:**
1. ⚠️ Only enable when needed
2. ⚠️ Use VPN if possible
3. ⚠️ Monitor access logs
4. ⚠️ Limit who has the URL
5. ⚠️ Consider adding authentication
6. ⚠️ Use HTTPS if public
7. ⚠️ Regular security audits

---

## 🔐 Adding Authentication (Advanced)

### **Option 1: Streamlit Auth Component**
```python
# Install streamlit-authenticator
pip install streamlit-authenticator

# Add to webapp.py
import streamlit_authenticator as stauth

# Configure authentication
authenticator = stauth.Authenticate(...)
name, authentication_status, username = authenticator.login()

if authentication_status:
    # Show RAPIDRAG interface
    main()
else:
    st.error("Please login")
```

### **Option 2: Reverse Proxy (Nginx)**
```nginx
# nginx.conf
server {
    listen 80;
    
    location / {
        auth_basic "RAPIDRAG Access";
        auth_basic_user_file /etc/nginx/.htpasswd;
        proxy_pass http://localhost:8501;
    }
}
```

### **Option 3: Cloud Platform Auth**
- Streamlit Cloud: Built-in OAuth
- AWS: IAM authentication
- Azure: Active Directory
- Heroku: Add-on authentication

---

## 📈 Monitoring Usage

### **Check Active Connections**
```bash
# Windows
netstat -an | findstr 8501

# Shows connected clients
```

### **View Streamlit Stats**
- Browser: Check network tab
- Logs: Streamlit terminal output
- Files: Monitor `data/document_store.json` changes

---

## 🚀 Quick Reference

```bash
# Local (you only)
start-webapp.bat
→ http://localhost:8501

# Network (team on LAN)
start-webapp-network.bat
→ http://192.168.X.X:8501

# External (internet)
start-webapp-external.bat
→ http://YOUR-PUBLIC-IP:8501
⚠️ Requires port forwarding
⚠️ Security risks

# Via menu system
rag-menu.bat
→ Option 7: Local
→ Option 8: Network
→ Option 9: External
```

---

## ✨ Summary

**RAPIDRAG supports three access modes:**

1. **Local** - Solo use, maximum security
2. **Network** - Team sharing, safe and easy
3. **External** - Internet access, use with caution

**Each has its place. Choose based on your needs!**

**For most teams:** Use **Network** mode for safe, easy collaboration!

---

*For security best practices and advanced configurations, consult your IT department or security team.*
