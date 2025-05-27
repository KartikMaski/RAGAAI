# RAGAAI

# 📈 Finance Assistant – Multi-Agent Market Brief Generator

A modular, multi-agent financial assistant capable of ingesting real-time data, analyzing market movements, performing document retrieval, generating natural language summaries, and interacting through voice. Built using **FastAPI**, **LangChain**, **HuggingFace**, **Whisper**, and **Streamlit**.

---

## 🧠 Key Features

- **Data Ingestion Agents**: Scrape earnings and pull stock data from Yahoo Finance and Alpha Vantage.
- **Retriever Agent**: Embed and search relevant market documents using FAISS and Sentence Transformers.
- **Language Agent**: Generate market briefs using DistilGPT2 with RAG integration.
- **Analysis Agent**: Analyze exposure and identify portfolio risks.
- **Voice Agent**: Use Whisper for speech-to-text and gTTS for text-to-speech.
- **Frontend**: Simple Streamlit UI to query and listen to market summaries.
- **Orchestrator**: FastAPI-based service to coordinate multi-agent tasks.

---



## Architecture

                        +------------------+
                        |   Streamlit App  |
                        |   (app.py)       |
                        +--------+---------+
                                 |
                                 v (HTTP)
                  +--------------+--------------+
                  |      FastAPI Orchestrator   | ←─── Main microservice interface
                  |        (main.py)            |
                  +--------------+--------------+
                                 |
       +-------------------------+--------------------------+
       |                         |                          |
       v                         v                          v
+--------------+      +--------------------+      +------------------+
| API Agent    |      | Scraping Agent     |      | Analysis Agent   |
| (api_agent)  |      | (scraping_agent)   |      | (analysis_agent) |
+------+-------+      +----------+---------+      +--------+---------+
       |                         |                         |
       v                         v                         v
+---------------+       +--------------------+     +-----------------------+
| Yahoo Finance |       | MarketWatch        |     | Business Logic:       |
| AlphaVantage  |       | SEC Edgar          |     | - Exposure %          |
+---------------+       +--------------------+     | - Risk movements      |
                                                   +-----------------------+

       +--------------------------------------------------+
       |                                                  |
       v                                                  v
+---------------------+                          +------------------------+
| Retriever Agent     | ←── Ingests & Indexes    | Language Agent         |
| (retriever_agent)   |     domain knowledge     | (language_agent)       |
| (FAISS + SBERT)     |                          | (DistilGPT2 + RAG)     |
+---------------------+                          +------------------------+
        ^                                                       |
        |                                                       v
        |                                             +----------------------+
        +------------- Retrieval -------------------> | Text Generation /   |
                                                      | RAG Q&A System      |
                                                      +----------------------+

       +-------------------------+
       | Voice Agent            |
       | (voice_agent.py)       |
       +-----------+------------+
                   | 
         +---------v---------+
         | Whisper ASR       | ←── Audio Transcription
         | gTTS              | ←── Audio Playback
         +-------------------+
