from fastapi import FastAPI, UploadFile, HTTPException
from pdf_loader import extract_text
from vector_store import VectorStore
from rag_engine import answer_question
from models import QueryRequest
from config import TOP_K_RESULTS  # ✅ Import correct config

app = FastAPI()

# Global Vector Store Instance
store = VectorStore()

@app.get("/")
def home():
    return {"status": "PolicyGuard AI Backend Running"}

@app.post("/upload")
async def upload(file: UploadFile):
    try:
        # Extract text from PDF
        pages = extract_text(file.file)
        if not pages:
            return {"status": "error", "message": "Could not extract text or file is empty."}
            
        # Add to Vector DB
        store.add(pages)
        return {"status": "success", "indexed_pages": len(pages)}
    except Exception as e:
        print(f"Upload Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error during processing.")

@app.post("/query")
async def query(req: QueryRequest):
    try:
        # 1. Retrieve relevant docs using Configured K
        docs = store.search(req.question, k=TOP_K_RESULTS)
        
        if not docs:
            return {
                "answer": "⚠️ **No Data:** I cannot answer because no documents have been indexed yet.", 
                "sources": [], 
                "confidence": 0
            }

        context = "\n\n".join(docs)
        
        # 2. Generate Answer (Synchronous call wrapped in async endpoint)
        result = answer_question(context, req.question)
        
        return {
            "answer": result["answer"], 
            "sources": docs,
            "confidence": result["confidence"]
        }
    except Exception as e:
        print(f"Query Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))