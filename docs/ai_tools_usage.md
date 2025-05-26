# AI Tool Usage Log

This document tracks the usage of AI tools (e.g., ChatGPT, GitHub Copilot) throughout the development of the **Finance Assistant Agent System**.

---

## 📌 Summary

| Tool Used        | Purpose                                      | Modules Affected                    |
|------------------|----------------------------------------------|-------------------------------------|
| ChatGPT (GPT-4)  | Prompt-based code scaffolding, debugging     | agents/, data_ingestion/, streamlit_app/ |
| GitHub Copilot   | Code autocompletion, boilerplate suggestions | voice/, orchestrator/, README.md    |
| LangChain        | Retrieval QA, LLM interface                  | language_agent.py                   |
| HuggingFace      | Transformers + pipelines                     | language_agent.py, retriever_agent.py |
| FAISS            | Vector store for RAG                         | retriever_agent.py                  |
