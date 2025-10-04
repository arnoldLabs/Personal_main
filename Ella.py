import speech_recognition as sr
from win32com.client import Dispatch
import os
import webbrowser
import pyautogui
import time
from playsound import playsound

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__ == "__main__":
    print("Hey Boss")

r = sr.Recognizer()

with sr.Microphone() as source:
    def boot():
        playsound("beep.mp3")    
        audio = r.listen(source, phrase_time_limit = 5)

        try:
            text = r.recognize_google(audio)
            print("You said : ", text)
        except:            
            boot()

        if "Prakash" in text or "prakash":
            os.startfile("vallinda_new.py")
            exit()
                
        else:            
            boot()
        boot()
    boot()
        
            


        

        
