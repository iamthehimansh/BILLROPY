from RTk import GPIO
# from testclass import test
from time import sleep
import playsound
import time
import json
import pyttsx3
from tkinter import *
engine = pyttsx3.init()
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
GPIO.setmode(GPIO.BCM)
speedofmoter=0
l_of_box=100
w_of_box=100
# moter 1
in1A = 24
in2A = 23
enA = 25
# moter 2
in1B = 3
in2B = 2
enB = 1
# ultrasonic 1
TRIG=7
ECHO=8
# robo global
forward=True
c_speed=0
mydir="N"
mycoo=[1,1]
goinginx=False
goinginy=False
with open("obj.json","r") as objdata:
    objdict=json.load(objdata)

class ultrasonic:
    def __init__(self,TRIG,ECHO):
        self.TRIG=TRIG
        self.ECHO=ECHO
        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)
        GPIO.output(self.TRIG, False)
    def startprocess(self):
        GPIO.output(self.TRIG, True)
        sleep(0.00001)
        GPIO.output(self.TRIG, False)
        while GPIO.input(self.ECHO)==0:
            starttime=time.time()
        while GPIO.input(self.ECHO)==1:
            stoptime=time.time()
            if stoptime-starttime > l_of_box/speedofmoter:
                lol=False
                break
        if lol!= False:
            d_cm=(stoptime-starttime)*34300
            if d_cm > l_of_box:
                return  "go"
            else:
                # if goinginx==True:
                #     objfinded(objco=[mycoo[0]+1,mycoo[1]])
                # elif goinginy==True:
                #     objfinded(objco=[mycoo[0],mycoo[1]+1])
                return "wait"
        else:
            return "go"
    def distance(self,a=1):
        GPIO.output(self.TRIG, False)
        GPIO.output(self.TRIG, True)
        sleep(0.00001)
        GPIO.output(self.TRIG, False)
        while GPIO.input(self.ECHO)==0:
            starttime=time.time()
        while GPIO.input(self.ECHO)==1:
            stoptime=time.time()
            d_cm=(stoptime-starttime)*34300
            if d_cm>20:
                break
        if a==1:
            return d_cm
        elif a==2:
            if d_cm>19:
                return "go"
            else:
                return "turn"
multrasonic = ultrasonic(TRIG,ECHO) 
class Moter:
    def __init__(self,Ena,in1,in2):
        # in1= input 1 forward
        # in2=input 2 backward
        self.Ena=Ena
        self.in1=in1
        self.in2=in2
        
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.Ena,GPIO.OUT)
        self.p=GPIO.PWM(Ena,1000)
    def movef(self,s=30):
        self.p.ChangeDutyCycle(s)
        # GPIO.PWM(self.Ena,1000).ChangeDutyCycle(s)
        GPIO.output(self.in1,True)
        GPIO.output(self.in2,False)
    def ChangeSpeed(self,s=30):
        self.p.ChangeDutyCycle(s)
       
    def Stop(self):
        GPIO.output(self.in1,False)
        GPIO.output(self.in2,False)
        self.p.ChangeDutyCycle(0)
    def moveB(self,s=30):
        self.p.ChangeDutyCycle(s)
        GPIO.output(self.in1,False)
        GPIO.output(self.in2,True)

