from crewai import Crew
from textwrap import dedent

from agents.crypto_analysis_agents import CryptoAnalysisAgents
from tasks.crypto_tasks import CryptoAnalysisTasks

from dotenv import load_dotenv
load_dotenv()

class LenoxCrew:
    def __init__(self, cryptocurrency):
        self.cryptocurrency = cryptocurrency

    def run(self):
        agents = CryptoAnalysisAgents()
        tasks = CryptoAnalysisTasks()

        technical_analyst_agent = agents.technical_analyst()
        sentiment_analyst_agent = agents.sentiment_analyst()
        strategy_advisor_agent = agents.strategy_advisor()

        market_research_task = tasks.market_research(technical_analyst_agent, self.cryptocurrency)
        technical_analysis_task = tasks.technical_analysis(technical_analyst_agent, self.cryptocurrency)
        sentiment_analysis_task = tasks.sentiment_analysis(sentiment_analyst_agent, self.cryptocurrency)
        strategy_recommendation_task = tasks.strategy_recommendation(strategy_advisor_agent, self.cryptocurrency)

        crew = Crew(
            agents=[
                technical_analyst_agent,
                sentiment_analyst_agent,
                strategy_advisor_agent
            ],
            tasks=[
                market_research_task,
                technical_analysis_task,
                sentiment_analysis_task,
                strategy_recommendation_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to Lenox Crypto Analysis")
    print('-------------------------------------')
    cryptocurrency = input(
        dedent("""
            What is the cryptocurrency you want to analyze? (e.g., BTC, ETH)
        """)
    )

    lenox_crew = LenoxCrew(cryptocurrency.upper())
    result = lenox_crew.run()
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)
