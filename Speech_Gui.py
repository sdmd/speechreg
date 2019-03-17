#this is for python --V 2.7
#pip install SpeechRecognition
#pip install pyttsx3

#import time

import speech_recognition as sr
from time import ctime

import os
import pyttsx3
import sys

import Tkinter
import tkMessageBox

os.chdir("D:\\PYTHON\Speech")

top = Tkinter.Tk()
top.minsize(300,100)
top.geometry("300x100")


#function for text to speech
def speak(audiostr):
    print(audiostr)
    engine = pyttsx3.init()
    ttstxt=audiostr
    engine.say(ttstxt)
    engine.runAndWait()
    

#function for TTS
def Mytts():
    engine = pyttsx3.init()
    fl=open("speechtext.txt","r")
    ttstxt=fl.read()
    engine.say(ttstxt)
    engine.runAndWait()
    fl.close()




#function for Speech Recocognization
def recordAudio():
    
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   
        f=open("speechto.txt","a+")
        data=""
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data + '\n')
        f.write(data+'\n')
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request ; {0}".format(e))

    finally :
        f.close()
    return data



#function for voice assistant
def tahoe(data):

    if 'what is the time' in data :
        speak(ctime())
    elif 'how are you' in data:
        speak("I am fine")
    elif 'who are you' in data:
        speak("I am tahoe")
    elif 'open my' in data:
        Mytts();
    else :
        pass


speak("Welcome")
speak("Please select option from the box")

#function for continuous Speech recognization process
def start():
    time.sleep(2)
    speak("Hello! Sir, I can recognize your speech")
    while True:
        data = recordAudio()
        tahoe(data)
        if data == "exit":
            speak("Exit Successfully")
            top.destroy()
            sys.exit(0)
            
            

B1 = Tkinter.Button(top, text = "Text to Speech", command = Mytts)
B1.place(x = 100,y = 10)
B2 = Tkinter.Button(top, text = "Speech Recognition", command = start)
B2.place(x = 85,y = 40)
top.mainloop()

