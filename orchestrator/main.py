from fastapi import FastAPI, UploadFile, File
from agents.api_agent import get_stock_data
from agents.scraping_agent import get_earnings_surprise
from agents.analysis_agent import calculate_exposure
from agents.language_agent import generate_brief
from agents.retriever_agent import ingest_docs, retrieve_top_k
from agents.voice_agent import transcribe_audio, speak_text

import shutil
import os

app = FastAPI()

PORTFOLIO = {
    "TSMC": 100000,
    "SAMSUNG": 50000
}
TOTAL_AUM = 700000

sample_docs = [
    "Tech stocks in Asia often include TSMC, Samsung, Alibaba, etc.",
    "Earnings surprises occur when reported EPS differs from consensus estimates.",
    "Risk exposure in tech increases with rising yields or geopolitical tensions."
]
ingest_docs(sample_docs)

@app.get("/brief")
def get_market_brief():
    try:
        tsmc = get_stock_data("TSM")
        samsung = get_stock_data("SSNLF")

        earnings = [
            get_earnings_surprise("TSM"),
            get_earnings_surprise("SSNLF")
        ]

        exposure = calculate_exposure(PORTFOLIO, TOTAL_AUM)

        query = "risk exposure in Asia tech stocks and earnings surprises"
        chunks = retrieve_top_k(query, k=2)
        retrieved_context = " ".join([chunk["text"] for chunk in chunks])

        context = (
            f"{retrieved_context}\n"
            f"Asia Tech Exposure is {exposure['asia_exposure_percent']}% of AUM.\n"
            f"TSMC daily change: {tsmc.get('change_percent', 'N/A')}%.\n"
            f"Samsung daily change: {samsung.get('change_percent', 'N/A')}%.\n"
            f"Earnings: {earnings}"
        )

        summary = generate_brief(context)
        speak_text(summary)

        return {
            "summary": summary,
            "context_used": context,
            "raw_data": {
                "stock_data": {"TSMC": tsmc, "Samsung": samsung},
                "earnings": earnings,
                "exposure_percent": exposure
            }
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/voice-query/")
async def process_voice(file: UploadFile = File(...)):
    try:
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        transcription = transcribe_audio(temp_path)
        os.remove(temp_path)

        # Process the transcribed query through RAG + LLM
        chunks = retrieve_top_k(transcription, k=2)
        context = " ".join([chunk["text"] for chunk in chunks])
        summary = generate_brief(context)
        speak_text(summary)

        return {
            "transcription": transcription,
            "response": summary,
            "context": context
        }
    except Exception as e:
        return {"error": str(e)}

