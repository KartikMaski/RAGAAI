# === retriever_agent.py ===
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)
documents = []
doc_sources = []

def ingest_docs(docs: list, sources: list = None):
    global documents, doc_sources
    embeddings = model.encode(docs)
    index.add(np.array(embeddings).astype('float32'))
    documents = docs.copy()
    doc_sources = sources.copy() if sources else ["source_unknown"] * len(docs)

def retrieve_top_k(query: str, k=3):
    query_vec = model.encode([query]).astype('float32')
    D, I = index.search(query_vec, k)
    return [{"text": documents[i], "source": doc_sources[i]} for i in I[0] if i < len(documents)]
