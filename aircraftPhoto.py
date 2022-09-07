#this module allow determine the wing a/c attached to

import requests
from bs4 import BeautifulSoup

def getPlanePage(reg):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    page = requests.get('https://www.planespotters.net/search?q=' + reg, headers=header)
    soup = BeautifulSoup(page.text, 'lxml')
    print(soup)
    photoPage = soup.find(class_='photo_card__grid')
    print(photoPage)

getPlanePage('93-0602')

