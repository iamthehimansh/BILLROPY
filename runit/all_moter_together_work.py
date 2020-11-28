import Moter
from all_moter_together_work import*
from time import sleep
speed=11
time_to_turn_1_deg=0.002
wmoter=Moter.Moter(1,2,3)
emoter=Moter.Moter(4,5,6)


def stop():
	wmoter.stop()
	emoter.stop()
def moveforward(distance):
	t=distance/speed
	wmoter.movef(100)
	emoter.movef(100)
	sleep(t)
	wmoter.stop()
	emoter.stop()
	print("moved forward {distance} cm")
def turn(angle):
	time=time_to_turn_1_deg*angle
	wmoter.stop()
	emoter.movef()
	sleep(time)
	wmoter.stop()
	emoter.stop()
	print("turned {angle}`")

def  exitall():
	wmoter.q()
	emoter.q()
