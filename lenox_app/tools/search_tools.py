import os
import json
import requests
from langchain.tools import tool

class SearchTools:
    @tool("Search the web")
    def search_web(self, query, search_type='internet'):
        """
        Searches the web for the given query and returns the results.
        :param query: The search query string.
        :param search_type: 'internet' or 'news' to specify the type of search.
        :return: A dictionary of search results.
        """
        try:
            if search_type == 'internet':
                url = "https://google.serper.dev/search"
                payload = json.dumps({"q": query})
                headers = {'X-API-KEY': os.getenv('SERPER_API_KEY'), 'content-type': 'application/json'}
                response = requests.post(url, headers=headers, data=payload)
            elif search_type == 'news':
                url = "https://newsapi.org/v2/everything"
                params = {'q': query, 'apiKey': os.getenv('NEWS_API_KEY')}
                response = requests.get(url, params=params)
            else:
                raise ValueError("Invalid search type specified.")

            if response.status_code == 200:
                results = response.json().get('articles' if search_type == 'news' else 'organic', [])
                return {'status': 'success', 'data': results[:4]}
            else:
                raise Exception(f"Failed to search with status code: {response.status_code}")
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
