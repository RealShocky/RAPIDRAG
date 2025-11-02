"""
Futuristic RAG Chatbot Web Interface
Beautiful space-themed Streamlit dashboard with animations
"""

import streamlit as st
import time
from pathlib import Path
from datetime import datetime
import json
from typing import List
import plotly.graph_objects as go
from rag_pipeline import SimpleRAGPipeline
from config import Config
import os

# Page configuration
st.set_page_config(
    page_title="RAPIDRAG - Lightning Fast AI Knowledge Base",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for futuristic space theme
def load_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap');
    
    /* Animated space background */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1a3e 25%, #0f0c29 50%, #302b63 75%, #24243e 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Starfield effect */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #eee, transparent),
            radial-gradient(2px 2px at 60px 70px, #fff, transparent),
            radial-gradient(1px 1px at 50px 50px, #ddd, transparent),
            radial-gradient(1px 1px at 130px 80px, #fff, transparent),
            radial-gradient(2px 2px at 90px 10px, #eee, transparent);
        background-size: 200px 200px;
        background-repeat: repeat;
        opacity: 0.3;
        animation: twinkle 3s ease-in-out infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.6; }
    }
    
    /* Main content */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        position: relative;
        z-index: 1;
    }
    
    /* Headers with glow effect */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00d4ff !important;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5),
                     0 0 20px rgba(0, 212, 255, 0.3),
                     0 0 30px rgba(0, 212, 255, 0.2);
        letter-spacing: 2px;
    }
    
    h1 {
        font-size: 3rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    /* Sidebar styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10, 14, 39, 0.95) 0%, rgba(26, 26, 62, 0.95) 100%);
        border-right: 2px solid rgba(0, 212, 255, 0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Cards with glass effect */
    .stMarkdown, .stTextInput, .stTextArea, .stSelectbox {
        font-family: 'Rajdhani', sans-serif;
    }
    
    div[data-testid="stMetricValue"] {
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        color: #00d4ff;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }
    
    /* Buttons with neon effect */
    .stButton > button {
        font-family: 'Orbitron', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: 2px solid #00d4ff;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.6),
                    0 0 60px rgba(0, 212, 255, 0.4);
        transform: translateY(-2px);
        border-color: #fff;
    }
    
    /* Chat messages */
    .stChatMessage {
        background: rgba(26, 26, 62, 0.6);
        border-radius: 15px;
        border: 1px solid rgba(0, 212, 255, 0.2);
        backdrop-filter: blur(10px);
        margin: 1rem 0;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* File uploader */
    .stFileUploader {
        border: 2px dashed #00d4ff;
        border-radius: 15px;
        background: rgba(0, 212, 255, 0.05);
        padding: 2rem;
    }
    
    /* Success/Info messages */
    .stSuccess, .stInfo {
        background: rgba(0, 212, 255, 0.1);
        border-left: 4px solid #00d4ff;
        border-radius: 10px;
    }
    
    /* Progress bars */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #00d4ff 100%);
        border-radius: 10px;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        font-family: 'Orbitron', sans-serif;
        color: #00d4ff;
        background: rgba(26, 26, 62, 0.6);
        border-radius: 10px;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Orbitron', sans-serif;
        background: rgba(26, 26, 62, 0.6);
        border-radius: 10px 10px 0 0;
        color: #00d4ff;
        border: 1px solid rgba(0, 212, 255, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(10, 14, 39, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #00d4ff 0%, #667eea 100%);
    }
    
    /* Floating particles animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    /* Glow effect on focus */
    input:focus, textarea:focus {
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.5) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'rag_pipeline' not in st.session_state:
        st.session_state.rag_pipeline = None
    if 'system_initialized' not in st.session_state:
        st.session_state.system_initialized = False
    if 'total_documents' not in st.session_state:
        st.session_state.total_documents = 0
    if 'total_queries' not in st.session_state:
        st.session_state.total_queries = 0

# Initialize RAG pipeline
@st.cache_resource
def get_rag_pipeline():
    """Initialize and cache the RAG pipeline"""
    try:
        rag = SimpleRAGPipeline()
        rag.initialize()
        return rag
    except Exception as e:
        st.error(f"Failed to initialize RAG system: {e}")
        return None

# Create animated metric cards
def animated_metric(label, value, icon="🌟"):
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
        border: 2px solid rgba(0, 212, 255, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
        backdrop-filter: blur(10px);
    ">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">{icon}</div>
        <div style="
            font-family: 'Orbitron', sans-serif;
            font-size: 2.5rem;
            color: #00d4ff;
            text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
            font-weight: bold;
        ">{value}</div>
        <div style="
            font-family: 'Rajdhani', sans-serif;
            font-size: 1rem;
            color: #a0a0ff;
            text-transform: uppercase;
            letter-spacing: 2px;
        ">{label}</div>
    </div>
    """, unsafe_allow_html=True)

# Main app
def main():
    load_css()
    init_session_state()
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
        <h1 style='text-align: center; margin-bottom: 2rem;'>
            ⚡ RAPIDRAG
        </h1>
        <p style='text-align: center; font-size: 1.1rem; color: #a0a0ff; margin-top: -1rem;'>
            Lightning Fast AI Knowledge Base
        </p>
        """, unsafe_allow_html=True)
        
        # System status
        st.markdown("### 🔮 System Status")
        
        # Initialize pipeline if not done
        if not st.session_state.system_initialized:
            with st.spinner("🚀 Initializing RAPIDRAG..."):
                st.session_state.rag_pipeline = get_rag_pipeline()
                if st.session_state.rag_pipeline:
                    st.session_state.system_initialized = True
                    # Get document count
                    try:
                        docs_path = Path("data/document_store.json")
                        if docs_path.exists():
                            with open(docs_path) as f:
                                data = json.load(f)
                                st.session_state.total_documents = len(data)
                    except:
                        st.session_state.total_documents = 0
        
        if st.session_state.system_initialized:
            st.success("✅ System Online")
            st.info(f"🤖 LLM: {Config.LLM_PROVIDER.upper()}")
            st.info(f"📚 Documents: {st.session_state.total_documents}")
            st.info(f"💬 Queries: {st.session_state.total_queries}")
        else:
            st.error("❌ System Offline")
        
        st.markdown("---")
        
        # Navigation
        st.markdown("### 🎛️ Navigation")
        page = st.radio(
            "Select Module",
            ["💬 Chat", "📤 Upload Documents", "⚙️ Settings", "📊 Analytics"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Quick actions
        st.markdown("### ⚡ Quick Actions")
        if st.button("🔄 Refresh System", use_container_width=True):
            st.cache_resource.clear()
            st.session_state.system_initialized = False
            st.rerun()
        
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
        
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; color: #666; font-size: 0.8rem; margin-top: 2rem;'>
            ⚡ RAPIDRAG v1.0.0<br/>
            Your Enterprise AI Solution
        </div>
        """, unsafe_allow_html=True)
    
    # Main content based on page selection
    if page == "💬 Chat":
        show_chat_page()
    elif page == "📤 Upload Documents":
        show_upload_page()
    elif page == "⚙️ Settings":
        show_settings_page()
    elif page == "📊 Analytics":
        show_analytics_page()

def show_chat_page():
    """Main chat interface"""
    # Header with animation
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='font-size: 4rem; margin-bottom: 0;'>
            ⚡ RAPIDRAG
        </h1>
        <p style='
            font-family: "Rajdhani", sans-serif;
            font-size: 1.2rem;
            color: #a0a0ff;
            letter-spacing: 3px;
        '>
            Lightning Fast AI-Powered Knowledge Base
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        animated_metric("Documents", st.session_state.total_documents, "📚")
    with col2:
        animated_metric("Queries", st.session_state.total_queries, "💬")
    with col3:
        animated_metric("Provider", Config.LLM_PROVIDER.upper()[:4], "🤖")
    with col4:
        animated_metric("Status", "ONLINE" if st.session_state.system_initialized else "OFFLINE", "🟢" if st.session_state.system_initialized else "🔴")
    
    st.markdown("<br/>", unsafe_allow_html=True)
    
    # Chat container
    chat_container = st.container()
    
    # Display chat history
    with chat_container:
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"], avatar="🌟" if message["role"] == "assistant" else "👤"):
                st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("⚡ Ask anything from your knowledge base..."):
        if not st.session_state.system_initialized:
            st.error("❌ System not initialized. Please refresh the system from the sidebar.")
            return
        
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant", avatar="🌟"):
            with st.spinner("⚡ Searching knowledge base..."):
                try:
                    response = st.session_state.rag_pipeline.ask(prompt)
                    st.markdown(response)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    st.session_state.total_queries += 1
                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.chat_history.append({"role": "assistant", "content": error_msg})

def show_upload_page():
    """Document upload interface"""
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1>📤 UPLOAD TO KNOWLEDGE BASE</h1>
        <p style='
            font-family: "Rajdhani", sans-serif;
            font-size: 1.2rem;
            color: #a0a0ff;
        '>
            Expand your knowledge base instantly
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # File upload
    uploaded_files = st.file_uploader(
        "Upload Documents",
        type=['txt', 'md', 'pdf', 'docx', 'html', 'json'],
        accept_multiple_files=True,
        help="Supported formats: TXT, MD, PDF, DOCX, HTML, JSON"
    )
    
    if uploaded_files:
        st.success(f"✨ {len(uploaded_files)} file(s) selected")
        
        # Show file details
        with st.expander("📋 View Files"):
            for file in uploaded_files:
                st.write(f"• {file.name} ({file.size/1024:.2f} KB)")
        
        # Upload button
        if st.button("🚀 Upload & Process", use_container_width=True):
            # Create containers for better visibility
            progress_container = st.container()
            status_container = st.container()
            
            with progress_container:
                progress_bar = st.progress(0, text="Starting upload...")
            
            with status_container:
                status_text = st.empty()
            
            # Save files
            documents_dir = Path("documents")
            documents_dir.mkdir(exist_ok=True)
            
            for i, file in enumerate(uploaded_files):
                with status_container:
                    status_text.info(f"📥 Uploading {file.name}...")
                
                # Save file
                file_path = documents_dir / file.name
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                
                # Update progress
                progress_pct = int(((i + 1) / len(uploaded_files)) * 50)  # First 50%
                with progress_container:
                    progress_bar.progress(progress_pct, text=f"Uploaded {i+1}/{len(uploaded_files)} files...")
                
                time.sleep(0.1)  # Small delay to show progress
            
            with status_container:
                status_text.warning("✨ Processing documents with AI...")
            
            # Processing phase
            with progress_container:
                progress_bar.progress(60, text="Running document ingestion...")
            
            # Run ingestion
            try:
                import subprocess
                result = subprocess.run(
                    ["py", "ingest_documents.py"],
                    capture_output=True,
                    text=True
                )
                
                with progress_container:
                    progress_bar.progress(90, text="Finalizing...")
                
                if result.returncode == 0:
                    with progress_container:
                        progress_bar.progress(100, text="Complete!")
                    
                    with status_container:
                        status_text.empty()
                        st.success("🎉 Documents successfully added to knowledge base!")
                    
                    # Show balloons
                    st.balloons()
                    
                    # Update document count
                    try:
                        docs_path = Path("data/document_store.json")
                        if docs_path.exists():
                            with open(docs_path) as f:
                                data = json.load(f)
                                st.session_state.total_documents = len(data)
                                st.info(f"📊 Total documents in knowledge base: {len(data)}")
                    except:
                        pass
                    
                    # Refresh pipeline
                    st.cache_resource.clear()
                    st.session_state.system_initialized = False
                    
                    st.warning("🔄 Refreshing system... Please wait 3 seconds...")
                    time.sleep(3)
                    st.rerun()
                else:
                    st.error(f"❌ Error processing documents: {result.stderr}")
            except Exception as e:
                st.error(f"❌ Error: {e}")
    
    # Current documents
    st.markdown("---")
    st.markdown("### 📚 Current Knowledge Base")
    
    docs_path = Path("data/document_store.json")
    if docs_path.exists():
        try:
            with open(docs_path) as f:
                data = json.load(f)
                
            if data:
                st.info(f"📊 Total documents: {len(data)}")
                
                with st.expander("View Document List"):
                    for i, doc in enumerate(data[:10], 1):  # Show first 10
                        filename = doc.get('meta', {}).get('filename', 'Unknown')
                        file_type = doc.get('meta', {}).get('file_type', 'unknown')
                        st.write(f"{i}. **{filename}** ({file_type})")
                    
                    if len(data) > 10:
                        st.write(f"... and {len(data) - 10} more documents")
            else:
                st.warning("No documents in knowledge base yet.")
        except:
            st.error("Error reading knowledge base.")
    else:
        st.warning("📭 Knowledge base is empty. Upload documents to get started!")

def show_settings_page():
    """Settings interface"""
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1>⚙️ SYSTEM CONFIGURATION</h1>
        <p style='
            font-family: "Rajdhani", sans-serif;
            font-size: 1.2rem;
            color: #a0a0ff;
        '>
            Configure your RAPIDRAG system
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # LLM Provider
    st.markdown("### 🤖 LLM Provider")
    current_provider = Config.LLM_PROVIDER
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Current Provider:** {current_provider.upper()}")
    with col2:
        if st.button("🔄 Switch Provider"):
            st.info("Use `python switch_provider.py` from terminal to switch")
    
    # Model settings
    st.markdown("### 🎯 Model Settings")
    st.text_input("Embedding Model", value=Config.EMBEDDING_MODEL, disabled=True)
    st.number_input("Top K Retrieval", value=Config.TOP_K_RETRIEVAL, min_value=1, max_value=10, disabled=True)
    
    # System info
    st.markdown("### 📊 System Information")
    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.metric("Python Version", "3.x")
        st.metric("Haystack Version", "2.x")
    with info_col2:
        st.metric("Documents Directory", "documents/")
        st.metric("Data Directory", "data/")

def show_analytics_page():
    """Analytics dashboard"""
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1>📊 RAPIDRAG ANALYTICS</h1>
        <p style='
            font-family: "Rajdhani", sans-serif;
            font-size: 1.2rem;
            color: #a0a0ff;
        '>
            Real-time insights and performance metrics
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        animated_metric("Total Documents", st.session_state.total_documents, "📚")
    with col2:
        animated_metric("Total Queries", st.session_state.total_queries, "💬")
    with col3:
        animated_metric("Active Sessions", 1, "🌟")
    
    st.markdown("<br/>", unsafe_allow_html=True)
    
    # Charts
    st.markdown("### 📈 Activity Over Time")
    
    # Create a simple visualization
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[st.session_state.total_queries // 5 * i for i in range(1, 6)],
        mode='lines+markers',
        line=dict(color='#00d4ff', width=3),
        marker=dict(size=10, color='#7b2cbf'),
        fill='tonexty',
        fillcolor='rgba(0, 212, 255, 0.1)'
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#00d4ff', family='Rajdhani'),
        xaxis=dict(showgrid=False, title="Time"),
        yaxis=dict(showgrid=True, gridcolor='rgba(0, 212, 255, 0.1)', title="Queries"),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Document types
    st.markdown("### 📁 Document Types Distribution")
    
    docs_path = Path("data/document_store.json")
    if docs_path.exists():
        try:
            with open(docs_path) as f:
                data = json.load(f)
            
            # Count file types
            file_types = {}
            for doc in data:
                file_type = doc.get('meta', {}).get('file_type', 'unknown')
                file_types[file_type] = file_types.get(file_type, 0) + 1
            
            if file_types:
                fig = go.Figure(data=[go.Pie(
                    labels=list(file_types.keys()),
                    values=list(file_types.values()),
                    hole=.4,
                    marker=dict(colors=['#667eea', '#764ba2', '#00d4ff', '#7b2cbf', '#a0a0ff'])
                )])
                
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#00d4ff', family='Orbitron'),
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
        except:
            st.warning("No analytics data available yet.")
    else:
        st.warning("No documents to analyze.")

if __name__ == "__main__":
    main()
