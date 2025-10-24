# 🌦️Automated Data Aggregator
An automation-based Python project that fetches real-time weather details and top news headlines for a given city, and automatically sends them via email notifications to users.

This project demonstrates the integration of multiple APIs, automation, and email delivery, ideal for productivity, daily updates, and smart information aggregation.

## 🚀Features

🌤 Real-time Weather Fetching – Gets the latest temperature, humidity, and weather conditions for a user-specified city.

🗞️ Top Headlines Aggregation – Fetches current top news headlines for that region or globally.

📧 Automated Email Delivery – Sends the aggregated data directly to the user’s email inbox.

⚙️ Environment Variable Support – Keeps sensitive API keys and passwords secure.

## 🧠Tech Stack
```
Category	            Technology Used
Programming Language	Python 3.x
APIs Used	            OpenWeatherMap API, NewsAPI
Libraries	            requests, smtplib, email.mime, dotenv, pycountry
Automation Tools	    Python Script
Output Format	        Email
```

## 📂Project Structure
```Automated-Data-Aggregator/<br>
├── src/
│   ├── fetch_weather.py        # Handles weather API fetching
│   ├── fetch_news.py           # Fetches top headlines
│   ├── send_email.py           # Sends email notifications
│   ├── main.py                 # Main script integrating everything
│   ├── .env                    # Stores API keys and credentials
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Ignored files
```

## 🔑Environment Variables (.env File)

WEATHER_API_KEY=your_openweatherapi_key

WEATHER_URL=weather_url

LAT_LONG_URL=lat_long_url

NEWS_API_KEY=your_newsapi_key

NEWS_URL=news_url

EMAIL_USER=your_email_id

EMAIL_PASS=your_email_password

## 🧩Installation & Setup
1. Clone the Repository<br>
```
git clone https://github.com/Lakshita-1502/Automated-data-aggregator.git
cd Automated-data-aggregator
```

2. Install Dependencies<br>
```
pip install -r requirements.txt
```

3. Configure Environment Variables<br>
Create a .env file as shown above and fill in your keys.

4. Run the Project<br>
```
python src/main.py
```

## ⚡How It Works

Fetch Weather Data:<br>
Uses the OpenWeatherMap API to get temperature, humidity, and weather conditions.

Fetch News Headlines:<br>
Uses NewsAPI to get top headlines related to the user’s region.

Aggregate and Format:<br>
Merges both sets of data into a clean, readable format.

Send Email:<br>
Uses SMTP protocol (smtplib) to send an email containing the fetched data.

Automate Execution:<br>
Use Windows Task Scheduler or Cron Jobs to run main.py daily.

## 🧾Requirements

Python 3.8+

Internet connection

API keys from:

OpenWeatherMap

NewsAPI

## 🧠Future Enhancements

📆 Add daily/weekly scheduling via built-in Python automation

📱 Add WhatsApp or Telegram message support

🌍 Multi-city support

🧾 Store previous reports in local database (SQLite)
 
🧠 Add AI summary of top headlines

## 🧾Sample Email Output

Subject: Daily weather and news update

🌤 Pune Weather Update<br>
Description:- Overcast clouds<br>
Temperature:- 25.99 °C<br>
Pressure:- 1007 hPa<br>
Humidity:- 71 %<br>
<br>
🗞 Top headlines :-<br>
Starmer meets Modi on his first visit to India<br>
India impress to beat Sri Lanka in World Cup opener<br>
HMD’s Touch 4G is a dumb-smart-phone<br>
<br>
🙏 Thank you for using our service.<br>
<br>
🌤️Have a nice Day!<br>
<br>
Report generated on: Friday, 24 October 2025, 03:01 PM<br>
You’re receiving this automated weather and news summary.<br>
© 2025 Automated Data Aggregator<br>