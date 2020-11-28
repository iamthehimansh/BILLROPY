# import Moter
# import distance
import gui
# temp moter
class Moterz:
    def __init__(self,Ena,in1,in2):
        # in1= input 1 forward
        # in2=input 2 backward
        print("strt")
    def movef(self,s=30):
        print("f speed=",s)
    def ChangeSpeed(self,s=30):
        
       print("speed change ",s)
    def Stop(self):
        pass
    def moveB(self,s=30):
        print("b speed=",s)
    def q(self):
        print("GPIO cleaning up")
wmoter=Moterz(1,2,3)
emoter=Moterz(4,5,6)
mgui=gui.gui(wmoter,emoter)
