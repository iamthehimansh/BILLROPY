import json
import random


with open("data.json","r")as rf:
    data=json.load(rf)    
    bacup=data
print(bacup)


for i in range(12,50):
    data[str(i)]={"name":f"Product {str(i)}","product_img":"/logo","product_des":"Now No Descripition here","prise":str((random.randint(700,1000))//7)}
    print(f"Data no {str(i)} is added")



try:
    with open("data.json","w")as wf:
        json.dump(data,wf)
except:
    with open("data.json","w")as wf:
        json.dump(bacup,wf)



with open("data.json","r")as rf:
    data=json.load(rf)    


print()
print()
print()
print()
print()
print(data)
