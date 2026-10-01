from pyowm import OWM 
from pyowm.utils import config
from pyowm.utils import timestamps
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Access variables
OWM_API_KEY = os.getenv('OWM_API_KEY')
# print(OWM_API_KEY)
owm = OWM(OWM_API_KEY)
mgr = owm.weather_manager()

observation = mgr.weather_at_place('London,GB')
w = observation.weather
print(w.detailed_status)
print(w.wind())
print(w.humidity)
print(w.temperature('celsius'))
print(w.rain)
print(w.heat_index)
print(w.clouds)

# forecast = mgr.forecast_at_place('Milan,IT','daily')
# answer=forecast.will_be_clear_at(timestamps.tomorrow())