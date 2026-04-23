import json

with open("data.json",'r') as file:
    data=json.load(file)
# print(data)

lenght =0
for i in data:
    lenght += 1

print(lenght)

name=input("please enter your name")
city=input("enter your city")

added_data = {
    "name":name,
    "id":lenght+1,
    "city":city
}

data.append(added_data)

with open ("data.json",'w') as file:
    json.dump(data,file,indent=4)
