# earnings_scraper.py

import requests
from bs4 import BeautifulSoup

def get_earnings_surprise(ticker: str):
    url = f"https://www.marketwatch.com/investing/stock/{ticker}/analystestimates"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch data"}

    soup = BeautifulSoup(response.text, "html.parser")
    try:
        estimates = soup.select_one("li.analyst__estimates-item span.analyst__estimates-value").text.strip()
        return {"ticker": ticker, "earnings_surprise": estimates}
    except Exception:
        return {"error": "Could not parse earnings data"}
