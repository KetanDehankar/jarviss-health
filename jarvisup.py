# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:09:40 2021

@author: Keytan
"""

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
from plyer import notification




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sunita mam. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        print("Say that again please...")  
        return "None"
    return query

       
        
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'search doctor' in query:
            webbrowser.open("doctor.com")
            
        elif 'search medicine' in query:
            webbrowser.open("netmeds.com")

        elif 'calories' in query:
            webbrowser.open('calorie calculator.com')
        
        elif  'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("jarvis","")
            speak("You tell me to remind you that :"+rememberMsg)
            remember = open('data.txt', 'w')
            remember.write(rememberMsg)
            remember.close()
            
        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            speak("you tell me that"+remember.read())


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'alarm' in query:
            speak("Enter the time !")
            time = input (": Enter the time :")
            
            
            while True:
                Time_AC = datetime.datetime.now()
                now = Time_AC.strftime("%H:%M:%S")
                
                if now == time:
                    speak("Time to wake up sunita mam!")
                    playsound('Hey Ram - Hey Ram.mp3')
                    speak("alarm closed")
                elif now>time:
                    break

            
        else:
          speak("Sorry sunita mam, i am not able to do it")
      
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water now",
            message = "Please drink water sunita mam, your body needs 2.7 litres water for healthy life.",
            app_icon = "C:\\Users\\Keytan\\Desktop\\jarvis\\Iconsmind-Outline-Glass-Water.ico",
            timeout=10
          
            )
            #time.sleep(60*60)
    