class gui:
    def __init__(self):
        self.root = Tk()
        c_speed==0
        eastmoter.Stop()
        westmoter.Stop()
        quitbtn = Button(self.root, text="Quit",command=self.root.destroy)
        quitbtn.grid(row=0,column=2)



        upbtn = Button(self.root, text="Up",command=commandup)
        upbtn.grid(row=2,column=2)

        leftbtn = Button(self.root, text="Left",command=commandleft)
        leftbtn.grid(row=3,column=1)

        stpobtn = Button(self.root, text="stop",command=commandstop)
        stpobtn.grid(row=3,column=2)

        rightbtn = Button(self.root, text="Right",command=commandright)
        rightbtn.grid(row=3,column=3)

        downbtn = Button(self.root, text="Down",command=commanddown)
        downbtn.grid(row=4,column=2)
        def Quitme(a=None):
            self.root.destroy()
        self.root.bind("<w>", commandup)
        self.root.bind("<s>", commanddown)
        self.root.bind("<d>", commandright)
        self.root.bind("<a>", commandleft)
        self.root.bind("<space>", commandstop)
        self.root.bind("<z>", commandstop)
        self.root.bind("<q>", Quitme)

        self.root.bind("<W>", commandup)
        self.root.bind("<S>", commanddown)
        self.root.bind("<D>", commandright)
        self.root.bind("<A>", commandleft)
        self.root.bind("<Z>", commandstop)
        self.root.bind("<Q>", Quitme)
        def printhimansh(a=NONE):
            print("HIMANSH")
            engine.say("Himansh")
            engine.say("Jai  Himansh")
            engine.say("One Two Three")
            engine.say("One, Two, Three")
            engine.runAndWait()
        self.root.bind("<H><I><M><A><N><S><H>",printhimansh )
        self.root.bind("<h><i><m><a><n><s><h>",printhimansh )
        # root.bind("<space>",printhimansh )

        self.root.bind("<Up>", commandup)
        self.root.bind("<Down>", commanddown)
        self.root.bind("<Right>", commandright)
        self.root.bind("<Left>", commandleft)
        self.root.mainloop()
westmoter=Moter(enA,in1A,in2A)
eastmoter=Moter(enB,in1B,in2B)
timeto360deg=90
class funck:
    def __init__(self):
        pass
    def getdir(self,mycoodin,target,coodinate,goto):
        if coodinate.lower()=="y":
            if mycoodin[1]-target[1]==1:
                return "N"
            elif mycoodin[1]-target[1]==-1:
                return "S"
            else:
                return False
        elif coodinate.lower()=="x":
            if mycoodin[0]-target[0]==1:
                return "E"
            elif mycoodin[0]-target[0]==-1:
                return "W"
            else:
                return False
        else:
            return False
    
    def turndirandgo(self,targetdir,maintarget):
        turndir(mydir,targetdir)
        d=maintarget*l_of_box
        t=speedofmoter/d
        t1=time.time()
        subtime=0
        while True:
            t2=time.time()-t1-subtime 
            if multrasonic.startprocess()=="go":
                if t2 < t:
                    westmoter.movef(100)
                    eastmoter.movef(100)
                else:
                    break
            else:
                westmoter.moveB(5)
                eastmoter.moveB(5)
                westmoter.Stop()
                eastmoter.Stop()
                
                engine.say("plz give me side ") 

                engine.runAndWait()
                playsound.playsound(r'C:\Users\IamTheHimansh\Documents\BILLROPY\gotext.wav')
                subtime+=t2-time.time()

        

def dirtoangle(dir):
    alldirtoangledict={
    "N-N":[0,0],
    "S-S":[0,0],
    "E-E":[0,0],
    "W-W":[0,0],
    "N-S":[180,-180],
    "N-E":[90,-270],
    "N-W":[270,-90],
    "E-S":[90,-270],
    "E-N":[270,-90],
    "E-W":[180,-180],
    "W-S":[170,-90],
    "W-E":[180,-180],
    "W-N":[90,-270]
    }
    try:

        return alldirtoangledict[dir]
    except ValueError:
        return False
def turnx(angle):
    if type(angle)==list:
        r_angle=min(angle[0],angle[1]*(-1)) 
        if r_angle==angle[0]:
            eastmoter.Stop()
            westmoter.movef()
            sleep(timeto360deg/r_angle) 
        else:
            eastmoter.movef()
            westmoter.Stop()
            sleep(timeto360deg/r_angle)
    elif type(angle)==int or type(angle)==float:
        if angle>0:
            eastmoter.Stop()
            westmoter.movef()
            sleep(timeto360deg/angle)
        else:
            eastmoter.movef()
            westmoter.Stop()
            sleep(timeto360deg/angle*(-1))
def turndir(mydir,targetdir):
    if targetdir!=False:
        angle=dirtoangle(mydir+"-"+targetdir)
        if angle!= False:
            turnx(angle)
            mydir=targetdir
    else:
        print("wrong target diriction")
