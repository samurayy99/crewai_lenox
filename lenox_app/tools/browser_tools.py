import os
import json
import requests
from langchain.tools import tool
from unstructured.partition.html import partition_html

class BrowserTools():

    @tool("Scrape website content")
    def scrape_and_summarize_website(self, website):
        try:
            # Ensure to replace 'BROWSERLESS_API_KEY' with your actual API key for browserless
            url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
            payload = json.dumps({"url": website})
            headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
            response = requests.post(url, headers=headers, data=payload)
            
            # Handle potential errors and unexpected responses
            if response.status_code == 200:
                elements = partition_html(text=response.text)
                content = "\n\n".join([str(el) for el in elements])
                return {'status': 'success', 'data': {'content': content}}
            else:
                raise Exception(f"Failed to scrape the website with status code: {response.status_code}")
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
