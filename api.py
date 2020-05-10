import json

with open("sample.json") as f:
    data = json.load(f)

# print(data)
tempitem = {"value": "Temp", "onclick": "CreateNewDoc()"}
# print(type(data["menu"]["popup"]["menuitem"]))
menuitem = data["menu"]["popup"]["menuitem"]
for i in range (10000):
    menuitem.append(tempitem)

for index, item in enumerate(menuitem):
    print(index, item)

with open('new_sample.json','w') as f:
    json.dump(data,f,indent=2)

