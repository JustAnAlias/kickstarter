import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)
    

uniques = []

for project in data.keys():
    name = data[project]['category']
    if name not in uniques:
        uniques.append(name)

for values in uniques:
        print(values)