import streamlit as st
import requests
import pandas as pd

# Set the API key for MediaStack
api_key = "371a1750c4791037ce0a4d98b7bfd6b9"

# Streamlit App
st.title("Algorithmic News Analysis App")

# Sidebar for user input
st.sidebar.header("User Input")

# User input for stock search
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL):").upper()

if not stock_symbol:
    st.warning("Please enter a stock symbol.")
    st.stop()

# MediaStack API endpoint for news
news_url = f"http://api.mediastack.com/v1/news?access_key={api_key}&symbols={stock_symbol}"

# Fetch news data from MediaStack
response = requests.get(news_url)
news_data = response.json()

# Display news headlines
st.subheader(f"Latest News for {stock_symbol}")
for article in news_data['data']:
    st.write(f"- {article['title']}")

# Sentiment Analysis
# You can use your own sentiment analysis model or a pre-trained model here

# Dummy sentiment score for demonstration purposes
sentiment_score = 0.2  # Assume a value between -1 and 1 where -1 is negative, 0 is neutral, and 1 is positive

st.subheader("Sentiment Analysis")
st.write(f"Sentiment Score: {sentiment_score}")

# Evaluate undervalued/neutral/overvalued stock
if sentiment_score > 0.2:
    st.success("Stock is Undervalued!")
elif -0.2 <= sentiment_score <= 0.2:
    st.info("Stock is Neutral.")
else:
    st.error("Stock is Overvalued!")

# Additional functionalities (Gauging market risk, Evaluating company performance) can be added based on the requirements.

# End of Streamlit App
