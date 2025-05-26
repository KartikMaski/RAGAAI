# market_data_loader.py

import yfinance as yf
import requests

ALPHA_API_KEY = "8C71EDY75M7F0UAP"  # Ideally move this to an .env file

def get_stock_data_yahoo(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="2d")

    if len(hist) < 2:
        return {"error": "Not enough historical data"}

    current_price = hist['Close'].iloc[-1]
    previous_price = hist['Close'].iloc[-2]
    change_percent = ((current_price - previous_price) / previous_price) * 100

    return {
        "ticker": ticker,
        "current_price": round(current_price, 2),
        "previous_close": round(previous_price, 2),
        "change_percent": round(change_percent, 2),
        "date": str(hist.index[-1].date())
    }

def get_stock_data_alpha(ticker: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_API_KEY}"
    response = requests.get(url).json()
    try:
        timeseries = response["Time Series (Daily)"]
        dates = sorted(timeseries.keys(), reverse=True)
        current = float(timeseries[dates[0]]['4. close'])
        previous = float(timeseries[dates[1]]['4. close'])
        change = ((current - previous) / previous) * 100
        return {
            "ticker": ticker,
            "current_price": round(current, 2),
            "previous_close": round(previous, 2),
            "change_percent": round(change, 2),
            "date": dates[0]
        }
    except Exception:
        return {"error": "Failed to retrieve AlphaVantage data"}
