from crewai import Agent
from tools.crypto_data_tools import CryptoDataTools
import logging

class CryptoAnalysisAgents:
    def create_technical_analyst(self, cryptocurrency):
        logging.info('Creating technical analyst with cryptocurrency: %s', cryptocurrency)
        
        # Define the tools within the method scope
        tools = [
            lambda: CryptoDataTools.fetch_and_analyze_prices(cryptocurrency),
            lambda: CryptoDataTools.analyze_sentiment(cryptocurrency),
            lambda price_data, sentiment_data: CryptoDataTools.formulate_strategy(price_data, sentiment_data)
        ]
        
        # Check if tools are callable and add enhanced error logging
        try:
            for tool in tools:
                if not callable(tool):
                    logging.error(f"Tool {tool} is not callable.")
                    raise ValueError(f"Tool {tool} is not callable.")
            logging.info('All tools are callable for Technical Analyst')
            
            return Agent(
                role='Crypto Technical Analyst',
                goal="Deliver state-of-the-art technical analysis for cryptocurrencies, aiming to provide clients with precise forecasts and valuable insights.",
                backstory="A well-versed analyst boasting extensive experience in the cryptocurrency markets, renowned for pinpointing market trends and delivering deep analysis.",
                verbose=True,
                tools=tools
            )
        except Exception as e:
            logging.error(f"An error occurred while initializing tools for Technical Analyst: {e}")
            raise


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
        logging.info('Creating strategy advisor with cryptocurrency: %s', cryptocurrency)

        # Create a lambda function to wrap the 'formulate_strategy' method
        strategy_formulate_lambda = lambda price_data, sentiment_data: CryptoDataTools.formulate_strategy(price_data, sentiment_data)

        # Add the lambda function to the tools list
        tools = [
            strategy_formulate_lambda
        ]

        # Check if all tools are callable
        if not all(callable(tool) for tool in tools):
            logging.error('One or more tools are not callable for Strategy Advisor.')
            raise ValueError("One or more tools are not callable for Strategy Advisor.")
        logging.info('All tools are callable for Strategy Advisor')

        # Return the Agent with the tools
        return Agent(
            role='Crypto Strategy Advisor',
            goal="Synthesize technical and sentiment analyses to develop well-rounded trading and investment strategies.",
            backstory="A seasoned strategist who integrates a variety of analytical insights to craft informed, strategic advice tailored to cryptocurrency investments.",
            verbose=True,
            tools=tools
        )


