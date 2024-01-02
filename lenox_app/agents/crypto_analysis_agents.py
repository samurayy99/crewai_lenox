from crewai import Agent
from tools.crypto_data_tools import CryptoDataTools

class CryptoAnalysisAgents:
    def create_technical_analyst(self, cryptocurrency):
        """
        Instantiate a Technical Analyst agent equipped with specialized cryptocurrency analysis tools.
        :param cryptocurrency: The symbol of the cryptocurrency to analyze (e.g., 'BTC').
        """
        tools = [
            CryptoDataTools.fetch_and_analyze_prices(cryptocurrency),
            CryptoDataTools.analyze_sentiment(cryptocurrency),
            CryptoDataTools.formulate_strategy  # Ensure this is callable or a valid tool
        ]
        if not all(tools):  # Check if any tool is None or invalid
            raise ValueError("One or more tools are not correctly initialized for Technical Analyst.")
        return Agent(
            role='Crypto Technical Analyst',
            goal="Deliver state-of-the-art technical analysis for cryptocurrencies, aiming to provide clients with precise forecasts and valuable insights.",
            backstory="A well-versed analyst boasting extensive experience in the cryptocurrency markets, renowned for pinpointing market trends and delivering deep analysis.",
            verbose=True,
            tools=tools
        )

    def create_sentiment_analyst(self, cryptocurrency):
        tools = [
            CryptoDataTools.analyze_sentiment(cryptocurrency)
        ]
        if not all(tools):  # Check if any tool is None or invalid
            raise ValueError("One or more tools are not correctly initialized for Sentiment Analyst.")
        return Agent(
            role='Crypto Sentiment Analyst',
            goal="Analyze and interpret the market sentiment surrounding various cryptocurrencies to offer a detailed perspective.",
            backstory="Renowned for a keen ability to navigate through social media, news outlets, and forums to precisely gauge public sentiment regarding diverse cryptocurrencies.",
            verbose=True,
            tools=tools
        )

    def create_strategy_advisor(self, cryptocurrency):
        tools = [
            CryptoDataTools.formulate_strategy  # Ensure this is callable or a valid tool
        ]
        if not all(tools):  # Check if any tool is None or invalid
            raise ValueError("One or more tools are not correctly initialized for Strategy Advisor.")
        return Agent(
            role='Crypto Strategy Advisor',
            goal="Synthesize technical and sentiment analyses to develop well-rounded trading and investment strategies.",
            backstory="A seasoned strategist who integrates a variety of analytical insights to craft informed, strategic advice tailored to cryptocurrency investments.",
            verbose=True,
            tools=tools
        )
