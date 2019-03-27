#!/user/bin/env python3

#this is for python --V 3.6

import time
import speech_recognition as sr
from time import ctime
from gtts import gTTS
import os
import pyttsx3
import sys
import wikipedia

#function for text to speech
def speak(audiostr):
    print(audiostr)
    engine = pyttsx3.init()
    ttstxt=audiostr
    engine.say(ttstxt)
    engine.runAndWait()




#function for Speech Recocognization
def recordAudio():
    
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)
        data=""
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data + '\n')
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request ; {0}".format(e))
    return data


#AI answer by using wikipedia 
def wiki():
    speak("Tell me what topic do you want to know")
    ask=recordAudio()
    speak(wikipedia.summary(ask))




#function for AI assistant
def tahoe(data):

    if 'what is the time' in data :
        speak(ctime())
    elif 'how are you' in data:
        speak("I am fine, Thank you")
    elif 'who are you' in data:
        speak("I am your assistant")
    elif 'what is your name' in data :
        speak("my name is AI Machine")
    elif 'I want to know' in data :
        wiki()
    elif 'thank you' in data :
        speak("welcome")
    else :
        pass


speak("Welcome")
speak("Hello! Sir, I am AI machine")
#function for continuous Speech recognization and AI process
time.sleep(1)
speak("Ask me saying: I want to know")
speak("you can exit from me by saying: EXIT !")
while True:
    data = recordAudio()
    tahoe(data)
    if data == "exit":
        speak("Exit Successfully")
        sys.exit(0)
            
            


