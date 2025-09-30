import requests
import json
from bs4 import BeautifulSoup
json_list =[]
for page in range(1,11):
    api_end = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url=api_end)
    data = response.text
    soup = BeautifulSoup(data, "lxml")
    quotes = soup.find_all(class_="text")
    author = soup.find_all(class_="author")
    for i in range(len(quotes)):
        json_list.append({ "Quote" : quotes[i].text.strip("“”") , "Author" : author[i].text})

with open("Quotes.json","w") as datafile:
    json.dump(json_list,datafile,indent=4)

print("The JSON File has been successfully saved")
