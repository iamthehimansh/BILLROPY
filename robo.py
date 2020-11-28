# import RTk.GPIO as GPIO
from RTk import GPIO
from robo1 import MyRoboClass as r
from time import sleep
import cv2
while True:
    try:
        if r.multrasonic.distance(2)=="turn":
            r.eastmoter.movef(5)
            r.westmoter.movef(25)
            sleep(0.025)
            r.eastmoter.movef()
            r.westmoter.movef()
        else:
            r.westmoter.movef()
            r.eastmoter.movef()
    except Exception as e:
        r.engine.say("error ")
        r.engine.say(e)
        r.engine.runAndWait()













# Robo coad start Here 
allobstacal={"all":[],"obj1":[(1,1),(2,1)]}
def addobstracal(name,locatin):
    pass
def addobjbyleanth_width(data):
    l=data[0] # [((num,alphabet_no)),((num,alphabet_no))]
    w=[1] # [((num,alphabet_no)),((num,alphabet_no))]
    mdatadicy={"data":[]}
    lr_start=l[0][0][0]
    lr_stop=l[0][1][0]
    lkey=l[0][0][1]
    for i in range(lr_start,lr_stop):
        try:
            patsay=mdatadicy["data"].index((i,lkey),0,len(mdatadicy["data"]))
        except ValueError :
            patsay=None
        if patsay==None:
            mdatadicy["data"].append((i,lkey))

def addobjasobs(name,data):

    # data formet data=[[((num,alphabet_no)),((num,alphabet_no))],[((num,alphabet_no)),((num,alphabet_no))]]
    addobjbyleanth_width(data)



# All AI  Goes Here

