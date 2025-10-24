from dotenv import load_dotenv
from fetch_weather import fetch_weather
from send_email import send_email
from fetch_news import fetch_news

load_dotenv()

if __name__=="__main__":
    city_name=input("Enter the city name:- ")
    emailId=input("Enter the receiver's email id:- ")
    weather=fetch_weather()
    weather_data=weather.get_weather(city_name)
    country_name=weather.get_country(city_name)

    news=fetch_news()
    news_data=news.extract_news(country_name)

    mail=send_email()
    mail.sending_email(weather_data, city_name, news_data, emailId)