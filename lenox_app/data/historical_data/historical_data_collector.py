# historical_data_collector.py
import requests
import os
import json

def fetch_historical_data(crypto_symbol, compare_symbol='USD', limit=1000):
    url = f'https://min-api.cryptocompare.com/data/v2/histoday'
    params = {
        'fsym': crypto_symbol,
        'tsym': compare_symbol,
        'limit': limit
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json().get('Data').get('Data')
        with open(f'data/historical_data/{crypto_symbol}_{compare_symbol}_historical.json', 'w') as file:
            json.dump(data, file)
        print(f"Historical data for {crypto_symbol} saved.")
    else:
        print("Failed to fetch historical data.")

if __name__ == "__main__":
    # Example usage
    fetch_historical_data('BTC')  # Fetch historical data for Bitcoin
