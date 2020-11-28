from tkinter import *
import pyttsx3

# print("\")

engine = pyttsx3.init()
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
root = Tk()
root.title("himansh")
# root.iconwindow(r"C:\Users\IamTheHimansh\Desktop\Aanal-collage.jpg")

# command
def commandup(a=None):
    # engine.say("Monna")
    engine.say("The quick brown fox jumped over the lazy dog.")
    engine.runAndWait()
    print("Up")
def commanddown(a=None):
    print("Down")
def commandright(a=None):
    print("Right")
def commandleft(a=None):
    print("Left")
def commandstop(a=None):
    print("Stop")
def Quitme(a=None):
    engine.say("By By Dear good by")
    engine.runAndWait()
    root.destroy()
quitbtn = Button(root, text="Quit",command=root.destroy)
quitbtn.grid(row=0,column=2)



upbtn = Button(root, text="Up",command=commandup)
upbtn.grid(row=2,column=2)

leftbtn = Button(root, text="Left",command=commandleft)
leftbtn.grid(row=3,column=1)

stpobtn = Button(root, text="stop",command=commandstop)
stpobtn.grid(row=3,column=2)

rightbtn = Button(root, text="Right",command=commandright)
rightbtn.grid(row=3,column=3)

downbtn = Button(root, text="Down",command=commanddown)
downbtn.grid(row=4,column=2)
root.bind("<w>", commandup)
root.bind("<s>", commanddown)
root.bind("<d>", commandright)
root.bind("<a>", commandleft)
root.bind("<space>", commandstop)
root.bind("<z>", commandstop)
root.bind("<q>", Quitme)

root.bind("<W>", commandup)
root.bind("<S>", commanddown)
root.bind("<D>", commandright)
root.bind("<A>", commandleft)
root.bind("<Z>", commandstop)
root.bind("<Q>", Quitme)
def printhimansh(a=NONE):
    print("HIMANSH")
    engine.say("Himansh")
    # engine.say("Jai  Himansh")

    engine.runAndWait()
    engine.say("One")
    engine.say("Two")
    engine.say("Three")
    engine.say("Go Gone Goes")
    engine.runAndWait()
    
    engine.say("One on one ")
    engine.say("Two on two ")
    engine.say("Three on three")
    engine.say("One Two Three")
    engine.say("One, Two, Three")
    engine.runAndWait()
root.bind("<H><I><M><A><N><S><H>",printhimansh )
root.bind("<h><i><m><a><n><s><h>",printhimansh )
# root.bind("<space>",printhimansh )

root.bind("<Up>", commandup)
root.bind("<Down>", commanddown)
root.bind("<Right>", commandright)
root.bind("<Left>", commandleft)


root.mainloop()