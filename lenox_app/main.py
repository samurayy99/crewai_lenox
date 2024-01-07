from crewai import Crew
import os
from agents.crypto_analysis_agents import CryptoAnalysisAgents
from tasks.crypto_tasks import CryptoAnalysisTasks
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

class LenoxCrew:
    def __init__(self, cryptocurrency):
        self.cryptocurrency = cryptocurrency.upper()

    def run(self):
        logging.info(f'Initializing LenoxCrew with cryptocurrency: {self.cryptocurrency}')
        agents = CryptoAnalysisAgents()
        tasks = CryptoAnalysisTasks()

        try:
            technical_analyst_agent = agents.create_technical_analyst(self.cryptocurrency)
            sentiment_analyst_agent = agents.create_sentiment_analyst(self.cryptocurrency)
            strategy_advisor_agent = agents.create_strategy_advisor(self.cryptocurrency)

            market_research_task = tasks.compile_market_research(technical_analyst_agent, self.cryptocurrency)
            technical_analysis_task = tasks.perform_technical_analysis(technical_analyst_agent, self.cryptocurrency)
            sentiment_analysis_task = tasks.conduct_sentiment_analysis(sentiment_analyst_agent, self.cryptocurrency)
            strategy_recommendation_task = tasks.formulate_strategy_recommendation(strategy_advisor_agent, self.cryptocurrency)

            crew = Crew(
                agents=[technical_analyst_agent, sentiment_analyst_agent, strategy_advisor_agent],
                tasks=[market_research_task, technical_analysis_task, sentiment_analysis_task, strategy_recommendation_task],
                verbose=True
            )

            result = crew.kickoff()
            logging.info(f'After crew kickoff, result: {result}')
            return result
        except Exception as e:
            logging.error(f"An error occurred during the crew process: {e}")
            raise

if __name__ == "__main__":
    try:
        print("## Welcome to Lenox Crypto Analysis")
        print('-------------------------------------')
        cryptocurrency = input("What is the cryptocurrency you want to analyze? (e.g., BTC, ETH) ")
        if not cryptocurrency:
            raise ValueError("No cryptocurrency provided.")
        
        lenox_crew = LenoxCrew(cryptocurrency)
        result = lenox_crew.run()
        print("\n\n########################")
        print("## Here is the Report")
        print("########################\n")
        print(result)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        exit(1)
