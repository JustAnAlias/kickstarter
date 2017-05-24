import json
import os
wee={}

def run():
        for directory, subdirectories, files in os.walk("failed"):
            for file in files:
                print("failed project from file failed/"+file)
                with open("failed/"+file) as data_file:
                    data = json.load(data_file)

        #with open('failed/fail1.json') as data_file:
        #    data = json.load(data_file)

                for index in range(len(data["projects"])):

                #Define Values for keys
                        url = ('/'.join(("https://www.kickstarter.com/projects", str(data["projects"][index]["id"])[:-1], data["projects"][index]["slug"])))
                        id = data["projects"][index]["id"]
                        name = data["projects"][index]["name"]
                        category = data["projects"][index]["category"]["name"]
                        state = data["projects"][index]["state"]
                        goal = data["projects"][index]["goal"]
                        pledged = data["projects"][index]["pledged"]
                #Insert into Dictionary
                        wee[data["projects"][index]["slug"]] = {"id": id, "name": name, "url": url, "category": category, "state": state, "goal": goal, "pledged": pledged}


        with open('datafailed.json', 'w') as fp:
            json.dump(wee, fp, indent=4)
        print("Dumped data to datafailed.json for analysis")
