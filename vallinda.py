import tkinter as tk
from tkinter import *
import speech_recognition as sr
from win32com.client import Dispatch
import os
import webbrowser
import pyautogui
from pynput.keyboard import Key, Controller
# from PIL import Image, ImageTk
import time

# tkinter controls
root = tk.Tk()
root.title("Sample")
root.geometry("250x400")


def animation():
    time.sleep(0.5)

    time.sleep(0.5)

    time.sleep(0.5)
    p4 = tk.Label(root, text="Listening...", font=("SF Pro", 20)).place(x=50, y=50)


tk.Label(root, text="Listening", font=("SF Pro", 20)).place(x=50, y=50)
animation()
root.mainloop()

# other controls
keyboard = Controller()


def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)


if __name__ == "__main__":
    speak("Hello Sir")

r = sr.Recognizer()

with sr.Microphone(device_index=1) as source:
    def boot():
        speak("Listening ")
        print("Listening....")
        audio = r.listen(source, timeout=4, phrase_time_limit=3)

        try:
            text = r.recognize_google(audio)

        except:
            speak("Can't hear you")
            boot()

        if "ok" in text or "Ok" in text:

            if "how are you" in text:
                speak("I am fine")

            elif "hello" in text:
                speak("Hello Sir")

            elif "open videos" in text:
                speak("opening youtube")

                os.startfile("D:\\python_projects\\youtube.pyw")
                exit()

            elif "open code" in text:
                speak("Opening Visual Studio code")
                os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")

            elif "search for" in text:
                text = text.replace("search for", "")
                text = text.replace("ok", "")
                speak("Searching")
                print("Searching....")
                speak(text)
                webbrowser.open(text)

            elif "who is" in text:
                text = text.replace("who is", "")
                text = text.replace("ok", "")
                speak("Searching")
                print("Searching....")
                speak(text)
                webbrowser.open(text)

            elif "shut down" in text or "bye bye" in text:
                speak("Good bye")
                exit()

            elif "play music" in text or "play songs" in text or "play song" in text:
                music_dir = "D:\\My music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "close window" in text:
                pyautogui.keyDown("alt")
                pyautogui.press("f4")
                pyautogui.keyUp("alt")

            elif "switch window" in text:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")

            elif "what is" in text:
                text = text.replace("what is", "")
                text = text.replace("ok", "")
                speak("Searching")
                print("searching...")
                speak(text)
                webbrowser.open(text)

            elif "install" in text:
                speak("installing module")
                text = text.replace("install", "")
                text = text.replace("ok", "")
                os.startfile("C:\\Windows\\System32\\cmd.exe")
                pyautogui.write(" pip install")
                pyautogui.write(text, interval=0.25)
                pyautogui.press("enter")

            # elif "stop music" in text or "pause music" in text or "stop song" in text or "pause song" in text:
            #     pyautogui.keyDown("fn")
            #     pyautogui.press("f11")
            #     p

            elif "open recent" in text:
                os.startfile("D:\\python_projects\\recents.pyw")
                exit()






        else:
            speak("Can't recognize")
        boot()


    boot()
