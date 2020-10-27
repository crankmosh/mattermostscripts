#scrape costco URL
#importing the libraries
import urllib.request
import re
from bs4 import BeautifulSoup
import datetime

urlcostco='https://www.costco.com/sony-65%22-class---x90ch-series---4k-uhd-led-lcd-tv.product.100657324.html'
urlbb='https://www.bestbuy.com/site/sony-65-class-x900h-series-led-4k-uhd-smart-android-tv/6401205.p?skuId=6401205'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

def get_data_costco(url):
    req = urllib.request.Request(
       url,
       data=None,
       headers={'User-Agent': user_agent }
    )
#    print('getting URL' )
    webpage = urllib.request.urlopen(req,timeout=30).read()
    soup = BeautifulSoup(webpage, "lxml")
#    print('parsing...')
    return soup.find("meta", property="product:price:amount")
#    print (price.get('content'))

def get_data_bb(url):
    req = urllib.request.Request(
       url,
       data=None,
       headers={'User-Agent': user_agent }
    )
#    print('getting URL' )
    webpage = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(webpage, "lxml")
#    print('parsing...')
    return soup.find('span',class_="price")
#    print (price.text)

pricecostco = get_data_costco(urlcostco)
pricebb = get_data_bb(urlbb)

now = datetime.datetime.now()

f = open('public_html/prices.html','w')
f.write("<p>Current Prices for Sony X900H<p>\n")
f.write("<p>Updated: ")
f.write("<meta property='updatetime' content='")
f.write(now.strftime("%m-%h-%y %H:%M"))
f.write("'>")
f.write(now.strftime("%m-%h-%y %H:%M"))
f.write("</meta>")
f.write("<p>Costco: \n")
f.write("<meta property='pricecostco' content='")
f.write(pricecostco.get('content'))
f.write("'>")
f.write(pricecostco.get('content'))
f.write("</meta>")
f.write("<p>Bestbuy: \n")
f.write("<meta property='pricebb' content='")
f.write(pricebb.text)
f.write("'>")
f.write(pricebb.text)
f.write("</meta>")
f.close
quit()
