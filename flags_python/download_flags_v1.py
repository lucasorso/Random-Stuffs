import os
import json
import urllib
import unicodedata
from urllib.request import Request
from urllib.request import urlopen

# https://www.countryflags.io/#body #Source

# <img src="https://www.countryflags.io/be/shiny/64.png">
# <img src="https://www.countryflags.io/be/flat/64.png">

# Version 1.0

IMG_URL = "https://www.countryflags.io/{}/{}/64.png"
IMG_PATH = "images/{}/"

SHINY = 'shiny'
FLAT = 'flat'

def download_img(flag_code, img_name, type):
	image_path = IMG_PATH.format(type)
	if not os.path.exists(image_path):
		os.makedirs(image_path)

	request = Request(IMG_URL.format(flag_code, type), headers={'User-Agent': 'Mozilla/5.0'})
	response = urlopen(request)

	with open(image_path + img_name, "wb") as f:
		f.write(response.read())

def format_icon_name(name):
	sample = "ic_{}.png"
	name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode('utf8')
	return sample.format(name.lower()).replace(" ", "_").replace("\"", "")

countries_flag = json.load(open('flags_obj.json'))

count = 0

for country in countries_flag:
	
	flag_code = country['code']
	flag_name = country['name']

	print(format_icon_name(flag_name))

	print(count, flag_code, flag_name, "\n")
	download_img(flag_code, format_icon_name(flag_name), SHINY)
	
	count = count + 1