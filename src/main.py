from dotenv import load_dotenv
from fetch_weather import fetch_weather
from send_email import send_email
from fetch_news import fetch_news

load_dotenv()

if __name__=="__main__":
    city=input("Enter the city name of whose you want the weather details:- ")
    wf=fetch_weather()
    result=wf.get_weather(city)
    fn=fetch_news()
    news=fn.extract_news()
    se=send_email()
    se.sending_email(result, city, news)