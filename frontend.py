import streamlit as st
import requests

# --- PAGE CONFIGURATION ---
# ✅ UPDATED: Added initial_sidebar_state="expanded" to force the sidebar open
st.set_page_config(
    page_title="PolicyGuard AI", 
    page_icon="🛡️", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
    <style>
    .main {background-color: #f9f9f9;}
    .stButton>button {width: 100%;}
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ PolicyGuard AI")
st.markdown("### Enterprise Compliance & Intelligence Agent")

# Define Backend URL
BACKEND_URL = "https://policyguard.onrender.com"

# Initialize Session State
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# Sidebar
with st.sidebar:
    st.header("📂 Policy Ingestion")
    uploaded_file = st.file_uploader("Upload Policy PDF", type="pdf")
    
    if uploaded_file:
        if st.button("🚀 Index Document"):
            with st.spinner("Processing & Vectorizing..."):
                files = {"file": ("policy.pdf", uploaded_file.getvalue(), "application/pdf")}
                try:
                    res = requests.post(f"{BACKEND_URL}/upload", files=files)
                    if res.status_code == 200:
                        st.success(f"✅ Indexed {res.json().get('indexed_pages')} pages!")
                    else:
                        st.error(f"❌ Indexing Failed: {res.text}")
                except Exception as e:
                    st.error(f"Server Connection Error: {e}")
    
    st.divider()
    st.info("💡 **Tip:** Ask specific questions like 'What is the limit for travel expenses?'")

# Main Chat Area
question = st.text_input("🔍 **Query the Policy:**", placeholder="Type your compliance question here...")

if st.button("Analyze Policy"):
    if not question:
        st.warning("⚠️ Please type a question.")
    else:
        st.session_state.analysis_result = None # Clear previous
        with st.spinner("🧠 Analyzing Policy Context..."):
            try:
                payload = {"question": question}
                res = requests.post(f"{BACKEND_URL}/query", json=payload)
                
                if res.status_code == 200:
                    st.session_state.analysis_result = res.json()
                else:
                    st.error(f"⚠️ Error {res.status_code}: {res.text}")
            except Exception as e:
                st.error(f"🔌 Connection Error: {e}")

# Display Results
if st.session_state.analysis_result:
    data = st.session_state.analysis_result
    
    # Layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 🏛️ Analysis Result")
        # Now safe to use Markdown because we escaped $ in backend
        st.markdown(data["answer"])
    
    with col2:
        st.markdown("### 📊 Metrics")
        score = data.get("confidence", 0)
        
        if score > 80:
            st.success(f"High Confidence: {score}%")
        elif score > 50:
            st.warning(f"Medium Confidence: {score}%")
        else:
            st.error(f"Low Confidence: {score}%")
            
    with st.expander("🔍 **View Source Evidence** (RAG Context)"):
        for i, src in enumerate(data.get("sources", [])):
            st.markdown(f"**📄 Excerpt {i+1}:**")
            st.caption(src[:500] + "...") # Show first 500 chars
            st.divider()