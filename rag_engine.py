# rag_engine.py
import os
from groq import Groq
from config import GROQ_API_KEY, SYSTEM_PROMPT

# Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)

def clean_response_text(text: str) -> str:
    # ✅ FIX: Added 'r' before the quote to fix SyntaxWarning
    r"""
    Escapes dollar signs to prevent Streamlit/Markdown crashes.
    """
    if not text:
        return ""
    # Double backslash is needed to create a single literal backslash
    return text.replace("$", "\\$")

def answer_question(context: str, question: str):
    """
    Uses Groq (Llama 3.1) for extremely fast, free inference.
    """
    full_prompt = f"""{SYSTEM_PROMPT}

POLICY CONTEXT:
{context}

QUESTION:
{question}
"""

    try:
        # 🚀 CALL GROQ API
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": full_prompt}
            ],
            # ✅ UPDATED: The new standard model name
            model="llama-3.1-8b-instant", 
            temperature=0.1,
        )

        raw_answer = chat_completion.choices[0].message.content
        cleaned_answer = clean_response_text(raw_answer)
        
        return {"answer": cleaned_answer, "confidence": 95}

    except Exception as e:
        print(f"❌ Groq Error: {e}")
        return {
            "answer": f"⚠️ **AI Error:** {str(e)}", 
            "confidence": 0
        }