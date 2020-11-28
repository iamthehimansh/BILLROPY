from tkinter import *
from time import sleep
# for speak
import requests
def engine(a,url=None) :
    if url==None:
        url = 'http://robo1.himansh.com/speak'

    myobj = {'id': 'robo 1.0','pass':'hamthumkonahijantayhai','text':a}

    x = requests.post(url, data = myobj)

    print(x.text)

class gui:
    def __init__(self,westmoter,eastmoter):
        self.root = Tk()
        self.c_speed=0
        eastmoter.Stop()
        westmoter.Stop()
        quitbtn = Button(self.root, text="Quit",command=self.root.destroy)
        quitbtn.grid(row=0,column=2)
        self.forward=None
        # function
        def commandup(a=None):

            if self.forward==True or self.forward==None:
                if self.forward==None:
                    self.c_speed=0
                self.c_speed=self.c_speed+10
                if self.c_speed>100:
                    self.c_speed=100
                westmoter.movef(self.c_speed)
                eastmoter.movef(self.c_speed)
                westmoter.ChangeSpeed(self.c_speed)
                eastmoter.ChangeSpeed(self.c_speed)
                self.forward=True
            elif self.forward==False:
                self.c_speed=self.c_speed-10
                if self.c_speed<0:
                    self.c_speed=0
                if self.c_speed==0:
                    westmoter.Stop()
                    eastmoter.Stop()
                    self.forward=None
                else:
                    westmoter.moveB(self.c_speed)
                    eastmoter.moveB(self.c_speed)
                    westmoter.ChangeSpeed(self.c_speed)
                    eastmoter.ChangeSpeed(self.c_speed)
                    self.forward=False

            print("Up")
            speedvar.set(self.c_speed)
        def commanddown(a=None):
            if self.forward==False or self.forward==None:
                if self.forward==None:
                    self.c_speed=0
                self.c_speed= self.c_speed-10
                if self.c_speed<0:
                    self.c_speed=0
                if self.c_speed==0:
                    westmoter.Stop()
                    eastmoter.Stop()
                    self.forward=None
                else:
                    westmoter.moveB(self.c_speed)
                    eastmoter.moveB(self.c_speed)
                    westmoter.ChangeSpeed(self.c_speed)
                    eastmoter.ChangeSpeed(self.c_speed)
                    self.forward=False
            elif self.forward==True:
                self.c_speed=self.c_speed-10
                if self.c_speed<0:
                    self.c_speed=0
                if self.c_speed==0:
                    westmoter.Stop()
                    eastmoter.Stop()
                    self.forward=None
                else:
                    westmoter.movef(self.c_speed)
                    westmoter.ChangeSpeed(self.c_speed)
                    eastmoter.movef(self.c_speed)
                    eastmoter.ChangeSpeed(self.c_speed)
                    self.forward=True
            print("Down")
            speedvar.set(self.c_speed)
        def commandright(a=None):
            
            if self.forward==True:
                if self.c_speed-30<0:
                    eastmoter.movef(self.c_speed-30)

                    westmoter.movef(self.c_speed-10)
                    westmoter.ChangeSpeed(self.c_speed-10)
                    eastmoter.ChangeSpeed(self.c_speed-30)
                    sleep(0.25)
                    eastmoter.movef(self.c_speed)
                    westmoter.movef(self.c_speed)
                    westmoter.ChangeSpeed(self.c_speed)
                    eastmoter.ChangeSpeed(self.c_speed)
                else:
                    eastmoter.Stop()
                    if self.c_speed-10<0:
                        if self.c_speed<0:
                            westmoter.movef(10)
                            westmoter.ChangeSpeed(10)
                        else:
                            westmoter.movef(self.c_speed)
                            westmoter.ChangeSpeed(self.c_speed)
                    sleep(0.25)
                    eastmoter.movef(self.c_speed)
                    westmoter.movef(self.c_speed)
                    westmoter.ChangeSpeed(self.c_speed)
                    eastmoter.ChangeSpeed(self.c_speed)
            elif  self.forward==False:
                if self.c_speed-30>0:
                    eastmoter.moveB(self.c_speed-30)
                    westmoter.moveB(self.c_speed)
                    westmoter.ChangeSpeed(self.c_speed)
                    eastmoter.ChangeSpeed(self.c_speed-30)
                    sleep(0.25)
                    eastmoter.moveB(self.c_speed)
                elif self.c_speed<0 :
                    eastmoter.moveB(5)
                    westmoter.moveB(15)
                    westmoter.ChangeSpeed(15)
                    eastmoter.ChangeSpeed(5)
                else:
                    if self.c_speed-10<0:
                        eastmoter.moveB(5)
                        westmoter.moveB(15)
                        westmoter.ChangeSpeed(15)
                        eastmoter.ChangeSpeed(5)
                    else:
                        eastmoter.moveB(self.c_speed-10)
                        westmoter.moveB(self.c_speed-1)
                        westmoter.ChangeSpeed(self.c_speed-1)
                        eastmoter.ChangeSpeed(self.c_speed-10)
            elif self.forward==None:
                print("Cant't Turn , Because I am not moving")
            print("Right")
            speedvar.set(self.c_speed)
        def commandleft(a=None):

            if self.forward==True:
                if self.c_speed-30<0:
                    eastmoter.movef(self.c_speed-10)
                    westmoter.movef(self.c_speed-30)
                    sleep(0.25)
                    eastmoter.movef(self.c_speed)
                    westmoter.movef(self.c_speed)
                else:
                    westmoter.Stop()
                    if self.c_speed-10<0:
                        if self.c_speed<0:
                            eastmoter.movef(10)
                        else:
                            eastmoter.movef(self.c_speed)
                    sleep(0.25)
                    eastmoter.movef(self.c_speed)
                    westmoter.movef(self.c_speed)
            elif  self.forward==False:
                if self.c_speed-30>0:
                    westmoter.moveB(self.c_speed-30)
                    eastmoter.moveB(self.c_speed)
                    sleep(0.25)
                    westmoter.moveB(self.c_speed)
                elif self.c_speed<0 :
                    westmoter.moveB(5)
                    eastmoter.moveB(15)
                else:
                    if self.c_speed-10<0:
                        westmoter.moveB(5)
                        eastmoter.moveB(15)
                    else:
                        westmoter.moveB(self.c_speed-10)
                        eastmoter.moveB(self.c_speed-1)
            elif self.forward==None:
                print("Cant't Turn , Because I am not moving")
            print("Left")
            speedvar.set(self.c_speed)
        def commandstop(a=None):
            westmoter.Stop()
            eastmoter.Stop()
            self.forward=None
            print("Stop")
            speedvar.set(self.c_speed) 
        speedvar = IntVar()
        speed = Label(self.root, textvariable=speedvar)
        speed.grid(row=0,column=3)

        upbtn = Button(self.root, text="Up",command=commandup)
        upbtn.grid(row=3,column=2)

        leftbtn = Button(self.root, text="Left",command=commandleft)
        leftbtn.grid(row=4,column=1)

        stpobtn = Button(self.root, text="stop",command=commandstop)
        stpobtn.grid(row=4,column=2)

        rightbtn = Button(self.root, text="Right",command=commandright)
        rightbtn.grid(row=4,column=3)

        downbtn = Button(self.root, text="Down",command=commanddown)
        downbtn.grid(row=5,column=2)
        def Quitme(a=None):
            westmoter.q()
            eastmoter.q()
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
            engine("Jai  Mata di")
            engine("Himansh")
            engine("Jai  Himansh")
            engine("One Two Three")
            engine("One, Two, Three")
        self.root.bind("<H><I><M><A><N><S><H>",printhimansh )
        self.root.bind("<h><i><m><a><n><s><h>",printhimansh )
        # root.bind("<space>",printhimansh )

        self.root.bind("<Up>", commandup)
        self.root.bind("<Down>", commanddown)
        self.root.bind("<Right>", commandright)
        self.root.bind("<Left>", commandleft)
        self.root.mainloop()