import json

with open("problems Moonboard Masters 2017 40.json", "r") as file:
    mdata = json.load(file)

#number of climbs total
tclimbs = mdata["total"]

#all holds used by every climb (large)
holds = []
for i in range(len(mdata["data"]) - 1):
    for j in range(len(mdata["data"][i]["moves"]) - 1):
        holds.append(mdata["data"][i]["moves"][j]["description"])

#list of every type of hold
letters = ["A","B","C","D","E","F","G","H","I","J","K"]
hold_types = []
for i in range(11):
    for j in range(18):
        hold_types.append(f"{letters[i]}{j + 1}")

#list of amount of a hold type in every climb
hold_type_count = []
for i in range(len(hold_types)):
    hold_type_count.append(holds.count(hold_types[i]))

#create final dictionary of percent of hold types in all climbs
percent = {}
for i in range(len(hold_types)):
    percent.update({hold_types[i]: f"{round((hold_type_count[i] / tclimbs) * 100, 2)}%"})

for key in percent:
    print(f"{key}: {percent[key]}")