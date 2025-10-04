from AppOpener import open as op
import speech_recognition as sr
from win32com.client import Dispatch
from playsound import playsound

import os
import webbrowser
import pyautogui
import time
import random


def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)


if __name__ == "__main__":
    print('''project 6798 : Voice_automation_assistant [h9bi6l96]
Subject [Lily] --status(Completed)
All clear [System Secure]

************************ WELCOME BOSS ***************************''')

    speak("Welcome Boss")

r = sr.Recognizer()

with sr.Microphone() as source:
    while True:

        # playsound("beep.mp3")
        audio = r.listen(source, phrase_time_limit=3)

        try:
            text = r.recognize_google(audio)
            print("You said : ", text)
        except Exception as e:
            print(f'Error occurred :: {e}')
            continue

        func_1 = ["I am good, as my all functions working properly", "I am enjoying this day", "I am good",
                  "Really fine", "I am fine", "Smiling like always"]
        func_2 = ["Checking your whatsapp messages", "Rolling the notifications", "i am receiving updates on whatsapp",
                  "Give me a second"]
        func_3 = ["Its time to have fun", "Lets chill together", "here we go", "Let's have fun"]
        func_4 = ["My pleasure", "Always with you sir", "you are welcome", "have a nice day sir", "See you soon",
                  "Goodbye", "keep smiling"]
        func_5 = ["Let's get to work", "loading your workspace", "Here you are", "Moving to your workspace"]
        func_6 = ["playing your favourite songs", "Listen your liked songs", "here are your favourite one's",
                  "playing music"]

        if "how are you" in text:
            speak(random.choice(func_1))

        elif "Youtube" in text or "youtube" in text or "YouTube" in text:
            speak("Opening You tube")
            op("Youtube")

        elif "who are you" in text or "tell me about yourself" in text or "introduce yourself" in text:
            speak("Myself Zaar")
            speak("A personal assistant")
            speak("I am a updated version of Vellinda")
            speak("You are running my beta version")
            speak("My creator is Mr. Arnold")
            speak("Nice to meet you")

        elif "code" in text:
            speak("Opening Visual Studio code")
            op("Visual Studio Code")

        elif "search for" in text:
            text = text.replace("search for", "")

            speak("Searching")
            print("Lily : Searching....")
            speak(text)
            webbrowser.open(text)

        elif "messages" in text:
            speak(random.choice(func_2))
            op("WhatsApp")

        elif "thank you" in text or "good bye" in text or "goodbye" in text:
            speak(random.choice(func_4))
            os.startfile("Ella.py")
            exit()

        elif "who is" in text:
            text = text.replace("who is", "")

            speak("Searching for ")
            speak(text)
            print("Lily : Searching....")
            webbrowser.Chrome(text)

        elif "my text book" in text or "my textbook" in text:
            os.startfile("My_Textbook.py")
            exit()

        elif "play music" in text or "play songs" in text or "play song" in text:
            speak(random.choice(func_6))
            op("spotify")
            time.sleep(3)
            pyautogui.press("playpause")

        elif "type" in text:
            text = text.replace("type", "")
            pyautogui.write(text, 0.15)

        elif "next" in text:
            pyautogui.press("nexttrack")

        elif "resume" in text or "stop" in text:
            pyautogui.press("playpause")

        elif "previous" in text:
            pyautogui.press("prevtrack")
            pyautogui.press("prevtrack")

        elif "play" in text:
            text = text.replace("play", "")
            open("spotify")
            time.sleep(5)
            pyautogui.keyDown("ctrl")
            pyautogui.press("l")
            pyautogui.keyUp("ctrl")
            time.sleep(0.5)
            pyautogui.typewrite(text, 0.25)
            pyautogui.press("enter")
            time.sleep(0.25)
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("enter")

        elif "volume up" in text:
            def chalu():
                for i in range(1, 11):
                    pyautogui.press("volumeup")


            chalu()

        elif "volume down" in text:
            def band():
                for i in range(1, 11):
                    pyautogui.press("volumedown")


            band()

        elif "files" in text:
            pyautogui.keyDown("win")
            pyautogui.press("e")
            pyautogui.keyUp("win")

        elif "silent" in text or "mute" in text:
            pyautogui.press("volumemute")

        elif "Unmute" in text:
            pyautogui.press("volumemute")

        elif "pause" in text or "stop" in text:
            pyautogui.press("playpause")

        elif "close" in text:
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            pyautogui.keyUp("alt")

        elif "switch" in text:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif "minimise" in text:
            pyautogui.keyDown("win")
            pyautogui.press("m")
            pyautogui.keyUp("win")

        elif "what is" in text:
            text = text.replace("what is", "")

            speak("Searching for ")
            speak(text)
            print("Lily : Searching...")
            webbrowser.open(text)

        elif "install" in text:
            speak("installing module")
            text = text.replace("install", "")

            os.startfile("C:\\Windows\\System32\\cmd.exe")
            time.sleep(0.5)
            pyautogui.write(" pip install")
            pyautogui.write(text, 0.25)
            pyautogui.press("enter")

        # elif "recent" in text:
        # os.startfile("D:\\python_projects\\recents.pyw")
        # exit()

        else:
            continue

