from crewai import Crew
from textwrap import dedent
import os
from agents.crypto_analysis_agents import CryptoAnalysisAgents
from tasks.crypto_tasks import CryptoAnalysisTasks
import logging
from dotenv import load_dotenv
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

class LenoxCrew:
    def __init__(self, cryptocurrency):
        self.cryptocurrency = cryptocurrency

    def run(self):
        agents = CryptoAnalysisAgents()
        tasks = CryptoAnalysisTasks()

        # Pass the cryptocurrency parameter to agent creation methods
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
        return result

if __name__ == "__main__":
    print("## Welcome to Lenox Crypto Analysis")
    print('-------------------------------------')
    cryptocurrency = input("What is the cryptocurrency you want to analyze? (e.g., BTC, ETH) ").strip().upper()
    
    if not cryptocurrency:
        logging.error("No cryptocurrency provided. Exiting.")
        exit(1)

    lenox_crew = LenoxCrew(cryptocurrency)
    result = lenox_crew.run()
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)
