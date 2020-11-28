import pyttsx3
engine = pyttsx3.init()
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("welcome to vlcc salon mahnar")
engine.say("From Baby singh")
engine.runAndWait()
while  True:
    i=input("")
    engine.say(i)
    engine.runAndWait()
    