#!/usr/bin/env  python

#   WEATHER APP USING OPENWEATHERMAP API.
#   OPENWEATHERMAP DOCUMENTATION: https://openweathermap.org/api
#   IMPORT ipstack API as a MODULE for current IP location info.
#   it can also be used for looking up geolocation of any IP


import json
import requests
from ipstack import GeoLookup
from tkinter import *

def get_loaction():
    # GET LOCATION  WITH ipstack
    ipstack_API_KEY = "0d08445765516e3fb5265bad0788f891"
    geo_lookup = GeoLookup(ipstack_API_KEY)  # API KEY FOR IPSTACK
    location_info = geo_lookup.get_own_location()
    print(type(location_info))
    data_display.insert(END, json.dumps(location_info, indent=2))   # debug
    get_weather_data(location_info['country_name'])


def get_weather_data(location):

    # data_display.insert(END, "Region: " + location_info['region_name']+", "+location_info['country_name']+"\n ")

    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    openweathermap_API_KEY = "0da443e6847a8634a3cd2103be39cc53"
    URL = baseURL + "q=" + str(location) + "&units=metric" + "&appid=" + openweathermap_API_KEY
    req = requests.get(url=URL)
    data = req.json()
    print(json.dumps(data, indent=4, sort_keys=True))
    data_display.insert(END, json.dumps(data, indent=4, sort_keys=True))       #debug
    data_display.insert(END, "\nWeather: " + str(data['weather'][0]['main']) + "y")
    data_display.insert(END, "\ntemperature: " + str(data['main']['temp']) + " degree Celsius")
    data_display.insert(END, "\nMin temperature: " + str(data['main']['temp_min']) + " degree Celsius")
    data_display.insert(END, "\nMax temperature: " + str(data['main']['temp_max']) + " degree Celsius")



root = Tk()
root.title("Weather App")
root.geometry("720x480")

frame = Frame(root)
frame.pack()

inputFrame = Frame(root, width=100)
inputFrame.pack(side="left")

submitBtn = Button(inputFrame, text="Get Data", command=get_loaction)
submitBtn.pack()

displayFrame = Frame(root)
displayFrame.pack(side="right")

data_display = Text(displayFrame)
data_display.pack()




root.mainloop()

#   {'coord': {'lon': 90.41, 'lat': 23.73},
#   'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50n'}],
#   'base': 'stations',
#   'main': {'temp': 25, 'feels_like': 25.54, 'temp_min': 25, 'temp_max': 25, 'pressure': 1014, 'humidity': 61},
#   'visibility': 4000,
#   'wind': {'speed': 2.6, 'deg': 280},
#   'clouds': {'all': 0},
#   'dt': 1606567715,
#   'sys': {'type': 1, 'id': 9145, 'country': 'BD', 'sunrise': 1606522930, 'sunset': 1606561857},
#   'timezone': 21600,
#   'id': 1185241,
#   'name': 'Paltan',
#   'cod': 200}
