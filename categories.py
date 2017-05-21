import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)
projects = data.keys()

categories = []

for project in projects:

    name = data[project]['category']
    if name not in categories:
        categories.append(name)

#for values in categories:
        #print(values)


categories.sort()
for project in data.keys():
    for category in categories:
         if(data[project]["category"] == category):
             print(data[project]["name"])