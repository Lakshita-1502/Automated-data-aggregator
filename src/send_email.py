import os
import smtplib

class send_email:
    def __init__(self):
        self.email=os.getenv("EMAIL_USER")
        self.password=os.getenv("EMAIL_PASS")

    def sending_email(self, msg, city):
        s=smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.email, self.password)
        message=self.generate_msg(msg, city)
        s.sendmail(self.email, self.email, message)
        s.quit()

    def generate_msg(self, msg, city):
        str=f"""
        In {city} weather details are as follows:- 
        Description:- {msg["description"]}
        Temperature:- {msg["temp"]}
        Pressure:- {msg["pressure"]}
        Humidity:- {msg["humidity"]}
        Visibility:- {msg["visibility"]}
        Wind Speed:- {msg["wind_speed"]}
        Cloudiness:- {msg["cloudiness"]}
        """

        if "rain" in msg:
            str=str+f"""Rain:- {msg["rain"]}\nThank You!!"""
            
        return str
