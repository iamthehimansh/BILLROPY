import json
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
while True:
    try:
        with open("telltext.json","r") as tell:
            mtell=json.load(tell)
            tell.close()
        with open("telltext.json","w")as wtell:
            json.dump({"tell":""},wtell)
            wtell.close()
        if type(mtell["tell"])==str:
            for i in mtell["tell"]:
                engine.say(i)
                engine.runAndWait()
    except KeyboardInterrupt:
        try:
            with open("telltext.json","r") as tell:
                mtell=json.load(tell)
            
            if type(mtell["tell"])==str:
                pass
        except:
            with open("telltext.json","w")as wtell:
                json.dump({"tell":""},wtell)
                wtell.close()
