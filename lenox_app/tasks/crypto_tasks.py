from crewai import Task, Agent  # Import the Agent class here
from textwrap import dedent

class CryptoAnalysisTasks:
    def compile_market_research(self, agent, cryptocurrency):
        if not isinstance(agent, Agent):  # Validate that the provided agent is an instance of Agent
            raise ValueError("The provided agent is not an instance of Agent.")
        return Task(
            description=dedent(f'''
                Gather and synthesize recent news articles, tweets, Reddit posts, and market analyses concerning {cryptocurrency}.
                Focus particularly on significant events, shifts in market sentiment, and community opinions. Include forthcoming events like hard forks, upgrades, and regulatory developments.
                The final report should offer an exhaustive summary of the latest news, notable changes in market sentiment, and potential impacts on {cryptocurrency}'s value.
                '''),
            agent=agent
        )

    def perform_technical_analysis(self, agent, cryptocurrency):
        if not isinstance(agent, Agent):
            raise ValueError("The provided agent is not an instance of Agent.")
        return Task(
            description=dedent(f'''
                Perform a comprehensive technical analysis on {cryptocurrency}, examining historical data, price patterns, and various technical indicators.
                The analysis should cover trends, momentum, volatility, and volume, offering a detailed overview of the current technical landscape.
                Conclude with actionable insights and potential trading signals based on the technical findings.
                '''),
            agent=agent
        )

    def conduct_sentiment_analysis(self, agent, cryptocurrency):
        if not isinstance(agent, Agent):
            raise ValueError("The provided agent is not an instance of Agent.")
        return Task(
            description=dedent(f'''
                Analyze the market sentiment surrounding {cryptocurrency} by collecting and evaluating sentiment data from various social media platforms and news sources.
                Utilize natural language processing techniques to gauge public mood and opinion trends.
                Summarize the sentiment findings and discuss their potential impact on the cryptocurrency's market behavior and investor perception.
                '''),
            agent=agent
        )

    def formulate_strategy_recommendation(self, agent, cryptocurrency):
        if not isinstance(agent, Agent):
            raise ValueError("The provided agent is not an instance of Agent.")
        return Task(
            description=dedent(f'''
                Based on the outcomes of technical and sentiment analysis, develop a comprehensive trading or investment strategy for {cryptocurrency}.
                The strategy should consider market conditions, risk tolerance, and investment goals, offering specific recommendations for entry, exit, and portfolio allocation.
                Provide a rationale for each recommendation, supported by the analytical findings.
                '''),
            agent=agent
        )
