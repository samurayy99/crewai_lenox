from crewai import Agent

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.crypto_data_tools import CryptoDataTools

class CryptoAnalysisAgents():
    def technical_analyst(self):
        return Agent(
          role='Crypto Technical Analyst',
          goal="""Provide cutting-edge technical analysis for cryptocurrencies 
          and impress clients with accurate predictions and insights.""",
          backstory="""A seasoned analyst with years of experience 
          in crypto markets, known for accurate trend predictions 
          and insightful analysis.""",
          verbose=True,
          tools=[
            CryptoDataTools.fetch_and_analyze_prices,
            CalculatorTools.calculate,
            BrowserTools.scrape_and_summarize_website,
            SearchTools.search_internet,
          ]
        )

    def sentiment_analyst(self):
        return Agent(
          role='Crypto Sentiment Analyst',
          goal="""Gauge and interpret the market sentiment for various 
          cryptocurrencies to provide a comprehensive outlook.""",
          backstory="""Known for the ability to sift through social media, 
          news, and forums to accurately assess the public sentiment 
          towards different cryptocurrencies.""",
          verbose=True,
          tools=[
            SearchTools.search_social_media,
            SearchTools.search_news,
            BrowserTools.scrape_and_summarize_website,
          ]
        )

    def strategy_advisor(self):
        return Agent(
          role='Crypto Strategy Advisor',
          goal="""Combine technical and sentiment analysis to formulate 
          comprehensive trading or investment strategies.""",
          backstory="""An experienced advisor who combines various analytical 
          insights to formulate strategic advice for crypto investments.""",
          verbose=True,
          tools=[
            BrowserTools.scrape_and_summarize_website,
            SearchTools.search_internet,
            CalculatorTools.calculate,
          ]
        )
