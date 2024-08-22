import pyttsx3
import os
import speech_recognition as sr
import pyaudio
import openai
import win32com
import webbrowser
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from ecapture import ecapture as ec
import sys
import ctypes
import speech_recognition as speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  !")

    else:
        speak("Good Evening !")

    asname = "lucy 1 point o"
    speak(f"I am your Assistant{asname}")


def username():
    global urname
    speak("What should i call you ?")
    urname = takeCommand()
    speak(f"Welcome {urname} ")
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome ", urname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower()
        sites = [["youtube", "https://youtube.com"], ["google", "www.google.com"], ["hackerrank", "www.hackerrank.com"],
                 ["instagram", "www.instagram.com"]]
        for site in sites:
            if f"open {site[0]}" in query:
                speak(f"Opening {site[0]}")
                webbrowser.open(site[1])
            else:
                pass

        if "how are you" in query:
            speak("I am doing great! how about you")

        elif "what is your name" in query:
            speak("my name is lucy  you can call me park")

        elif "what is my name" in query:
            speak(username())

        elif "lock my system" in query:
            ctypes.windll.user32.LockWorkStation()

        elif "stop" in query:
            sys.exit(0)

        elif "exit" in query:
            exit()

        elif "bye" in query:
            speak("okay bye have a good day")
            exit()

        elif "give me random number" in query:
            num = random.random()
            speak(num)
            print(num)

        elif "say me a joke" in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            speak(My_joke)
            print(My_joke)

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times 
                    of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        elif "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        else:
            pass
