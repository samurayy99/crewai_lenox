from crewai import Task
from textwrap import dedent

class CryptoAnalysisTasks:
    def compile_market_research(self, agent, cryptocurrency):
        """Compile comprehensive market research for a specified cryptocurrency."""
        return Task(
            description=dedent(f"""
                Gather and synthesize recent news articles, tweets, Reddit posts, and market analyses concerning {cryptocurrency}.
                Focus particularly on significant events, shifts in market sentiment, and community opinions. Include forthcoming events like hard forks, upgrades, and regulatory developments.
                The final report should offer an exhaustive summary of the latest news, notable changes in market sentiment, and potential impacts on {cryptocurrency}'s value.
                """),
            agent=agent
        )

    def perform_technical_analysis(self, agent, cryptocurrency): 
        """Perform detailed technical analysis for a specified cryptocurrency."""
        return Task(
            description=dedent(f"""
                Execute a technical analysis of {cryptocurrency}'s price movements using tools such as moving averages, RSI, and other pertinent indicators.
                Benchmark {cryptocurrency}'s performance against the broader market and similar cryptocurrencies.
                The final report should provide a detailed assessment of {cryptocurrency}'s current technical stance, featuring charts and indicators, and spotlighting crucial levels, trends, and patterns.
                """),
            agent=agent
        )

    def conduct_sentiment_analysis(self, agent, cryptocurrency):
        """Conduct sentiment analysis to gauge market mood towards a specified cryptocurrency."""
        return Task(
            description=dedent(f"""
                Examine market sentiment towards {cryptocurrency} utilizing sources like Twitter, Reddit, and news articles.
                The final report should illuminate prominent sentiment trends, key posts or articles, and encapsulate the community's overall perspective.
                """),
            agent=agent
        )

    def formulate_strategy_recommendation(self, agent, cryptocurrency):
        """Formulate a strategy recommendation based on comprehensive analyses for a specified cryptocurrency."""
        return Task(
            description=dedent(f"""
                Integrate and interpret analyses to devise a holistic investment or trading strategy for {cryptocurrency}.
                Take into account all elements, including technical charts, market sentiment, and pertinent news or events.
                The final strategy recommendation should articulate clear, actionable steps backed by substantial evidence.
                """),
            agent=agent
        )
