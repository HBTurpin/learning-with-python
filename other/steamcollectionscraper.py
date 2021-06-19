import requests
from bs4 import BeautifulSoup

URL = 'https://steamcommunity.com/sharedfiles/filedetails/?id=2387767532'
page = requests.get(URL)

html = BeautifulSoup(page.content, features="lxml");
div_tags = html.find_all('div')
ids = []
for div in div_tags:
     ID = div.get('id')
     if str(ID).startswith("sharedfile_"):
        ids.append(ID[len("sharedfile_"):])


#ARK Config File Setup
with open("other/Game.txt", 'w') as f:
    f.write("[ModInstaller]\n")
    for id in ids:
        f.write("ModIDS="+id+"\n")
    f.close()

with open("other/GameUserSettings.txt", 'w') as f:
    f.write("[ServerSettings]\n")
    text = ""
    for id in ids:
        text += id + ","
    text = text[:-1]
    f.write("ActiveMods="+text)
    f.close()
    