import json
import requests
import datetime
#import opencv

#data outputs to a CSV file in the current directory
csv_output = open("sample.csv", "w")

end_page = 2;
urls= []
wee={}

#scan through pages 1 to end_page for data, 20 results per page
for page in range(1,end_page+1):
    r = requests.get('https://www.kickstarter.com/discover/advanced.json?sort=most_funded&page=' + str(page))
    data = r.json()
    for index in range(len(data["projects"])):
        #print "%s,%f,%s,%f" % (data["projects"][index]["name"], data["projects"][index]["goal"], data["projects"][index]["currency"], data["projects"][index]["pledged"])
        csv_output.write("\"%s\",%s,%.0f,%s,%.2f,%d,%s,%s,%s\n" % (data["projects"][index]["name"].encode('ascii', 'ignore'),
            data["projects"][index]["category"]["slug"].split("/")[0],
            data["projects"][index]["goal"],
            data["projects"][index]["currency"],
            data["projects"][index]["pledged"],
            data["projects"][index]["backers_count"],
            str(datetime.datetime.fromtimestamp(data["projects"][index]["created_at"])),
            str(datetime.datetime.fromtimestamp(data["projects"][index]["launched_at"])),
            str(datetime.datetime.fromtimestamp(data["projects"][index]["deadline"]))))
        st = data["projects"][index]["id"]
	#urls.update("https://www.kickstarter.com/projects/"+str(data["projects"][index]["id"])[:-1]+"/"+data["projects"][index]["slug"])
        #print("",data["projects"][index]["id"],"/"+data["projects"][index]["slug"] )
        #urls.append("https://www.kickstarter.com/projects/"+str(data["projects"][index]["id"])[:-1]+"/"+data["projects"][index]["slug"])
        #urls.append('/'.join(("https://www.kickstarter.com/projects", str(data["projects"][index]["id"])[:-1], data["projects"][index]["slug"])))
        url = ('/'.join(("https://www.kickstarter.com/projects", str(data["projects"][index]["id"])[:-1], data["projects"][index]["slug"])))
#        urls.append(url)
        wee[data["projects"][index]["slug"]] = {"id": data["projects"][index]["id"], "name": data["projects"][index]["slug"], "url": url, "category": data["projects"][index]["category"]["name"]}
#        wee[data["projects"][index]["slug"]] = {"id": data["projects"][index]["id"]}
#        wee[data["projects"][index]["slug"]] = {"url": url}
#        wee['url'] = urls
        
	#urls.update("urls": url)

#print(urls)
#print(wee)

csv_output.close()


with open('data.json', 'w') as fp:
	json.dump(wee, fp, indent=4)
