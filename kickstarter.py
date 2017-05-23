import json
import requests
import datetime

end_page = 2;
urls= []
wee={}

print("Starting scraper")

#scan through pages 1 to end_page for data, 20 results per page
for page in range(1,end_page+1):
    r = requests.get('https://www.kickstarter.com/discover/advanced.json?sort=most_funded&page=' + str(page))
    data = r.json()

    for index in range(len(data["projects"])):

        #Define Values for keys
        url = ('/'.join(("https://www.kickstarter.com/projects", str(data["projects"][index]["id"])[:-1], data["projects"][index]["slug"])))
        id = data["projects"][index]["id"]
        name = data["projects"][index]["name"]
        category = data["projects"][index]["category"]["name"]
        #Insert into Dictionary
        wee[data["projects"][index]["slug"]] = {"id": id, "name": name, "url": url, "category": category}


with open('data.json', 'w') as fp:
	json.dump(wee, fp, indent=4)
print("Dumped data to data.json")
