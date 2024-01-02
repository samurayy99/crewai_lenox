# real_time_data_collector.py
from binance.client import Client
import os
import json

class RealTimeDataCollector:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def fetch_real_time_price(self, symbol):
        ticker = self.client.get_symbol_ticker(symbol=symbol)
        with open(f'data/real_time_data/{symbol}_real_time.json', 'w') as file:
            json.dump(ticker, file)
        print(f"Real-time price for {symbol} saved.")

if __name__ == "__main__":
    # Example usage
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    collector = RealTimeDataCollector(api_key, api_secret)
    collector.fetch_real_time_price('BTCUSDT')  # Fetch real-time price for BTC/USDT
