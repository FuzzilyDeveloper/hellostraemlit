
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Set page title
st.title("Simple Stock Data App")

# Sidebar for user inputs
st.sidebar.header("Stock Selection")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT):", value="AAPL").upper()
start_date = st.sidebar.date_input("Start Date", value=datetime.now() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", value=datetime.now())

# Fetch stock data
if ticker:
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(start=start_date, end=end_date)

        if not df.empty:
            # Display stock info
            st.header(f"{ticker} Stock Data")
            st.subheader("Company Info")
            info = stock.info
            st.write(f"**Name**: {info.get('longName', 'N/A')}")
            st.write(f"**Sector**: {info.get('sector', 'N/A')}")
            st.write(f"**Market Cap**: ${info.get('marketCap', 'N/A'):,.2f}")

            # Plot stock closing price
            st.subheader("Closing Price Chart")
            fig = px.line(df, x=df.index, y="Close", title=f"{ticker} Closing Price")
            st.plotly_chart(fig)

            # Display data table
            st.subheader("Historical Data")
            st.dataframe(df[["Open", "High", "Low", "Close", "Volume"]].round(2))

            # Key metrics
            st.subheader("Key Metrics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Current Price", f"${df['Close'][-1]:,.2f}")
            with col2:
                st.metric("52-Week High", f"${info.get('fiftyTwoWeekHigh', 'N/A'):,.2f}")
            with col3:
                st.metric("52-Week Low", f"${info.get('fiftyTwoWeekLow', 'N/A'):,.2f}")

        else:
            st.error("No data found for the selected ticker or date range.")
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {str(e)}")
else:
    st.info("Please enter a valid stock ticker to begin.")

# Instructions to run the app
st.sidebar.markdown("""
---
### How to Run
1. Save this code as `app.py`.
2. Install dependencies:  
   ```bash
   pip install streamlit yfinance pandas plotly
   """)
