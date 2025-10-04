import speech_recognition as sr
from win32com.client import Dispatch
import os
import webbrowser
import pyautogui
from pynput.keyboard import Key, Controller
import time
import datetime

keyboard = Controller()

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__ == "__main__":
    speak("Loading")
    time.sleep(0.25)

r = sr.Recognizer()

with sr.Microphone() as source:
    def boot():
        speak("Listening ")
        print("Listening....")
        audio = r.listen(source, timeout=6, phrase_time_limit=3)

        try:
            text = r.recognize_google(audio)
            print("You said : ", text)
        except:
            speak("Can't hear you")
            boot()

        if "what is charge" in text:
            speak("Charge is a fundamental property of matter.")
            time.sleep(0.25)
            speak("by virtue of which two bodies")
            time.sleep(0.25)
            speak("either attract or repel")

        elif "charge of electron" in text or "charge on electron" in text:
            speak("Every electron has charge of ")
            time.sleep(0.25)
            speak("minus 1.6 into ")
            speak("10 to the power minus 19")
            speak("Coulomb")

        elif "charge of proton" in text or "charge on proton" in text:
            speak("Every proton has charge of ")
            time.sleep(0.25)
            speak("plus 1.6 into ")
            speak("10 to the power minus 19")
            speak("Coulomb")
        
        elif "property of charges" in text:                    
            speak("First Property")
            speak("Charge is a scalar quantity")
            time.sleep(1)
            speak("Second Property")
            speak("charge is conservative")
            time.sleep(0.5)
            speak("It can neither be created")
            speak(" nor be destroyed")
            time.sleep(1)
            speak("Third Property")
            speak("According to Einstein")
            time.sleep(0.5)
            speak("If any object travels with the speed of light")
            speak(" then mass changes to energy")
            time.sleep(0.5)
            speak("But charge is different")
            speak(" If charge travels with the speed of light")
            speak(" then its mass dont change into energy")
            time.sleep(0.5)
            speak("It is called Invarience of charge")

        elif "goodbye" in text or "bye" in text or "exit" in text:
            speak("have a nice day")
            os.startfile("vallinda_new.py")
            exit()

        elif "method of charging" in text:
            speak("There are three methods of charging")
            time.sleep(1)
            speak("First Method")
            speak("Charging by conduction")
            time.sleep(0.5)
            speak("if touch a charged body with a uncharged body")
            speak(" then sharing of charges take place")
            time.sleep(0.25)
            speak("And uncharged body become charged")
            time.sleep(1)
            speak("Second Method")
            speak("Charging by induction")
            time.sleep(0.5)
            speak("If we bring a charged body near to a uncharged body")
            speak(" And earth the uncharged body")
            time.sleep(0.25)
            speak("Then the uncharged body become charged")
            speak("with the help of earthing and")
            time.sleep(0.25)
            speak("Attraction and Repulsion of charges")
            time.sleep(1)
            speak("Third Method")
            speak("Charging by Friction")

            time.sleep(0.5)
            speak("If we rub any two objects")            
            time.sleep(0.25)
            speak("Due to excess heat")
            speak(" one oject loses electron and other gains it")
            time.sleep(0.25)
            speak(" then both object get charged")

        elif "coulomb law" in text:
            speak("Doctor coulomb says that")
            time.sleep(0.25)
            speak("In an isolated system")
            speak("if two charges are separated by a distance")
            time.sleep(0.25)
            speak(" then the force between them")
            time.sleep(0.25)
            speak("is equals to product of charges")
            speak(" divide by square of distance between them")                             

        elif "value of e not" in text or "value of permitivity" in text or "value of Epsilon Not" in text:
            speak("Epsilon not has value of ")
            time.sleep(0.25)
            speak("eight point eight five ")
            time.sleep(0.25)
            speak("into ten to the power minus 12")
            speak("Newton meter square")
            time.sleep(0.25)
            speak("per coulomb square")

        elif "value of k" in text or "value of K" in text:
            speak("The value of K is")
            time.sleep(0.25)
            speak("nine into")
            speak("10 to the power 9")
            
        elif "concept of super position" in text or "concept of superposition" in text:
            speak("If there are two charges")
            time.sleep(0.25)
            speak("And a third charge bring near them")
            time.sleep(0.25)
            speak(" then position where those two charges will not effect")
            time.sleep(0.25)
            speak("the third charge")

        elif "what is Null point" in text:
            speak("Point where the value of electric field")
            time.sleep(0.25)
            speak("is zero")

        elif "property of electric field" in text:
            speak("First property")
            time.sleep(0.25)
            speak("Electric field lines start from positive to negative")
            time.sleep(0.25)
            speak("But they dont make close loop")
            time.sleep(0.5)
            speak("second property")
            time.sleep(0.25)
            speak("Direction of field lines is found by")
            speak(" drawing tangent at that point")
            time.sleep(0.5)
            speak("Third property")
            time.sleep(0.25)
            speak("Electric field do not intersect each other")
            time.sleep(0.5)
            speak("Forth property")
            time.sleep(0.25)
            speak("Electric field lines are")
            speak(" perpendicular to surfaces")
            time.sleep(0.5)
            speak("Fifth property")
            time.sleep(0.25)
            speak("Electric field lines do not pass through conductors")
            time.sleep(0.5)
            speak("Sixth property")
            time.sleep(0.25)
            speak("The spacing between field lines indicate")
            speak(" the strength of field")                      
                     
                                
        boot()
    boot()
boot()

        
            
