import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

class send_email:
    def __init__(self):
        self.email=os.getenv("EMAIL_USER")
        self.password=os.getenv("EMAIL_PASS")
    
    def sending_email(self, weather, city, news, email):
        msg=MIMEMultipart("alternative")
        msg["Subject"]="Daily weather and news update"
        msg["From"]=self.email
        msg["To"]=email
        html=self.generate_msg(weather, city, news)
        msg.attach(MIMEText(html, "html"))

        s=smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.email, self.password)
        s.send_message(msg)
        print("\nEmail sent successfully")
        s.quit()

    def get_current_date(self):
        current_date_time=datetime.now()
        return current_date_time.strftime("%A, %d %B %Y, %I:%M %p")

    def generate_msg(self, weather, city, news):
        date_time=self.get_current_date()
        body=f"""
        <body style="font-family: Arial, sans-serif;">
        <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; margin-bottom:15px;">
        <h2>🌤 {city} Weather Update </h2>
        <b>Description:- </b> {weather["description"].capitalize()}<br>
        <b>Temperature:- </b> {round(weather["temp"]-273.15,2)} °C<br>
        <b>Pressure:- </b> {weather["pressure"]} hPa<br>
        <b>Humidity:- </b> {weather["humidity"]} %<br>
        """

        if "rain" in weather:
            body=body+f"<p><b>Rain:- </b> {weather['rain']}mm<br>\n"

        body+="<h2>\n🗞 Top headlines :- \n</h2>"
        for title in news:
            body+=f"<li>{title}\n</li>"
            
        body+=f"""
        <p>🙏 Thank you for using our service.\n</p>
        <p>🌤️Have a nice Day!\n</p>
        <hr style="margin: 20px 0; border: none; border-top: 1px solid #ddd;">
        <p style="font-size: 13px; color: #777;">
        Report generated on: {date_time}<br>
        You’re receiving this automated weather and news summary.<br>© 2025 Automated Data Aggregator</p>  
        </div>  
        </body>"""
        return body