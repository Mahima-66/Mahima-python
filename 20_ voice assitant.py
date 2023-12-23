# Importing the required modules
import pyttsx3 # For text to speech conversion
import speech_recognition as sr # For speech recognition
import wikipedia # For accessing wikipedia
import webbrowser # For opening web pages
import time # For getting the current time
import schedule # For scheduling tasks

# Initializing the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Setting the voice to female
engine.setProperty('rate', 120) # Setting the speech rate to 120 words per minute
engine.say("Hi, I am Meera, your voice assistant. How can I help you?")
engine.runAndWait()

# Defining a function to listen to the user's voice and return the text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except:
        print("Sorry, I could not understand that.")
        text = ""
    return text

# Defining a function to respond to the user's query
def respond (text):
    if "hello meera" in text.lower():
        engine.say("Hello, nice talking to you.")
        engine.runAndWait()
        day = listen()
        if "good" in day.lower():
            engine.say("I'm glad to hear that. What made your day good?")
        elif "bad" in day.lower():
            engine.say("I'm sorry to hear that. What happened?")
        else:
            engine.say("you are welcome.")
            engine.runAndWait()
            reason = listen()
            engine.say(f"How are you getting ready to accomplish your objectives?")
            engine.runAndWait()
            objectives = listen()
            engine.say(f"That sounds great. I hope you achieve your goals. Do you need any help from me?")
            engine.runAndWait()
            engine.say("Sorry, I did not get that. ")
            engine.runAndWait()
    
    elif "current time" in text.lower():
        current_time = time.strftime("%I:%M %p")
        engine.say(f"The current time is {current_time}")
        engine.runAndWait()
    elif "wikipedia" in text.lower():
        engine.say("Searching Wikipedia...")
        engine.runAndWait()
        text = text.replace("wikipedia", "")
        results = wikipedia.summary(text, sentences=2)
        engine.say("According to Wikipedia,")
        engine.runAndWait()
        engine.say(results)
        engine.runAndWait()
    elif "youtube" in text.lower():
        engine.say("Opening YouTube...")
        engine.runAndWait()
        webbrowser.open("https://www.youtube.com")
    elif "schedule" in text.lower():
        engine.say("What task do you want to schedule?")
        engine.runAndWait()
        task = listen()
        engine.say("When do you want to schedule it?")
        engine.runAndWait()
        time = listen()
    elif "open a website" in text.lower():
        engine.say("What website do you want to open?")
        engine.runAndWait()
        website=listen()
        # ... code to parse the website and open it ...
        engine.say(f"Opening {website}")
        engine.runAndWait()
    
    elif "goodbye" in text.lower():
        engine.say("Bye, have a nice day.")
        engine.runAndWait()
        exit()
    else:
        engine.say("Sorry, I did not get that. Please try again.")
        engine.runAndWait()

# Running a loop to keep listening and responding
while True:
    text = listen()
    respond(text)