from crewai import Task
from textwrap import dedent

class CryptoAnalysisTasks():
    def market_research(self, agent, cryptocurrency):
        return Task(description=dedent(f"""
            Collect and summarize recent news articles, tweets, Reddit posts, and market analyses related to {cryptocurrency}.
            Pay special attention to any significant events, market sentiments, and community opinions. Include upcoming events like hard forks, upgrades, and regulatory news.
            The final report should provide a comprehensive summary of the latest news, notable shifts in market sentiment, and potential impacts on {cryptocurrency}'s value.
            """),
          agent=agent
        )

    def technical_analysis(self, agent, cryptocurrency): 
        return Task(description=dedent(f"""
            Conduct a technical analysis of {cryptocurrency}'s price action using tools like moving averages, RSI, and other relevant indicators.
            Compare the cryptocurrency's performance with the overall market and similar coins.
            The final report should assess {cryptocurrency}'s current technical posture with charts and indicators, highlighting key levels, trends, and patterns.
            """),
          agent=agent
        )

    def sentiment_analysis(self, agent, cryptocurrency):
        return Task(description=dedent(f"""
            Analyze the sentiment of the market towards {cryptocurrency} using sources like Twitter, Reddit, and news articles.
            The final report should highlight significant sentiment trends, influential posts or articles, and a summary of the community's outlook.
            """),
          agent=agent
        )

    def strategy_recommendation(self, agent, cryptocurrency):
        return Task(description=dedent(f"""
            Review and synthesize analyses to form a comprehensive investment or trading strategy for {cryptocurrency}.
            Consider all aspects, including technical charts, market sentiment, and relevant news or events.
            The final strategy recommendation should provide clear actionable steps with supporting evidence.
            """),
          agent=agent
        )
