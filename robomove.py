# from robo1 import MyRoboClass as r
import pyttsx3 #for test purpus
import random
from time import sleep
import json
import cv2
mycontrol={}
turncount=0
# while True:
#     try:
#         with open("movement.json","r") as j:
#             mycontrol=json.load(j)
#         if mycontrol["move"]=="go":    
#             if r.multrasonic.distance(2)=="turn":
#                 r.eastmoter.movef(5)
#                 r.westmoter.movef(25)
#                 sleep(0.025)
                
#                 # r.eastmoter.movef()
#                 # r.westmoter.movef()
#                 turncount+=1
#             else:
#                 r.westmoter.movef()
#                 r.eastmoter.movef()
#                 turncount=0
#         elif mycontrol["move"]=="stop":
#             r.westmoter.Stop()
#             r.eastmoter.Stop()
#         elif mycontrol["move"]=="command":
#             cmd=mycontrol["command"]

#             # get access command and fallow it . it will be appended in future
#         if turncount>38:
#             r.engine.say("I Am  In Trap")
#             r.engine.say("Please Give Me side")
#             r.engine.runAndWait()
#     except Exception as e:
#         r.engine.say("error ")
#         r.engine.say(e)
#         r.engine.runAndWait()

engine = pyttsx3.init()
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

count=0
z=0
while True:
    z+=1
    # count=random.randint(0,111110)
    count=5
    if z%40==0:
        count=1
    try:
        with open("movement.json","r") as j:
            mycontrol=json.load(j)
        if mycontrol["move"]=="go":    
            if count % 5==0:
                print("turn left")
                a=[a*a for a in range(0,600)]
                sleep(0.025)
                
                b=[a for a in range(0,200)]
                turncount+=1
            else:
                print("f")
                turncount=0
        elif mycontrol["move"]=="stop":
            print("stop")
            c=[a for a in range(0,200)]
        elif mycontrol["move"]=="command":
            cmd=mycontrol["command"]
            print(cmd)
            d=[a for a in range(0,200)]
            # get access command and fallow it . it will be appended in future
        if turncount>38:
            engine.say("I Am  In A Trap")
            engine.say("Please Give Me side")
            engine.runAndWait()
    except Exception as e:
        engine.say("error ")
        engine.say(e)
        print(e)
        engine.runAndWait()


# ₹ 2500000000000.0
# 2.5 lakh crore
# 1667