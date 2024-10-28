import os
from dotenv import load_dotenv, dotenv_values
import requests
from twilio.rest import Client

load_dotenv()

api = os.environ.get("WEATHER_API")
city = os.environ.get("CITY")
account_sid = os.environ.get("TWILIO_ACC_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
ph1 = os.environ.get("PERSON_PH_NO")
ph2 = os.environ.get("TRIAL_PH_NO")

url= f"https://api.weatherapi.com/v1/forecast.json?key={api}&q={city}&days=2&aqi=no&alerts=no"
response = requests.get(url)
data = response.json()


if data['forecast']['forecastday'][1]['day']['daily_will_it_rain']:
    msg1 = "Tomorrow go with an umbrella mate....!"
    msg = msg1+ f"Possiblilty of rain is {data['forecast']['forecastday'][1]['day']['daily_chance_of_rain']}%"
    client = Client(account_sid, auth_token)

    m = client.api.account.messages.create(
        to="",
        from_="",
        body= msg)
# else:
#     print("No, there is no rain")
print(m.status)
