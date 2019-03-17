#python 2.7
#
#

import speech_recognition as sr
from time import ctime
import time
import os
import pyttsx3
os.chdir("D:\PYTHON\Speech") 
data=""

def speak(audiostr):
    print(audiostr)
    engine = pyttsx3.init()
    ttstxt=audiostr
    engine.say(ttstxt)
    engine.runAndWait()




def recordAudio():
# Record Audio
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   

    try:
        data = r.recognize_google(audio)
        print('You said: ' + data + '\n') 
    except sr.UnknownValueError:
        print("Could not understand audio")
        data = recordAudio();
#    except sr.RequestError as e:
#        print("Could not request results; {0}".format(e))
    return data




def tahoe(data):

    if 'what is the time' in data :
        speak(ctime())
    elif 'how are you' in data:
        speak("I am fine")
    elif 'who are you' in data:
        speak("I am tahoe")
    else :
        pass



time.sleep(2)

speak("Hi Sayed, what can I do for you?")
while 1:
    data = recordAudio()
    tahoe(data)



