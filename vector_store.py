import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

class VectorStore:
    def __init__(self):
        # 384 dimensions for all-MiniLM-L6-v2
        self.dimension = 384
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts = []

    def add(self, docs: list[str]):
        if not docs:
            return
        embeddings = self.model.encode(docs)
        self.index.add(np.array(embeddings).astype('float32'))
        self.texts.extend(docs)

    def search(self, query: str, k: int = 5):
        if not self.texts:
            return []
        
        q_emb = self.model.encode([query])
        # Search returns distances (D) and indices (I)
        D, I = self.index.search(np.array(q_emb).astype('float32'), k)
        
        results = []
        for i in I[0]:
            if i < len(self.texts) and i >= 0:
                results.append(self.texts[i])
        return results