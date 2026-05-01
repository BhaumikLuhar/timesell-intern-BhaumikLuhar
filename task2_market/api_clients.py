import yfinance as yf
import requests
from datetime import datetime


def fetch_stock_price(symbol: str):
    """
    Fetch stock/index price using yfinance
    """
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")

        if data.empty:
            raise ValueError("No data returned")

        price = float(data["Close"].iloc[-1])

        return {
            "asset": symbol,
            "price": price,
            "currency": "INR",  # assume INR for NIFTY etc.
            "timestamp": datetime.now()
        }

    except Exception as e:
        raise RuntimeError(f"Stock fetch failed for {symbol}: {e}")


def fetch_crypto_price(coin_id: str):
    """
    Fetch crypto price using CoinGecko
    """
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

        response = requests.get(url, timeout=5)
        data = response.json()

        if coin_id not in data:
            raise ValueError("Invalid response")

        price = data[coin_id]["usd"]

        return {
            "asset": coin_id.upper(),
            "price": price,
            "currency": "USD",
            "timestamp": datetime.now()
        }

    except Exception as e:
        raise RuntimeError(f"Crypto fetch failed for {coin_id}: {e}")