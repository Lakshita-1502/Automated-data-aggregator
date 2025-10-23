import os
import requests
import pycountry

class fetch_news:
    def __init__(self):
        self.news_api=os.getenv("NEWS_API_KEY")
        self.news_url=os.getenv("NEWS_URL")

    def get_news(self, country):
        news_country=pycountry.countries.get(alpha_2=country)
        params = {
            "q": news_country.name,
            "apiKey": self.news_api,
            "pageSize": 3
        }
        response=requests.get(self.news_url, params)
        return response.json()

    def extract_news(self, country):
        data=self.get_news(country)
        news_data=[]
        for i in range(3):
            news_data.append(data["articles"][i]["title"])
        return news_data