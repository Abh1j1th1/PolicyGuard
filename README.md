# 🛡️ PolicyGuard AI
### Enterprise Compliance & Audit Engine powered by RAG

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://policyguard.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![API](https://img.shields.io/badge/API-FastAPI-green.svg)](https://fastapi.tiangolo.com/)
[![LLM](https://img.shields.io/badge/AI-Llama3.1-purple.svg)](https://groq.com/)

---

## ⚠️ Important Note for Judges (Please Read First)

**This application is deployed on free-tier cloud infrastructure.**
* **Backend:** Hosted on Render (Free Tier).
* **Frontend:** Hosted on Streamlit Community Cloud.

**🛑 The "Cold Start" Delay:**
Render's free tier puts the server to "sleep" after 15 minutes of inactivity. When you first open the app or upload a document, **please allow 50-60 seconds** for the server to wake up. Subsequent requests will be instant!

---

## 🚀 Live Demo
**Click here to try the app:** 👉 **[https://policyguard.streamlit.app](https://policyguard.streamlit.app)** *(If the link doesn't load immediately, please refresh after 1 minute.)*

---

## 💡 The Problem
Corporate policy documents are often hundreds of pages long. Employees rarely read them, leading to:
* **Compliance Violations:** Accidental security breaches or expense fraud.
* **HR Overload:** Teams wasting hours answering repetitive questions like *"What is the travel allowance?"*
* **Information Silos:** Critical rules buried in PDF attachments nobody opens.

## 🛠️ The Solution
**PolicyGuard AI** is an intelligent forensic audit engine. It doesn't just "chat" with documents; it enforces them.
1.  **Ingest:** Upload any PDF policy (HR, Travel, IT Security).
2.  **Index:** The system creates a vector database of the rules.
3.  **Audit:** Ask complex scenario-based questions.
4.  **Verdict:** Receive a legally-grounded answer with **VERIFIED** citations.

---

## ✨ Key Features
* **RAG Architecture:** Retrieval-Augmented Generation ensures answers are strictly grounded in the uploaded text.
* **"Four Walls" Doctrine:** The AI is engineered to ignore outside knowledge and answer *only* based on your company's policy to prevent hallucinations.
* **Citation Engine:** Every claim includes a direct reference to the source text (e.g., `[Page 12, Section 4.1]`).
* **Conflict Detection:** Identifies ambiguous or contradictory rules within the document.

---

## ⚙️ Tech Stack
* **Frontend:** Streamlit (Python)
* **Backend:** FastAPI
* **AI Engine:** Groq API (Llama 3.1 8B Instant)
* **Vector Database:** FAISS (Facebook AI Similarity Search)
* **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
* **Deployment:** Render (API) + Streamlit Cloud (UI)

---

## 🏃‍♂️ Running Locally
If you prefer to run the code on your own machine:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Abh1j1th/PolicyGuard.git](https://github.com/Abh1j1th/PolicyGuard.git)
    cd PolicyGuard
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up Environment Variables**
    Create a `.env` file in the root directory and add your Groq API key:
    ```env
    GROQ_API_KEY=gsk_your_actual_key_here
    ```

4.  **Run the Backend**
    ```bash
    python -m uvicorn main:app --reload
    ```

5.  **Run the Frontend** (In a new terminal)
    ```bash
    python -m streamlit run frontend.py
    ```

---

## 🔮 Future Roadmap
* [ ] **Multi-Document Support:** Compare conflicting policies across different departments.
* [ ] **Admin Dashboard:** Analytics on what policies employees are asking about most.
* [ ] **Slack Integration:** A bot that answers policy questions directly in team chat.
---
*Built with ❤️ for DevFest 5.0 Hackathon 2026*
