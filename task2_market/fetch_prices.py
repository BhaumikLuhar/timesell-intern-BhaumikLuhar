import logging
from pathlib import Path
from task2_market.api_clients import fetch_stock_price, fetch_crypto_price


# Logging setup
log_file = Path(__file__).resolve().parent.parent / "logs" / "errors.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(log_file),
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_all_prices():
    """
    Fetch multiple assets with fault tolerance
    """
    results = []

    # Define assets
    stocks = ["^NSEI"]        # NIFTY50
    cryptos = ["bitcoin"]     # BTC
    extras = ["ETH-USD"]      # another asset via yfinance

    # Fetch stocks
    for s in stocks:
        try:
            results.append(fetch_stock_price(s))
        except Exception as e:
            logging.error(str(e))

    # Fetch crypto
    for c in cryptos:
        try:
            results.append(fetch_crypto_price(c))
        except Exception as e:
            logging.error(str(e))

    # Extra asset (optional)
    for e in extras:
        try:
            results.append(fetch_stock_price(e))
        except Exception as ex:
            logging.error(str(ex))

    return results
