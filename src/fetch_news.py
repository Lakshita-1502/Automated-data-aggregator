from dotenv import load_dotenv
import os
import requests

load_dotenv()

news_api=os.getenv("NEWS_API_KEY")
news_url=os.getenv("NEWS_URL")
params = {
    "q": "India",
    "apiKey": news_api,
    "pageSize": 1
}

response=requests.get(news_url, params)
news_data=response.json()

print(f"Title:- {news_data["articles"][0]["title"]}")
print(f"Description:- {news_data["articles"][0]["description"]}")