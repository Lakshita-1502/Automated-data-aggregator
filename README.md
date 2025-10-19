🌦️ Automated Data Aggregator

An automation-based Python project that fetches real-time weather details and top news headlines for a given city, and automatically sends them via email notifications to users.

This project demonstrates the integration of multiple APIs, automation, and email delivery — ideal for productivity, daily updates, and smart information aggregation.

🚀 Features

🌤 Real-time Weather Fetching – Gets the latest temperature, humidity, and weather conditions for a user-specified city.

🗞️ Top Headlines Aggregation – Fetches current top news headlines for that region or globally.

📧 Automated Email Delivery – Sends the aggregated data directly to the user’s email inbox.

⚙️ Environment Variable Support – Keeps sensitive API keys and passwords secure.

🕒 Scheduled Execution (Optional) – Can be automated using Task Scheduler (Windows) or Cron (Linux/macOS).

🧠 Tech Stack
Category	            Technology Used
Programming Language	Python 3.x
APIs Used	            OpenWeatherMap API, NewsAPI
Libraries	            requests, smtplib, email.mime, dotenv, json
Automation Tools	    Python Script / Cron Job / Task Scheduler
Output Format	        Email (HTML/Text)

📂 Project Structure
Automated-Data-Aggregator/
├── src/
│   ├── weather_fetcher.py      # Handles weather API fetching
│   ├── news_fetcher.py         # Fetches top headlines
│   ├── email_sender.py         # Sends email notifications
│   ├── main.py                 # Main script integrating everything
│   ├── .env                    # Stores API keys and credentials
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Ignored files (e.g., __pycache__, .env)

🔑 Environment Variables (.env File)

Create a .env file in the src/ folder and add the following:

OPENWEATHER_API_KEY=your_openweather_api_key
NEWS_API_KEY=your_newsapi_key
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

🧩 Installation & Setup
1. Clone the Repository
git clone https://github.com/Lakshita-1502/Automated-data-aggregator.git
cd Automated-data-aggregator

2. Install Dependencies
pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file as shown above and fill in your keys.

4. Run the Project
python src/main.py

⚡ How It Works

Fetch Weather Data:
Uses the OpenWeatherMap API to get temperature, humidity, and weather conditions.

Fetch News Headlines:
Uses NewsAPI to get top headlines related to the user’s region.

Aggregate and Format:
Merges both sets of data into a clean, readable format.

Send Email:
Uses SMTP protocol (smtplib) to send an email containing the fetched data.

Automate Execution:
Use Windows Task Scheduler or Cron Jobs to run main.py daily.

🧾 Requirements

Python 3.8+

Internet connection

API keys from:

OpenWeatherMap

NewsAPI

🧠 Future Enhancements

📆 Add daily/weekly scheduling via built-in Python automation

📱 Add WhatsApp or Telegram message support

🌍 Multi-city support

🧾 Store previous reports in local database (SQLite)

🧠 Add AI summary of top headlines

