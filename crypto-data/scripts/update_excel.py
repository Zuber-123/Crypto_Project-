import pandas as pd
import requests
import time

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return []

def update_excel():
    while True:
        data = fetch_crypto_data()
        if data:
            df = pd.DataFrame(data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"])
            df.to_excel("data/Crypto_Live_Data.xlsx", index=False)
            print("Excel file updated.")
        
        time.sleep(300)  # Update every 5 minutes

if __name__ == "__main__":
    update_excel()
