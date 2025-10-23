import os
import smtplib

class send_email:
    def __init__(self):
        self.email=os.getenv("EMAIL_USER")
        self.password=os.getenv("EMAIL_PASS")

    def sending_email(self, weather, city, news):
        s=smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.email, self.password)
        message=self.generate_msg(weather, city, news)
        s.sendmail(self.email, self.email, message)
        print("\nEmail sent successfully!!\n")
        s.quit()

    def generate_msg(self, weather, city, news):
        body=f"""
        In {city} weather details are as follows:- 
        Description:- {weather["description"]}
        Temperature:- {weather["temp"]}
        Pressure:- {weather["pressure"]}
        Humidity:- {weather["humidity"]}
        """

        if "rain" in weather:
            body=body+f"Rain:- {weather['rain']}\n"

        body+=f"\nTop Headlines:- \n{news}\nThank You!!\n-Automated-data-aggregator"
        return body
