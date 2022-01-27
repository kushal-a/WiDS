import requests
from bs4 import BeautifulSoup
import numpy as np

page = requests.get('https://en.wikipedia.org/wiki/List_of_natural_satellites')
soup = BeautifulSoup(page.content,'html.parser')
tab = soup.find_all('table',attrs={'class':'wikitable sortable jquery-tablesorter'})
planets=[]
names=[]
diameter=[]

for i in tab.find_all('tr'):
    row=i.find_all('td')
    planets.append(row[1].get_text())
    names.append(row[3].get_text())
    txt=row[4].get_text()
    if '±' in txt:
        txt = txt.split('±')[0]
        txt = txt.strip()
    dia = 2*float(txt)
    diameter.append(str(dia))

entries=[]
for i in range(len(planets)):
    entries.append(','.join(planets[i],names[i],diameter[i]))

csv = '\n'.join(entries)
print(csv)


