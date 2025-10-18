import os
import requests

class fetch_weather:
    def __init__(self):
        self.weather_url=os.getenv("WEATHER_URL")
        self.lat_long_url=os.getenv("LAT_LONG_URL")
        self.api=os.getenv("WEATHER_API_KEY")

    def lat_long_data(self, city):
        lat_params={"q":city, "appid":self.api}
        lat_long_data=requests.get(self.lat_long_url, lat_params)
        return lat_long_data.json()
    
    def fetch_data(self, city):
        coords_data=self.lat_long_data(city)
        lat=coords_data[0]["lat"]
        long=coords_data[0]["lon"]
        weather_params={"lat":lat, "lon":long, "appid":self.api}
        response=requests.get(self.weather_url, weather_params)
        return response.json()

    def get_country(self, city):
        country_data=self.lat_long_data(city)
        return country_data[0]["state"]
    
    def extract_data(self, data):
        weather_details={
            "description": data["weather"][0]["description"],
            "temp": data["main"]["temp"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "visibility": data["visibility"],
            "wind_speed": data["wind"]["speed"],
            "cloudiness": data["clouds"]["all"]
        }

        if "rain" in data:
            weather_details["rain"]=data["rain"]["1h"]

        return weather_details
    
    def get_weather(self, city):
        data=self.fetch_data(city)
        return self.extract_data(data)