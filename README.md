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



## 📐 System Architecture

```plaintext
                        +------------------+
                        |   Streamlit App  |
                        |   (app.py)       |
                        +--------+---------+
                                 |
                                 v (HTTP)
                  +--------------+--------------+
                  |      FastAPI Orchestrator   |
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
```

## 🔧 Components Breakdown

---

## 🧠 Agents

| Agent           | Functionality                                                                                 |
|-----------------|----------------------------------------------------------------------------------------------|
| **api_agent**       | Fetches stock market data using Yahoo Finance and AlphaVantage APIs.                        |
| **scraping_agent**  | Extracts earnings surprise data from MarketWatch and 10-K filings from SEC.                 |
| **analysis_agent**  | Analyzes exposure to markets and detects high-risk movements.                              |
| **retriever_agent** | Uses SBERT + FAISS to create a vector DB for domain knowledge retrieval.                    |
| **language_agent**  | Generates natural language briefs using DistilGPT2; integrates with FAISS for Retrieval-Augmented Generation (RAG). |
| **voice_agent**     | Handles speech-to-text (Whisper) and text-to-speech (gTTS).                                |

---

## 🚀 Orchestration

### `orchestrator/main.py`

- FastAPI routes integrate all agents.

- **`/brief` route:**

  - Fetches stock & earnings data.  
  - Analyzes exposure.  
  - Retrieves context using FAISS.  
  - Generates a market brief using DistilGPT2.  
  - Speaks the summary aloud.

- **`/voice-query/` route:**

  - Transcribes voice input using Whisper.  
  - Passes query to retrieval/generation pipeline.

---

## 🎨 Frontend

### `streamlit_app/app.py`

- Simple interface to trigger voice input or request summaries.  
- Displays data and visual feedback to users.

---

## 📦 Tools & Libraries

| Component     | Tool / Library                                 |
|---------------|-----------------------------------------------|
| Web API       | FastAPI                                       |
| Frontend      | Streamlit                                     |
| ML Inference  | HuggingFace Transformers (DistilGPT2, Whisper)|
| Vector Search | FAISS                                         |
| Embeddings    | Sentence-BERT, HuggingFace                     |
| Scraping      | BeautifulSoup, SEC-Edgar                       |
| TTS           | gTTS                                          |
| STT           | OpenAI Whisper                                |
| Data APIs     | yfinance, AlphaVantage                         |

---

## 📈 Performance Benchmarks (Sample Guidance)

| Task                       | Avg Latency | Comment                       |
|----------------------------|-------------|-------------------------------|
| Stock data fetch (Yahoo)   | ~200ms      | Depends on ticker volume       |
| Earnings scraping (MarketWatch) | ~500-800ms | Subject to page structure      |
| RAG + GPT2 generation      | ~1-2s       | May vary with model size       |
| Whisper STT (5s audio)     | ~4-6s       | Depends on local hardware      |
| FAISS retrieval (3 docs)   | <100ms      | Scales with vector DB size     |

---


## 📊 Framework/Toolkit Comparison

| Feature         | FAISS + SBERT                         | LangChain + HuggingFace                 |
|-----------------|----------------------------------------|------------------------------------------|
| **Use Case**     | Vector Search                          | RAG, QA, Text Generation                 |
| **Pros**         | Fast, scalable                         | Pre-built pipelines, flexible            |
| **Cons**         | Manual doc linking                     | Higher memory usage                      |
| **Use in Project** | Retriever Agent                       | Language Agent (RAG with GPT2)           |

---

| Feature         | Whisper STT                            | gTTS TTS                                 |
|-----------------|----------------------------------------|------------------------------------------|
| **Use Case**     | Audio transcription                    | Audio generation (speech output)         |
| **Pros**         | High accuracy                          | Lightweight                              |
| **Cons**         | Slow on CPU                            | Robotic tone                             |
| **Use in Project** | Voice Agent                           | Voice Agent                              |

