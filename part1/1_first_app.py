import pandas as pd
import streamlit as st
import yfinance as yf

st.write("""
## Simple Stock Price App
         
         Shown are the stock closing price and volume of Google!

""")

# Get the symbol.
tickerSymbol = "AAPL"
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker as a dataframe.
tickerDf = tickerData.history(period="1d")


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
