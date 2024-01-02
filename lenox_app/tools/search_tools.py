import os
import json
import requests
from langchain.tools import tool

class SearchTools():
    @tool("Search the internet")
    def search_internet(query):
        # Replace 'SERPER_API_KEY' with your actual API key for SERPER
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {'X-API-KEY': os.environ['SERPER_API_KEY'], 'content-type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        # Handle potential errors and unexpected responses
        if response.status_code == 200:
            results = response.json().get('organic', [])
            return "\n".join([f"Title: {r['title']}\nLink: {r['link']}\nSnippet: {r['snippet']}\n-----------------" for r in results[:4]])
        else:
            return "Failed to search the internet."

    @tool("Search news on the internet")
    def search_news(query):
        # Similar structure to search_internet, but targeting news sources
        # Ensure proper error handling and response validation
        # ...
