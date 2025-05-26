# filings_loader.py

import os
from sec_edgar_downloader import Downloader

def download_latest_10k(ticker: str, save_path="./docs/filings"):
    os.makedirs(save_path, exist_ok=True)
    dl = Downloader(save_path)
    dl.get("10-K", ticker, amount=1)
    return f"10-K downloaded for {ticker}"
