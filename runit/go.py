# import RPi.GPIO as GPIO
import json
from time import sleep
total_round=0
import requests
urlforgo_json='http://localhost:8080/movement_json'
data_for_go_json={"id":"robo 1.0","pass":"@!@IamTheHimansh/robo1z"}
r = requests.post(urlforgo_json,data=data_for_go_json)

# function
def  frist_path(q=0):
	total_distance=2.5
	distance_in_one_round=total_distance/10
	for i in range(1,11):
		while True:
			r = requests.post(urlforgo_json,data=data_for_go_json)
			main_moving_instruction=r.json()
			# with open("go.json","r") as moving_instruction:
			# 	main_moving_instruction=json.load(moving_instruction)
			if main_moving_instruction["go"]==True:
				moveforward(distance_in_one_round)

				if i==10:
					print("going done 1st compleat")
					if q==0:
						turn(90)
					else:
						turn(180)
				break
			# except Exception as e:
			# 	print(e)


def  second_path(q=0):
	total_distance=3.5
	distance_in_one_round=0.25
	no_of_moves=total_distance/distance_in_one_round #it contain the no of parts of move in wich robo goes to travel second path
	no_of_moves_int=no_of_moves//1
	no_of_moves_int=int(no_of_moves_int)
	print(no_of_moves_int)
	defreance_move=no_of_moves- no_of_moves_int
	for i in range(1,no_of_moves_int+1):
		while True:
			try:
				r = requests.post(urlforgo_json,data=data_for_go_json)
				main_moving_instruction=r.json()
				# with open("go.json","r") as moving_instruction:
				# 	main_moving_instruction=json.load(moving_instruction)
				if main_moving_instruction["go"]==True:
					moveforward(distance_in_one_round)
					if i==no_of_moves_int:
						moveforward(defreance_move)
						if not q==0:
							turn(90)
					break
			except:
				pass
	
	print("2nd compleated")

def  third_path(q=0):
	total_distance=3.5
	distance_in_one_round=0.25
	no_of_moves=total_distance//distance_in_one_round #it contain the no of parts of move in wich robo goes to travel third path
	no_of_moves_int=no_of_moves//1
	no_of_moves_int=int(no_of_moves_int)
	for i in range(1,no_of_moves_int+1):
		print(i)
		while True:
			try:
				r = requests.post(urlforgo_json,data=data_for_go_json)
				main_moving_instruction=r.json()
				# with open("go.json","r") as moving_instruction:
				# 	main_moving_instruction=json.load(moving_instruction)
				if main_moving_instruction["go"]==True:
					moveforward(distance_in_one_round)
					if i==no_of_moves_int:
						if q==0:
							for i in range(1,18+1):
								turn(10)
								sleep(2)
					break
			except:
				pass
	print("3rd compleated")


# for test purpose only function 
# def moveforward(distance):
# 	# go_forward(distance)
# 	print(f"going forward by {distance}")
# 	stop()

# def turn(degre):
# 	print(f"Turning {degre}`")
# 	# turn in given degree

# def stop(*kwargs):
# 	print("stop")

while True:
	try:
		r = requests.post(urlforgo_json,data=data_for_go_json)
		main_moving_instruction_1=r.json()
		# with open("go.json","r") as moving_instruction_1:
		# 	main_moving_instruction_1=json.load(moving_instruction_1)
		if main_moving_instruction_1["person_not_avilabe_count"]%5==0:
			pass
		else:
			total_round+=1
			if not total_round%2==0:
				frist_path()
				second_path()
				third_path()
				print("forward compleated")
			else:
				third_path(2)
				second_path(2)
				frist_path(2)
				print("backward compleated")
			print(f"No. of moves :- {total_round}")
		if total_round==2:
			break
	except KeyboardInterrupt:
		print(f"Total Round :- {total_round}")
		exitall()