def rungui():
    mygui=gui()
# command gui

def commandup(a=None):

    if forward==True or forward==None:
        if forward==None:
            c_speed=0
        c_speed=c_speed+10
        if c_speed>100:
            c_speed=100
        westmoter.movef(c_speed)
        eastmoter.movef(c_speed)
        forward=True
    elif forward==False:
        c_speed=c_speed-10
        if c_speed<0:
            c_speed=0
        if c_speed==0:
            westmoter.Stop()
            eastmoter.Stop()
            forward=None
        else:
            westmoter.moveB(c_speed)
            eastmoter.moveB(c_speed)
            forward=False

    print("Up")
def commanddown(a=None):
    if forward==False or forward==None:
        if forward==None:
            c_speed=0
        c_speed= c_speed-10
        if c_speed<0:
            c_speed=0
        if c_speed==0:
            westmoter.Stop()
            eastmoter.Stop()
            forward=None
        else:
            westmoter.moveB(c_speed)
            eastmoter.moveB(c_speed)
            forward=False
    elif forward==True:
        c_speed=c_speed-10
        if c_speed<0:
            c_speed=0
        if c_speed==0:
            westmoter.Stop()
            eastmoter.Stop()
            forward=None
        else:
            westmoter.movef(c_speed)
            eastmoter.movef(c_speed)
            forward=True
    print("Down")
def commandright(a=None):
    
    if forward==True:
        if c_speed-30<0:
            eastmoter.movef(c_speed-30)
            westmoter.movef(c_speed-10)
            sleep(0.25)
            eastmoter.movef(c_speed)
            westmoter.movef(c_speed)
        else:
            eastmoter.Stop()
            if c_speed-10<0:
                if c_speed<0:
                    westmoter.movef(10)
                else:
                    westmoter.movef(c_speed)
            sleep(0.25)
            eastmoter.movef(c_speed)
            westmoter.movef(c_speed)
    elif  forward==False:
        if c_speed-30>0:
            eastmoter.moveB(c_speed-30)
            westmoter.moveB(c_speed)
            sleep(0.25)
            eastmoter.moveB(c_speed)
        elif c_speed<0 :
            eastmoter.moveB(5)
            westmoter.moveB(15)
        else:
            if c_speed-10<0:
                eastmoter.moveB(5)
                westmoter.moveB(15)
            else:
                eastmoter.moveB(c_speed-10)
                westmoter.moveB(c_speed-1)
    elif forward==None:
        print("Cant't Turn , Because I am not moving")
    print("Right")
def commandleft(a=None):

    if forward==True:
        if c_speed-30<0:
            eastmoter.movef(c_speed-10)
            westmoter.movef(c_speed-30)
            sleep(0.25)
            eastmoter.movef(c_speed)
            westmoter.movef(c_speed)
        else:
            westmoter.Stop()
            if c_speed-10<0:
                if c_speed<0:
                    eastmoter.movef(10)
                else:
                    eastmoter.movef(c_speed)
            sleep(0.25)
            eastmoter.movef(c_speed)
            westmoter.movef(c_speed)
    elif  forward==False:
        if c_speed-30>0:
            westmoter.moveB(c_speed-30)
            eastmoter.moveB(c_speed)
            sleep(0.25)
            westmoter.moveB(c_speed)
        elif c_speed<0 :
            westmoter.moveB(5)
            eastmoter.moveB(15)
        else:
            if c_speed-10<0:
                westmoter.moveB(5)
                eastmoter.moveB(15)
            else:
                westmoter.moveB(c_speed-10)
                eastmoter.moveB(c_speed-1)
    elif forward==None:
        print("Cant't Turn , Because I am not moving")
    print("Left")
def commandstop(a=None):
    westmoter.Stop()
    eastmoter.Stop()
    forward=None
    print("Stop")  


if __name__ == "__main__":
    # Moter(1,2,3).movef()
    # test("himansh","Raj").lol("bot")
    rungui()
