from crewai import Task
from textwrap import dedent

class CryptoAnalysisTasks():
    def market_research(self, agent, cryptocurrency):
        return Task(description=dedent(f"""
            Collect and summarize recent news articles, tweets, 
            Reddit posts, and market analyses related to the 
            cryptocurrency and its ecosystem.
            Pay special attention to any significant events, market
            sentiments, and community opinions. Include upcoming 
            events like hard forks, upgrades, and regulatory news.
  
            Your final answer MUST be a report that includes a
            comprehensive summary of the latest news, any notable
            shifts in market sentiment, and potential impacts on 
            the cryptocurrency's value.
            Also, return the cryptocurrency symbol.
        
            Selected cryptocurrency by the customer: {cryptocurrency}
          """),
          agent=agent
        )

    def technical_analysis(self, agent, cryptocurrency): 
        return Task(description=dedent(f"""
            Conduct a technical analysis of the cryptocurrency's 
            price action. Utilize tools like moving averages, RSI,
            and other relevant indicators to assess potential 
            buy/sell signals. Compare the cryptocurrency's 
            performance with the overall market and similar coins.
  
            Your final report MUST include a clear assessment of 
            the cryptocurrency's current technical posture with 
            charts and indicators, pointing out key levels, trends, 
            and patterns.
  
            Selected cryptocurrency by the customer: {cryptocurrency}
          """),
          agent=agent
        )

    def sentiment_analysis(self, agent, cryptocurrency):
        return Task(description=dedent(f"""
            Analyze the sentiment of the market towards the 
            selected cryptocurrency. Utilize sources like Twitter,
            Reddit, and news articles to gauge the mood and opinions
            of traders and enthusiasts. Look into the frequency and 
            sentiment of mentions, hashtags, and overall visibility.
  
            Your final answer must be a report that highlights 
            significant sentiment trends, influential posts or 
            articles, and a summary of the community's outlook.
  
            Selected cryptocurrency by the customer: {cryptocurrency}
          """),
          agent=agent
        )

    def strategy_recommendation(self, agent, cryptocurrency):
        return Task(description=dedent(f"""
            Review and synthesize the analyses provided by the
            Technical Analyst and the Sentiment Analyst.
            Combine these insights to form a comprehensive
            investment or trading strategy. 
            
            You MUST consider all aspects, including technical
            charts, market sentiment, and any relevant news or 
            events.

            Your final answer MUST be a strategy recommendation for 
            your customer. It should be a detailed report, providing 
            a clear stance and actionable steps with supporting 
            evidence.

            Selected cryptocurrency by the customer: {cryptocurrency}
          """),
          agent=agent
        )
