
import requests
from rich import print
from datetime import datetime

def welcome_message():
  """This displays welcome message"""
  print("[bold purple]Welcome to my weather app🌤️[/bold purple]\n") 
  

def display_temperature(day, temperature, unit="C"):
  """Displays a temperature with day"""
  print(f"[bold purple]{day}: [/bold purple][bold yellow]{round(temperature)}º{unit}[/bold yellow]")


def display_current_weather(city):
  """Displays current weather"""
  api_key = "b125a59f9afa4ebc141352te1ao60a9c"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

  response = requests.get(api_url)
  weather = response.json()
  
  temperature = weather["temperature"]["current"]
  city = weather["city"]
  display_temperature(day="Today" f" in {city}", temperature=temperature)



def display_weather_forecast(city):
  """Displays weather forecast"""
  api_key = "b125a59f9afa4ebc141352te1ao60a9c"
  api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}"

  response = requests.get(api_url)
  weather_forecast = response.json()
  print("\n[bold green]Forecast:[/bold green]")
  
  for day in weather_forecast["daily"]:
    date_stamps = day["time"]
    forecast = datetime.fromtimestamp(date_stamps)
    current_date = forecast.strftime("%A")
    temperature = day['temperature']['day']

    if forecast.date() != datetime.today().date():
      display_temperature(current_date, temperature)
  


def display_credit(name):
  """Displays credit message"""
  print(f"\n\n\n\n[bold white]This app was built by {name} [/bold white]")


welcome_message()
city_name = input("Enter a city: ").strip()
print("")
if city_name:
  display_current_weather(city_name)
  display_weather_forecast(city_name)
  display_credit("Charity Orhoridiohwo")
else:
  print("⚠️ ⚠️ Please enter a valid city name!")
  display_credit("Charity Orhoridiohwo")

