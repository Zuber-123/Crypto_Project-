import streamlit as st
import pandas as pd
from scripts.fetch_data import fetch_crypto_data

def load_data():
    data = fetch_crypto_data()
    df = pd.DataFrame(data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"])
    return df

st.title("Live Cryptocurrency Data")
st.write("Fetching top 50 cryptocurrencies in real-time.")

if st.button("Refresh Data"):
    df = load_data()
    st.write(df)
else:
    df = load_data()
    st.write(df)
