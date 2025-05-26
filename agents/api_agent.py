# api_agent.py

from data_ingestion.market_data_loader import get_stock_data_yahoo, get_stock_data_alpha

def get_stock_data(ticker: str):
    return get_stock_data_yahoo(ticker)

def get_stock_data_from_alpha(ticker: str):
    return get_stock_data_alpha(ticker)
