import pandas as pd

def analyze_crypto_data():
    df = pd.read_csv("data/crypto_data.csv")

    # Top 5 by Market Cap
    top_5 = df.nlargest(5, 'market_cap')[["name", "market_cap"]]

    # Average Price of Top 50 Cryptos
    avg_price = df["current_price"].mean()

    # Highest and Lowest 24h Percentage Change
    highest_change = df.nlargest(1, "price_change_percentage_24h")
    lowest_change = df.nsmallest(1, "price_change_percentage_24h")

    print("Top 5 Cryptos by Market Cap:\n", top_5)
    print("Average Price of Top 50 Cryptos: $", avg_price)
    print("Highest Change (24h):\n", highest_change)
    print("Lowest Change (24h):\n", lowest_change)

if __name__ == "__main__":
    analyze_crypto_data()
