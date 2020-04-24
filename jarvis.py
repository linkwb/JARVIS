import random
import datetime
import re
import json
import urllib.request
import pyowm
import pyttsx3

owm = pyowm.OWM('7451715cb6e843730e4c2c5c894788cc')
url = 'http://ipinfo.io/json'
response = urllib.request.urlopen(url)
data = json.load(response)
city = data['city']
region = data['region']
observation = owm.weather_at_place(city+','+region)
weather = observation.get_weather()
time = datetime.datetime.now()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)

#initial prompt
print("Hello, Sir. The time is "+time.strftime("%H:%M")+". How can I be of assistance?\n")
engine.say("Hello, Sir. The Time is "+time.strftime("%H:%M")+". How can I be of assistance?")
engine.runAndWait()
prompt = input("> ")

#begin while loop
while "exit" not in prompt:
    
    #time
    if "time" in prompt:
        print("The time is "+time.strftime("%H:%M")+".")
        engine.say("The time is "+time.strftime("%H:%M")+".")
        engine.runAndWait()

        print("How else might I be of assistance, Sir?\n")
        engine.say("How else might I be of assistance, Sir?")
        engine.runAndWait()
        prompt = input("> ")
    
    #date
    elif "date" in prompt:
        print("The date is "+time.strftime("%m-%d-%y")+".")
        engine.say("The date is "+time.strftime("%m-%d-%y")+".")
        engine.runAndWait()

        print("How else might I be of assistance, Sir?\n")
        engine.say("How else might I be of assistance, Sir?")
        engine.runAndWait()
        prompt = input("> ")

    #location
    elif "location" in prompt:
        print("Your current location is "+city+", "+region+".")
        engine.say("Your current location is "+city+", "+region+".")
        engine.runAndWait()

        print("How else might I be of assistance, Sir?\n")
        engine.say("How else might I be of assistance, Sir?")
        engine.runAndWait()
        prompt = input("> ")

    #weather
    elif "weather" in prompt:
        print("The weather in "+city+", "+region+" is "+str(weather.get_temperature('fahrenheit')['temp']) +" degrees Fahrenheit.")
        engine.say("The weather in "+city+", "+region+" is "+str(weather.get_temperature('fahrenheit')['temp'])+" degrees Fahrenheit.")
        engine.runAndWait()

        print("How else might I be of assistance, Sir?\n")
        engine.say("How else might I be of assistance, Sir?")
        engine.runAndWait()
        prompt = input("> ")

    #error
    else:
        print("Sorry, Sir. I seem to be malfunctioning. Please try again.\n")
        prompt = input("> ")
        
print("I'll get back to running calculations, Sir.\n")
engine.say("I'll get back to running calculations, Sir.")
engine.runAndWait()