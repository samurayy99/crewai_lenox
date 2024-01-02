from crewai import Agent
from tools.crypto_data_tools import CryptoDataTools



class CryptoAnalysisAgents:
    def create_technical_analyst(self):
        """Instantiate a Technical Analyst agent equipped with specialized cryptocurrency analysis tools."""
        return Agent(
            role='Crypto Technical Analyst',
            goal="Deliver state-of-the-art technical analysis for cryptocurrencies, aiming to provide clients with precise forecasts and valuable insights.",
            backstory="A well-versed analyst boasting extensive experience in the cryptocurrency markets, renowned for pinpointing market trends and delivering deep analysis.",
            verbose=True,
            tools=[CryptoDataTools.fetch_and_analyze_prices]  # Ensure this method exists and is callable.
        )

    def create_sentiment_analyst(self):
        """Instantiate a Sentiment Analyst agent equipped with tools for analyzing market sentiment."""
        return Agent(
            role='Crypto Sentiment Analyst',
            goal="Analyze and interpret the market sentiment surrounding various cryptocurrencies to offer a detailed perspective.",
            backstory="Renowned for a keen ability to navigate through social media, news outlets, and forums to precisely gauge public sentiment regarding diverse cryptocurrencies.",
            verbose=True,
            tools=[CryptoDataTools.analyze_sentiment]  # Ensure this method exists and is callable.
        )

    def create_strategy_advisor(self):
        """Instantiate a Strategy Advisor agent equipped with tools for developing investment strategies."""
        return Agent(
            role='Crypto Strategy Advisor',
            goal="Synthesize technical and sentiment analyses to develop well-rounded trading and investment strategies.",
            backstory="A seasoned strategist who integrates a variety of analytical insights to craft informed, strategic advice tailored to cryptocurrency investments.",
            verbose=True,
            tools=[CryptoDataTools.formulate_strategy]  # Ensure this method exists and is callable.
        )

class Agent:
    def __init__(self, role, goal, backstory, verbose, tools=None):
        """
        Initialize an Agent with the given parameters.
        
        :param role: The role of the agent (e.g., 'Crypto Technical Analyst').
        :param goal: The goal or objective of the agent.
        :param backstory: The backstory providing context to the agent's role and goal.
        :param verbose: A boolean indicating if the agent should provide verbose output.
        :param tools: A list of tools the agent can use to perform its tasks. Defaults to an empty list if not provided.
        """
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.verbose = verbose
        self.tools = tools if tools is not None else []  # Set tools to an empty list if none are provided

        # ... rest of the initialization ...
