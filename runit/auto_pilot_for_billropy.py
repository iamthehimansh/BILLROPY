import json
# import distance
import random 
import requests
person_not_avilabe_count=0
# go_json={}
class go_:
	"""docstring for go_"""
	def __init__(self):
		self.go_json={"go":False}
	def get(self):
		return self.go_json
	def set(self,data):
		self.go_json=data
me=go_()
stop=None
# funck
def stop():
	me.set({"go":False,"newpersonformed":True})
	stop=True
def openbrowserforclint():
	print("let browser is opened")

def getinstruction(person_avilable,mv_json):
	print("getinstruction called")

	if mv_json==False:
		if person_avilable["person_avilable"]==True:
			if person_avilable["frist_time"]==True:
				stop()
				openbrowserforclint()	
		else:
			# distance1=distance.getdistance()
			distance1=random.randint(10, 150)
			# with open("go.json","w") as go_file:
			if distance1>70 or distance1==70:
				me.set({"go":True,"person_not_avilabe_count":person_avilable["person_not_avilabe_count"]})
			else:
				me.set({"go":False,"person_not_avilabe_count":person_avilable["person_not_avilabe_count"]})
	else:
		me.set({"go":False,"stoped":"by WEb server"})
	print("getinstruction ending")
	return me.get() ,stop

