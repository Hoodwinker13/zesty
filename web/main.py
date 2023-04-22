from bs4 import BeautifulSoup
import requests
import json

fandoms_html = requests.get("https://archiveofourown.org/media")

fandoms_text = fandoms_html.text

soup = BeautifulSoup(fandoms_text, 'lxml')

home_sec = soup.find_all(
    'a', class_ = "tag"
)
fandom_top = []
for fandom in home_sec:
    temp = {
        "name": fandom.get_text(),
        "link": "https://archiveofourown.org" + fandom.get("href")
    }
    fandom_top.append(temp)

fandom_for_all = soup.find_all(
    'p', class_ = "actions"
)
fandom_all = []
for links in fandom_for_all:
    temp = links.find(
        'a'
    )
    if(temp == None):
        continue
    fandom_links = "https://archiveofourown.org" + temp.get("href")
    fandom_html = requests.get(fandom_links)
    fandom_text = fandoms_html.text
    soup = BeautifulSoup(fandom_text, 'lxml')
    home_sec = soup.find_all(
    'a', class_ = "tag"
    )
    for fandom in home_sec:
        temp = {
            "name": fandom.get_text(),
            "link": "https://archiveofourown.org" + fandom.get("href")
        }
        fandom_all.append(temp)
    

all_fandom = {
    "top": fandom_top,
    "all": fandom_all
}

json_object = json.dumps(all_fandom, indent = 4)

with open("C:/Users/mjune/bearchainAI/web/json/fandoms.json", "w") as outfile:
    outfile.write(json_object)