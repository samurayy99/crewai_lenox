from crewai import Task, Agent  # Import the Agent class here
from textwrap import dedent

class CryptoAnalysisTasks:
    def compile_market_research(self, agent, cryptocurrency):
        if not isinstance(agent, Agent):  # Validate that the provided agent is an instance of Agent
            raise ValueError("The provided agent is not an instance of Agent.")
        return Task(
            description=dedent(f"""
                Gather and synthesize recent news articles, tweets, Reddit posts, and market analyses concerning {cryptocurrency}.
                Focus particularly on significant events, shifts in market sentiment, and community opinions. Include forthcoming events like hard forks, upgrades, and regulatory developments.
                The final report should offer an exhaustive summary of the latest news, notable changes in market sentiment, and potential impacts on {cryptocurrency}'s value.
                """),
            agent=agent
        )

    # Define additional tasks here as needed, following the same pattern:
    # def perform_technical_analysis(self, agent, cryptocurrency):
    #     # Ensure agent is a valid instance of Agent
    #     # Return a Task with a specific description and the associated agent

    # def conduct_sentiment_analysis(self, agent, cryptocurrency):
    #     # Ensure agent is a valid instance of Agent
    #     # Return a Task with a specific description and the associated agent

    # def formulate_strategy_recommendation(self, agent, cryptocurrency):
    #     # Ensure agent is a valid instance of Agent
    #     # Return a Task with a specific description and the associated agent
