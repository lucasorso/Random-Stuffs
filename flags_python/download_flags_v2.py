import os
import json
import urllib
import unicodedata
import re
import requests
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup as Bs
from lxml import html


# https://www.countryflags.io/#body #Source

# <img src="https://www.countryflags.io/be/shiny/64.png">
# <img src="https://www.countryflags.io/be/flat/64.png">

# Version 2.0

IMG_URL = "https://www.countryflags.io/{}/{}/64.png"
IMG_PATH = "images_v2/{}/"

SHINY = 'shiny'
FLAT = 'flat'

def download_img(flag_code, img_name, type = FLAT):
	image_path = IMG_PATH.format(type)
	if not os.path.exists(image_path):
		os.makedirs(image_path)

	request = Request(IMG_URL.format(flag_code, type), headers={'User-Agent': 'Mozilla/5.0'})
	response = urlopen(request)

	with open(image_path + img_name, "wb") as f:
		f.write(response.read())

def download_img(url, img_name, type = FLAT):
	image_path = IMG_PATH.format(type)
	if not os.path.exists(image_path):
		os.makedirs(image_path)

	request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	response = urlopen(request)

	with open(image_path + img_name, "wb") as f:
		f.write(response.read())

def format_icon_name(name):
	sample = "ic_{}.png"
	name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode('utf8')
	return sample.format(name.lower()).replace(" ", "_").replace("\"", "")


url = 'https://www.countryflags.io/#body'

request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(request)

soup = Bs(response)

URL = 'https://www.countryflags.io{}'

divs = soup.findAll(class_= 'item_country')    

for div in divs:
    #print(div)
    print(div.findAll('p')[1].text) # name
    download_img(URL.format(div.img['src']), format_icon_name(div.findAll('p')[1].text))
    #print(div.img['src']) # img source
    #print(div.find(class_ = 'bold').text) # code
    print('\n')