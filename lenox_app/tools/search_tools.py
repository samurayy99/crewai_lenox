import os
import json
import requests
from langchain.tools import tool

class SearchTools():
    @tool("Search the internet")
    def search_internet(self, query):
        """
        Searches the internet for the given query and returns the results.
        :param query: The search query string.
        :return: A dictionary of search results.
        """
        try:
            # Replace 'SERPER_API_KEY' with your actual API key for SERPER
            url = "https://google.serper.dev/search"
            payload = json.dumps({"q": query})
            headers = {'X-API-KEY': os.environ['SERPER_API_KEY'], 'content-type': 'application/json'}
            response = requests.post(url, headers=headers, data=payload)

            # Handle potential errors and unexpected responses
            if response.status_code == 200:
                results = response.json().get('organic', [])
                return {'status': 'success', 'data': [{'title': r['title'], 'link': r['link'], 'snippet': r['snippet']} for r in results[:4]]}
            else:
                raise Exception(f"Failed to search the internet with status code: {response.status_code}")
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    @tool("Search news on the internet")
    def search_news(self, query):
        """
        Searches news sources on the internet for the given query and returns the results.
        :param query: The search query string.
        :return: A dictionary of news search results.
        """
        try:
            # Similar structure to search_internet, but targeting news sources
            # Replace 'NEWS_API_KEY' with your actual API key for the news service
            url = "https://newsapi.org/v2/everything"
            params = {'q': query, 'apiKey': os.environ['NEWS_API_KEY']}
            response = requests.get(url, params=params)

            # Handle potential errors and unexpected responses
            if response.status_code == 200:
                articles = response.json().get('articles', [])
                return {'status': 'success', 'data': [{'title': article['title'], 'url': article['url'], 'snippet': article['description']} for article in articles]}
            else:
                raise Exception(f"Failed to search news with status code: {response.status_code}")
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
