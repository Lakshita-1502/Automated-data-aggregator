import os
import requests

class fetch_news:
    def __init__(self):
        self.news_api=os.getenv("NEWS_API_KEY")
        self.news_url=os.getenv("NEWS_URL")

    def get_news(self):
        params = {
            "q": "India",
            "apiKey": self.news_api,
            "pageSize": 1
        }
        response=requests.get(self.news_url, params)
        return response.json()

    def extract_news(self):
        data=self.get_news()
        return data["articles"][0]["title"]