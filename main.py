from command import Command
from executor import Executor
import re
import threading
import utils
import pyttsx3
import speech_recognition as sr


def speak(audio):
    print("Bot: ", audio)
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[1].id)

    # Method for the speaking of the the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    print("Recognizer check")
    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print("Microphone check")

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
        print("I Can hear")

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language = 'en-US')
            print("You:", Query)

        except Exception as e:
            speak("Please say that again")
            return takeCommand()


        return Query

if __name__ == "__main__":
    # The below is just an example, there will be voice interaction instead soon
    _x = input("Would you like voice interaction or text interaction?\n")
    print("Hello, am eric!")
    while True:
      if bool(re.match("text(?: interaction|)(?: please|)", _x, flags = re.IGNORECASE)):
        cmd = input()
        print("\n" + Executor(Command(cmd)).response)
        if cmd.lower() in ["adios", "goodbye", "bye", "cya"]:
          print("See you next time!")
          break
        
      else:
        cmd = takeCommand()
        resp = Executor(Command(cmd)).response
        print("\n" + resp)
        speak(resp)
        if cmd.lower() in ["adios", "goodbye", "bye", "cya"]:
          speak("See you next time!")
          break
      
        