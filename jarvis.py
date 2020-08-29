import datetime
import json
import urllib.request
import pyowm
import pyttsx3
import speech_recognition as sr

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
r = sr.Recognizer()
mic = sr.Microphone()


def recognize_speech_from_mic(r, mic):
    if not isinstance(r, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with mic as source:
        print("Speak:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = r.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


# initial prompt
print("Hello, William. The time is "+time.strftime("%H:%M")+". How can I be of assistance?\n")
engine.say("Hello, William. The Time is "+time.strftime("%H:%M")+". How can I be of assistance?")
engine.runAndWait()
speech = recognize_speech_from_mic(r, mic)
prompt = speech["transcription"]

# begin while loop
while "shut down" not in prompt:
    
    # time
    if "time" in prompt:
        print("The time is "+time.strftime("%H:%M")+".")
        engine.say("The time is "+time.strftime("%H:%M")+".")
        engine.runAndWait()

        print("How else might I be of assistance?\n")
        engine.say("How else might I be of assistance?")
        engine.runAndWait()
        speech = recognize_speech_from_mic(r, mic)
        prompt = speech["transcription"]

    # date
    elif "date" in prompt:
        print("The date is "+time.strftime("%m-%d-%y")+".")
        engine.say("The date is "+time.strftime("%m-%d-%y")+".")
        engine.runAndWait()

        print("How else might I be of assistance?\n")
        engine.say("How else might I be of assistance?")
        engine.runAndWait()
        speech = recognize_speech_from_mic(r, mic)
        prompt = speech["transcription"]

    # location
    elif "location" in prompt:
        print("Your current location is "+city+", "+region+".")
        engine.say("Your current location is "+city+", "+region+".")
        engine.runAndWait()

        print("How else might I be of assistance?\n")
        engine.say("How else might I be of assistance?")
        engine.runAndWait()
        speech = recognize_speech_from_mic(r, mic)
        prompt = speech["transcription"]

    # weather
    elif "weather" in prompt:
        print("The weather in " + city + ", " + region + " is " + str(weather.get_temperature('fahrenheit')['temp']) + " degrees Fahrenheit.")
        engine.say("The weather in " + city + ", " + region + " is " + str(weather.get_temperature('fahrenheit')['temp']) + " degrees Fahrenheit.")
        engine.runAndWait()

        print("How else might I be of assistance?\n")
        engine.say("How else might I be of assistance?")
        engine.runAndWait()
        speech = recognize_speech_from_mic(r, mic)
        prompt = speech["transcription"]

    # error
    else:
        print("Sorry. I seem to be malfunctioning. What was that?\n")
        engine.say("Sorry. I seem to be malfunctioning. What was that?\n")
        engine.runAndWait()

        speech = recognize_speech_from_mic(r, mic)
        prompt = speech["transcription"]

print("I'll get back to running calculations, Sir.\n")
engine.say("I'll get back to running calculations.")
engine.runAndWait()
