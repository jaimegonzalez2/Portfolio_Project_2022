#-------------------------------------------------------------------------------
# Name:        GIS Web Scraper
# Purpose:
#
# Author:      Jaime Gonzalez Jr.
#
# Created:     08/18/2020
#-------------------------------------------------------------------------------
# Web Scraper
# This python project is used to show the latest trend(s) in a given website. 
# In this case, I used an assortment of Geographic Information Systems websites. 

import requests
from bs4 import BeautifulSoup
import webbrowser
import pyperclip

# Geoawesomeness Website
r = requests.get('https://geoawesomeness.com/topics/geotrends/')
soup = BeautifulSoup(r.content, 'html5lib')

newDivs = soup.findAll('h3', {'class': 'entry-title td-module-title'})

print("Geoawesomeness Geotrends:")
for n in newDivs:
    print(n.text)

print('')

# Accessing the Geoawesomeness Website
user_input = input('Would you like to access the Geoawesomeness website? \
Yes (Y) or No (N).')

# Geoawesomeness website
pyperclip.copy('https://geoawesomeness.com/topics/geotrends/')

# Configuring the permission to accessing the website
if user_input == 'Y' or user_input == 'y':
    geo = pyperclip.paste()
    webbrowser.open(geo)
else:
    pass

print('')

# GIS Lounge Updates
l = requests.get('https://www.gislounge.com/')
soup1 = BeautifulSoup(l.content, 'html5lib')

updateDivs = soup1.findAll('h2', {'class':'wp-show-posts-entry-title'})


print('GIS Lounge Updates:')
for u in updateDivs:
    print(u.text)

print('')

# Accessing the GIS Lounge Website
user_input = input('Would you like to access the GIS Lounge website?\
 Yes (Y) or No (N).')

# GIS Lounge website
pyperclip.copy('https://www.gislounge.com/')

# Configuring the permission to accessing the website
if user_input == 'Y' or user_input == 'y':
    lounge = pyperclip.paste()
    webbrowser.open(lounge)
else:
    pass

print('')



# GIS Lounge Updates (via LinkedIn)
link = requests.get('https://www.linkedin.com/company/gis-lounge/')
soup2 = BeautifulSoup(link.content, 'html5lib')

linkDivs = soup2.findAll('span', {'class':'break-words'})


print('GIS Lounge LinkedIn Updates:')
for g in linkDivs:
    print(g.text)

print('')

# Esri Updates
esri = requests.get('https://www.esri.com/arcgis-blog/?s=#&categories=announcements')
soup2 = BeautifulSoup(esri.content, 'html5lib')

eDivs = soup2.findAll('h3', {'class':'news-card--result-title-link'})


print('Esri Annoucements:')
for es in eDivs:
    print(es.text)

print('')

# Source/Credit: https://www.youtube.com/watch?v=gvdSkBmjpbY
# https://www.hackersfriend.com/articles/building-news-aggregator-web-app-with-django-using-python-web-scraping
