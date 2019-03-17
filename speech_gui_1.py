from tkinter import *
import pyttsx3
import os
import sys
import winspeech
os.chdir("D:\\PYTHON\Speech")
from tkinter import messagebox
winspeech.initialize_recognizer(winspeech.INPROC_RECOGNIZER)

top = Tk()
top.geometry("100x100")

def SpeechRecognized(result,listener):
    print("You said: %s" %result)
    if result == "stop":
	    winspeech.stop_listening()
	    sys.exit(0)



def speech():
    messagebox.showinfo("Start speak", "Stop for termionate")
    listener = winspeech.listen_for_anything(SpeechRecognized)
    while listener.is_listening():
            continue


def tts():
    messagebox.showinfo("Say Hello", "Start TTS")
    engine = pyttsx3.init()
    f=open("speechtext.txt","r")
    ttstxt=f.read()
    engine.say(ttstxt)
    engine.runAndWait()


B1 = Button(top, text = "Say Text to Speech", command = tts)
B1.place(x = 20,y = 10)
B1 = Button(top, text = "Say Speech", command = speech)
B1.place(x = 30,y = 40)
top.mainloop()
