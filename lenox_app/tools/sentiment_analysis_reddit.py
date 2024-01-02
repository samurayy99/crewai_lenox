import praw
import os
from nltk.sentiment import SentimentIntensityAnalyzer
from langchain.tools import tool

class RedditSentimentAnalysis:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_USER_AGENT')
        )
        self.sia = SentimentIntensityAnalyzer()

    @tool("Analyze Reddit Sentiment")
    def analyze_reddit_sentiment(self, keywords, subreddits, limit=100):
        try:
            posts = []
            for subreddit in subreddits:
                for post in self.reddit.subreddit(subreddit).hot(limit=limit):
                    if any(keyword.lower() in post.title.lower() for keyword in keywords):
                        sentiment_score = self.sia.polarity_scores(post.title)
                        posts.append({
                            'title': post.title,
                            'sentiment': sentiment_score['compound'],
                            'url': post.url
                        })
            return {'status': 'success', 'data': posts}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
