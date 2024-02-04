import streamlit as st
import requests
from nltk.sentiment import SentimentIntensityAnalyzer

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

# User input for stock search (without .NS extension)
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., RELIANCE, TCS):").upper()

if not stock_symbol:
    st.warning("Please enter a stock symbol.")
    st.stop()

# MediaStack API endpoint for news without .NS extension
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

# Suggest trend based on sentiment
if cumulative_sentiment > 0.2:
    st.success("Suggested Trend: Upward")
elif -0.2 <= cumulative_sentiment <= 0.2:
    st.info("Suggested Trend: Neutral")
else:
    st.error("Suggested Trend: Downward")

# End of Streamlit App
