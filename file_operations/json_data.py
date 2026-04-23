import json

new_data = {
    "name" :"foram",
    "id" : 21,
    "city" :"gnr",
}

with open("data.json",'r') as file:
    data=json.load(file)

data.append(new_data)

with open("data.json",'w') as file:
    json.dump(data,file,indent=4)

