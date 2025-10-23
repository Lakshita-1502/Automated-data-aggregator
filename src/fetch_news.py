import os
import requests
import pycountry

class fetch_news:
    def __init__(self):
        self.news_api=os.getenv("NEWS_API_KEY")
        self.news_url=os.getenv("NEWS_URL")

    def get_news(self, country):
        news_country=pycountry.countries.get(alpha_2=country.upper())
        print(f"News country:- {pycountry.countries.get(alpha_2=country.upper())}")
        print(f"News_country_name:- {news_country.name}")
        params = {
            "q": news_country.name,
            "apiKey": self.news_api,
            "pageSize": 1
        }
        response=requests.get(self.news_url, params)
        return response.json()

    def extract_news(self, country):
        data=self.get_news(country)
        print(f"Extracted news country:- {country}")
        print(f"Total articles:- {data["totalResults"]}")
        return data["articles"][0]["title"]