import streamlit as st
import requests
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Set the API key for MediaStack
api_key = "371a1750c4791037ce0a4d98b7bfd6b9"

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

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

# Evaluate undervalued/neutral/overvalued stock
if cumulative_sentiment > 0.2:
    st.success("Stock is Undervalued!")
elif -0.2 <= cumulative_sentiment <= 0.2:
    st.info("Stock is Neutral.")
else:
    st.error("Stock is Overvalued!")

# End of Streamlit App
