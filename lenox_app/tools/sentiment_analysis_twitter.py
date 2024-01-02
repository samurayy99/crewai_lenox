import os
import tweepy
from nltk.sentiment import SentimentIntensityAnalyzer
from langchain.tools import tool

class TwitterSentimentAnalysis:
    def __init__(self):
        auth = tweepy.OAuthHandler(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET'))
        auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
        self.api = tweepy.API(auth)
        self.sia = SentimentIntensityAnalyzer()

    @tool("Analyze Twitter Sentiment")
    def analyze_twitter_sentiment(self, keywords, limit=100):
        tweets = []
        for keyword in keywords:
            for tweet in tweepy.Cursor(self.api.search, q=keyword, tweet_mode='extended', lang='en').items(limit):
                sentiment_score = self.sia.polarity_scores(tweet.full_text)
                tweets.append({
                    'text': tweet.full_text,
                    'sentiment': sentiment_score['compound'],
                    'url': f"https://twitter.com/user/status/{tweet.id}"
                })
        return tweets


if __name__ == "__main__":
    # Instantiate the analysis tool
    tsa = TwitterSentimentAnalysis()
    
    # Define keywords to monitor
    keywords = ['bitcoin', 'ethereum', 'crypto']
    
    # Perform sentiment analysis
    sentiments = tsa.analyze_twitter_sentiment(keywords)
    print(json.dumps(sentiments, indent=2))
