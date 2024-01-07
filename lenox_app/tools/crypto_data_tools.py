import requests
import os
from textblob import TextBlob  # Simple library for sentiment analysis
import tweepy  # Twitter API library
import logging

class CryptoDataTools:
    @staticmethod
    def fetch_and_analyze_prices(cryptocurrency):
        try:
            # Set your CoinMarketCap API Key
            api_key = os.getenv('COINMARKETCAP_API_KEY')
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': api_key,
            }
            
            # Fetch the latest price
            url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={cryptocurrency}"
            response = requests.get(url, headers=headers)
            data = response.json()

            # Extract price and other data
            latest_price = data['data'][cryptocurrency]['quote']['USD']['price']

            # Placeholder for moving average; replace with actual calculation
            moving_average = latest_price  # This is a placeholder

            logging.info('Successfully fetched and analyzed prices')
            return {
                'latest_price': latest_price,
                'moving_average': moving_average
            }
        except Exception as e:
            logging.error(f"Error in fetch_and_analyze_prices: {e}")
            return None  # or a suitable default value indicating failure


    @staticmethod
    def analyze_sentiment(cryptocurrency):
        """
        Analyzes market sentiment for a given cryptocurrency using Twitter data.
        :param cryptocurrency: The symbol of the cryptocurrency to analyze (e.g., 'BTC').
        :return: A sentiment score.
        """
        try:
            # Authenticate with the Twitter API
            auth = tweepy.OAuthHandler(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET'))
            auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
            api = tweepy.API(auth)

            # Fetch recent tweets about the cryptocurrency
            tweets = api.search_tweets(q=cryptocurrency, count=100)

            # Perform sentiment analysis on tweets
            sentiment_sum = 0
            for tweet in tweets:
                analysis = TextBlob(tweet.text)
                sentiment_sum += analysis.sentiment.polarity

            # Calculate average sentiment
            average_sentiment = sentiment_sum / len(tweets) if tweets else 0

            return {
                'sentiment_score': average_sentiment
            }
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def formulate_strategy(price_data, sentiment_data):
        """
        Formulates a trading strategy based on price and sentiment data.
        :param price_data: The data returned from fetch_and_analyze_prices.
        :param sentiment_data: The data returned from analyze_sentiment.
        :return: A trading strategy.
        """
        try:
            strategy = "hold"
            if price_data.get('latest_price', 0) > price_data.get('moving_average', 0) and sentiment_data.get('sentiment_score', 0) > 0:
                strategy = "buy"
            elif price_data.get('latest_price', 0) < price_data.get('moving_average', 0) and sentiment_data.get('sentiment_score', 0) < 0:
                strategy = "sell"

            return {
                'strategy': strategy
            }
        except Exception as e:
            return {'error': str(e)}
