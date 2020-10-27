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
priceamzn = soup.find("meta", property="priceamzn")
pricebh = soup.find("meta", property="pricebh")
f.close()
print ("Content-type: application/json")
print ( "" )
print ('{"response_type": "in_channel", "text": "Price for Sony X900H\\nCostco: ' + pricecostco.get('content') + '\\nBestbuy: ' + pricebb.get('content') + 
  '\\nAmazon: ' + priceamzn.get('content') + '\\nB&H: ' + pricebh.get('content'), end='')
print ('","username" : "PriceBot9000"}')
quit()

