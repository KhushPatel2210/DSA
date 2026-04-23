import json

name = input("please enter your name")
city = input("please enter the city name")

update_data={
    "name":"Khush Patel",
    "id":"21",
    "city":"GNR",
}

find_id=21

with open ("data.json","r") as file:
    data = json.load(file)
# print(data)

for i in data :
    if i["id"] == find_id:
        i["name"]=name
        i["city"]=city

with open ("data.json",'w') as file :
    json.dump(data,file,indent=4)
    
