#!/usr/bin/env  python

#   WEATHER APP USING OPENWEATHERMAP API.
#   OPENWEATHERMAP DOCUMENTATION: https://openweathermap.org/api
#   IMPORT ipstack API as a MODULE for current IP location info.
#   it can also be used for looking up geolocation of any IP


import json
import requests
from ipstack import GeoLookup
from tkinter import *

#
# class WeatherApp(Frame):
#     def

def get_weather_data():
    # GET LOCATION  WITH ipstack
    ipstack_API_KEY = "0d08445765516e3fb5265bad0788f891"
    geo_lookup = GeoLookup(ipstack_API_KEY)  # API KEY FOR IPSTACK
    location_info = geo_lookup.get_own_location()
    print("Location Info: \n")
    for items in location_info:
        print(items)

    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    openweathermap_API_KEY = "0da443e6847a8634a3cd2103be39cc53"
    URL = baseURL + "q=" + str(geo_lookup.get_own_location()['city']) + "&appid=" + openweathermap_API_KEY
    req = requests.get(url=URL)
    data = req.json()
    print("\n\nKeys: ")
    for keys in data:
        print(keys)


root = Tk()
root.title("Weather App")
root.geometry("720x480")

inputFrame = Frame(root, bg="red", width=200)
inputFrame.pack()
submitBtn = Button(inputFrame, text="Get Data", command=get_weather_data)
submitBtn.pack(side="left")


root.mainloop()
