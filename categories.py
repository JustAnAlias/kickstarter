import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)
projects = data.keys()

categoriesList = []
categoriesDict = {}


for project in projects:
    name = data[project]['category']
    if name not in categoriesList:
        categoriesList.append(name)

#for values in categoriesList:
        #print(values)

count = 0
categoriesList.sort()
for project in data.keys():
    for category in categoriesList:
         if(data[project]["category"] == category):
             if(category not in categoriesDict):
                categoriesDict[category] = data[project]["name"]
             else:
                 pass


pprint(categoriesDict)
