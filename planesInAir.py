# This module is responsible for getting info about all a/c in air
#OUTPUT - DICTIONARY WITH ALL AIRCRAFT IN AIR
# // dict = {'reg': {'type': type, 'callsign': callsign, 'altitude': altitude}, 'Lat/Long': ['29.357052', '-100.77845']...}

from bs4 import BeautifulSoup
import requests
from re import sub


# 2 zone - 2 pages No Europe and Europe
urlElsewhere = 'https://www.ads-b.nl/index.php?pageno=2002'
urlEurope = 'https://www.ads-b.nl/index.php?pageno=2001'

# get 'dirty' aircraft table
def getSource(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    acSource = soup.find(id='content').find_all(style='background-color: powderblue; border-bottom: 1px solid white;')
    return acSource

# get dict of aircraft now in air dict = {'reg': {'type': type, 'callsign': callsign, 'altitude': altitude},...}
# status can be - 'in air', 'out-of-range'
def nowInAir(acSource):
    acInAir = {}
    for aircraft in acSource:
        kol2 = aircraft.find_all(class_="col-2 kolom")
        reg = kol2[0].get_text(strip=True)
        type = kol2[1].get_text(strip=True)
        callsign = kol2[2].get_text(strip=True)
        if callsign == '':
            callsign = 'No data'
        kol1 = aircraft.find_all(class_="col-1 kolom")
        altitude = kol1[1].get_text(strip=True)
        latLong = kol1[4].select('img')[0]["title"][12:-2].split(',')
        if altitude == '':
            altitude = 'No data'
        reg = sub(r'[^\w\s]', '', reg) #delete all symbols except letters and digits
        acInAir[reg] = {'type': type, 'callsign': callsign, 'altitude': altitude, 'Lat/Long': latLong, 'status': 'in air', 'chat_id': []}
    return acInAir

# get common table with aircraft in air from all zones. output - dict
def getInAir():
    InAirElsewhere = nowInAir(getSource(urlElsewhere))
    InAirEurope = nowInAir(getSource(urlEurope))
    inAir = InAirElsewhere | InAirEurope
    return inAir
