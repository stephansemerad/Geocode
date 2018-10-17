#!/usr/bin/python
## -*- coding: utf-8 -*-
import os, re,random, string, sys,  os.path, time
dir_path = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent)
from datetime import datetime
import xmltodict
from urllib.request import urlopen
from decimal import Decimal
from bs4 import BeautifulSoup
import json, ast
import urllib.parse

address = "Brooklyn Avenue, New York, USA"
API_KEY = 'XXXXXXXXXXXXXXX'

address = urllib.parse.quote(address) #Fixes non Ascii Characters
url = "https://maps.googleapis.com/maps/api/geocode/json?key="+str(API_KEY)+"&new_forward_geocoder=true&address="+str(address)
print (url)
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser") #Get the HTML
soup = str(soup)
dictionary = json.loads(soup)
print(dictionary['results'][0]['address_components'])
location = dictionary['results'][0]['geometry']['location']#['address_components']
lat = location['lat']
lng = location['lng']
