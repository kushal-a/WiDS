import requests
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def get_coords(ra_s, dec_s):
    h_ind = ra_s.find('h')
    m_ind = ra_s.find('m')
    s_ind = ra_s.find('s')    
    h = float(ra_s[:h_ind])
    m = float(ra_s[(h_ind+1):m_ind])
    s = float(ra_s[(m_ind+1):s_ind])
    ra = h + m/60 + s/3600
    if dec_s[0] == '+':
        sign = 1
    else:
        sign = -1
    d_ind = dec_s.find('°')
    m_ind = dec_s.find('′')
    s_ind = dec_s.find('″')
    d = float(dec_s[1:d_ind])
    m = float(dec_s[(d_ind+1):m_ind])
    s = float(dec_s[(m_ind+1):s_ind])
    dec = sign*(d + m/60 + s/3600)
    return ra, dec

def plot(constellation):
    ind=int(np.where(constellation_names==constellation)[0])
    X=all_X[ind]
    Y=all_Y[ind]
    lums=all_lums[ind]
    lums_n = (16/np.max(lums))*lums

    plt.scatter(X,Y,s=lums_n)
    plt.show()

def get_map(constellation):
    url = f'https://en.wikipedia.org/wiki/List_of_stars_in_{constellation}' #page gets downloaded according to constellation
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'lxml')  #Here, the lxml parser is used instead of HTML parser

    tab = soup.find_all('table', attrs={'class':'wikitable sortable'})[0]   #To extract information from a wikipedia table
                               
    data = [[]]
    for i in tab.find_all('tr'):   #searching in each row of the table ( 'tr' tag stands for row)
        row = []                    #declaring empty row
        for j in i.find_all('td'):  #'td' tag stands for a cell
            row.append(j.get_text())   #add the text contents of each row to the list
        data.append(row)

    heads = []
    for i in tab.find_all('tr')[:1]:
        for j in i.find_all('th'):             #'th' tag stands for header cell
            heads.append(j.get_text().strip('\n'))

    name_ind = heads.index('Name')
    ra_ind = heads.index('RA')
    dec_ind = heads.index('Dec')
                                  
    mag_ind = heads.index('vis.mag.')
    
    name = []
    ra = []
    dec = []
    mag = []
    for i in data[2:-2]:
        name_string = i[name_ind]
        try:                                             #The code first tries to run the code inside try
            ra_string = i[ra_ind].replace('\xa0', '')
            dec_string = i[dec_ind].replace('\xa0', '')   #These are code used to format the data
            mag_string = i[mag_ind]                       
            if mag_string[0]=='−':
                mag_string = '-'+mag_string[1:]
        except:                                       #If any error gets thrown up, it will execute the code inside except
            continue
        try:
            ra_i, dec_i = get_coords(ra_string, dec_string)     #convert ra dec from string to float
        except:
            continue
        try:
            mag.append(float(mag_string))
            name.append(name_string)
            ra.append(ra_i)
            dec.append(dec_i)
        except:
            continue

    name = np.array(name)
    ra = np.array(ra)
    dec = np.array(dec)
    mag = np.array(mag)
    return name, ra, dec, mag
print("The program is scraping the web. Please wait")
page=requests.get('https://en.wikipedia.org/wiki/Lists_of_stars_by_constellation')
soup = BeautifulSoup(page.content,'lxml')
list_items=soup.find_all('li')

all_star_names=[]
all_X=[]
all_Y=[]
all_lums=[]
constellation_names=np.array([],dtype='S')

for constellation in list_items[5:93]:

    constellation_name=constellation.get_text()
    constellation_names=np.append(constellation_names,constellation_name) 
    names, ras, decs, mags = get_map(constellation_name)

    all_star_names.append(names)
    all_lums.append(10**(mags/(-2.5)))

    theta=np.radians(90-decs)
    phi=np.radians(15*ras)

    z=np.cos(theta)
    y=np.sin(theta)*np.sin(phi)
    x=np.sin(theta)*np.cos(phi)

    X=x/(1-z)
    Y=y/(1-z)

    all_X.append(X)
    all_Y.append(Y)

while True:
    name=input("Enter constellation name:")
    plot(name)
