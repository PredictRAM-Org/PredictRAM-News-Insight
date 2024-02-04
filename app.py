import streamlit as st
import requests
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import yfinance as yf
import matplotlib.pyplot as plt
import nltk

# Download the VADER lexicon file
nltk.download('vader_lexicon')

# Set the API key for MediaStack
api_key = "371a1750c4791037ce0a4d98b7bfd6b9"

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Streamlit App
st.title("Algorithmic News Analysis App")

# Sidebar for user input
st.sidebar.header("User Input")

# User input for stock search
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., RELIANCE, TCS):").upper()

if not stock_symbol:
    st.warning("Please enter a stock symbol.")
    st.stop()

# Define Indian business, economy, and market news sources
indian_news_sources = [
    "moneycontrol.com",
    "thehindubusinessline.com",
    "livemint.com",
    "economictimes.indiatimes.com",
    # Add more sources as needed
]

# MediaStack API endpoint for news from specific Indian sources
news_url = f"http://api.mediastack.com/v1/news?access_key={api_key}&symbols={stock_symbol}&sources={','.join(indian_news_sources)}"

# Fetch news data from MediaStack
response = requests.get(news_url)
news_data = response.json()

# Display news headlines and perform sentiment analysis
st.subheader(f"Latest News for {stock_symbol}")
cumulative_sentiment = 0.0

for article in news_data['data']:
    title = article['title']
    st.write(f"- {title}")
    
    # Sentiment analysis for each article
    sentiment_score = sia.polarity_scores(title)['compound']
    cumulative_sentiment += sentiment_score

    st.write(f"  - Sentiment Score: {sentiment_score:.2f}")

# Display cumulative sentiment score
st.subheader("Cumulative Sentiment Analysis")
st.write(f"Cumulative Sentiment Score: {cumulative_sentiment:.2f}")

# Evaluate undervalued/neutral/overvalued stock based on sentiment
if cumulative_sentiment > 0.2:
    st.success("Stock is Undervalued!")
elif -0.2 <= cumulative_sentiment <= 0.2:
    st.info("Stock is Neutral.")
else:
    st.error("Stock is Overvalued!")

# Fetch stock data using yfinance
stock_data = yf.download(stock_symbol, start="2023-02-04", end="2024-02-04", progress=False)

# Plot stock price trend
st.subheader(f"Stock Price Trend for {stock_symbol}")
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'])
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.title(f'Stock Price Trend for {stock_symbol}')
st.pyplot(plt)

# End of Streamlit App
