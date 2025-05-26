# === language_agent.py ===
from transformers import pipeline
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

generator = pipeline("text-generation", model="distilgpt2", max_new_tokens=100)
llm = HuggingFacePipeline(pipeline=generator)

def generate_brief(context: str):
    prompt = f"Generate a market summary for the following context:\n\n{context}\n\nSummary:"
    result = generator(prompt)[0]['generated_text']
    return result.split("Summary:")[-1].strip()

retrieval_qa = None

def init_retrieval_qa(docs: list):
    global retrieval_qa
    embeddings = HuggingFaceEmbeddings()
    faiss_store = FAISS.from_texts(docs, embeddings)
    retrieval_qa = RetrievalQA.from_chain_type(llm=llm, retriever=faiss_store.as_retriever())

def generate_rag_response(query: str):
    if retrieval_qa is None:
        return "Retriever not initialized."
    return retrieval_qa.run(query)
