import requests

r = requests.post('http://localhost:8080/movement_json',data={"id":"robo 1.0","pass":"@!@IamTheHimansh/robo1z"})
print(r)
print()
print(r.json())