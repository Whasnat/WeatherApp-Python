#!/usr/bin/env  python

#   WEATHER APP USING OPEN-WEATHER-MAP API.
#   OPEN-WEATHER-MAP DOCUMENTATION: https://openweathermap.org/api
#   IMPORT ipstack API as a MODULE for current IP location info.
#   IPSTACK can also be used for looking up geolocation of any IP


from ipstack import GeoLookup
from tkinter import *
import requests
import json

import time



# GET LOCATION INFO
def get_location():
    ipstack_API_KEY = "0d08445765516e3fb5265bad0788f891"    # MY IPSTACK API_KEY
    geo_lookup = GeoLookup(ipstack_API_KEY)     # GEO LOOK-UP INSTANCE
    city_name = city_nameInput.get()

    # GET DEVICE_IP LOCATION
    location_info = geo_lookup.get_own_location()

    if city_name == "":

        print(type(location_info))
        print(json.dumps(location_info, indent=2))
        # data_display.insert(END, json.dumps(location_info, indent=2))  # debug
        data_display.insert(END,
                            "Region: " + location_info['region_name'] + ", " + location_info['country_name'] + "\n")
        get_weather_data(location_info['city'])

    else:
        get_weather_data(location_info)


# GET WEATHER DATA
def get_weather_data(location):
    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    openweathermap_API_KEY = "0da443e6847a8634a3cd2103be39cc53"
    URL = baseURL + "q=" + str(location) + "&units=metric" + "&appid=" + openweathermap_API_KEY
    req = requests.get(url=URL)
    data = req.json()
    print("\n\n\n")
    print(type(data))
    print(json.dumps(data, indent=4, sort_keys=True))

    # data_display.insert(END, json.dumps(data, indent=4, sort_keys=True))       #debug

    data_display.insert(END, "\nWeather: " + str(data['weather'][0]['main']) + "y")
    if temperature.get():
        data_display.insert(END, "\ntemperature: " + str(data['main']['temp']) + " degree Celsius")
        data_display.insert(END, "\nMin temperature: " + str(data['main']['temp_min']) + " degree Celsius")
        data_display.insert(END, "\nMax temperature: " + str(data['main']['temp_max']) + " degree Celsius")

    if wind.get():
        wind_speed = ((data['wind']['speed'])*5)/18
        print(type(wind_speed))
        data_display.insert(END, f"\nWind speed: {wind_speed} km/h")

    if lat_long.get():
        location = "\nLatitude: " + str(data['coord']['lat']) + "\nLongitude: " + str(data['coord']['lon'])
        data_display.insert(END, location)

    # TIME STAMP FROM WEATHER DATA
    time_stamp = (data['sys']['sunrise'])
    data_display.insert(END,
                        "\nSunrise: " + time.strftime("%D %H:%M", time.localtime(time_stamp)))     # CONVERT TO LOCALTIME


def get_daily_weather_data():
    pass


# DEFINE ROOT AND MAIN-FRAME
root = Tk()
root.title("Weather App")
root.geometry("720x480")
frame = Frame(root)
frame.pack()


# INPUT FRAME FOR USER ENTRY AND BUTTONS
inputFrame = Frame(frame, width=100)
inputFrame.pack(side="left")

# GET USER INPUT
cityNameVar = StringVar()
city_nameInput = Entry(inputFrame, textvariable=cityNameVar)
city_nameInput.grid(row=0, column=0, sticky=W)
# city_nameInput.pack(side="right")

# CHECK BOXES
temperature = IntVar()
Checkbutton(inputFrame, text="temp", variable=temperature).grid(row=0, column=1, sticky=W)
wind = IntVar()
Checkbutton(inputFrame, text="wind", variable=wind).grid(row=0, column=2, sticky=W)
lat_long = IntVar()
Checkbutton(inputFrame, text="location", variable=lat_long).grid(row=0, column=3, sticky=W)

# GET DATA BUTTON
submitBtn = Button(inputFrame, text="Get Data", command=get_location)
submitBtn.grid(row=1, column=0, sticky=W)
# submitBtn.pack(side="left")

# TEXT WIDGET
displayFrame = Frame(frame)
displayFrame.pack(side="right")
data_display = Text(displayFrame)
data_display.pack()

root.mainloop()
