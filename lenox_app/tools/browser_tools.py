import os
import json
import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html

class BrowserTools():

    @tool("Scrape website content")
    def scrape_and_summarize_website(website):
        # Ensure to replace 'BROWSERLESS_API_KEY' with your actual API key for browserless
        url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
        payload = json.dumps({"url": website})
        headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        # Handle potential errors and unexpected responses
        if response.status_code == 200:
            elements = partition_html(text=response.text)
            content = "\n\n".join([str(el) for el in elements])
            # Simplified content handling for demonstration
            return content
        else:
            return "Failed to scrape the website."
