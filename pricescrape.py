#!/usr/bin/python3
#format output for Mattermost
#importing the libraries
import urllib.request
import re
from bs4 import BeautifulSoup


f = open('prices.html','r')
soup = BeautifulSoup(f,"lxml")
pricecostco = soup.find("meta", property="pricecostco")
pricebb = soup.find("meta", property="pricebb")
f.close()
print ("Content-type: application/json")
print ( "" )
print ('{"response_type": "in_channel", "text": "Price for Sony X900H\\nCostco: ' + pricecostco.get('content') + '\\nBestbuy: ' + pricebb.get('content') + '\\n', end='')
print ('","username" : "PriceBot9000"}')
quit()
