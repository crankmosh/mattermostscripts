#scrape costco URL
#importing the libraries
import urllib.request
import re
from bs4 import BeautifulSoup
import datetime

urlcostco='https://www.costco.com/sony-65%22-class---x90ch-series---4k-uhd-led-lcd-tv.product.100657324.html'
urlbb='https://www.bestbuy.com/site/sony-65-class-x900h-series-led-4k-uhd-smart-android-tv/6401205.p?skuId=6401205'
urlbbtcl='https://www.bestbuy.com/site/tcl-65-class-6-series-led-4k-uhd-smart-roku-tv/6424216.p?skuId=6424216'
urlbh='https://www.bhphotovideo.com/c/product/1545417-REG/sony_xbr65x900h_x900h_65_class_hdr.html'
urlamzn='https://www.amazon.com/dp/B084KQLVFH'
urlamzntcl='https://www.amazon.com/dp/B0885N17CC'
urlbhtcl='https://www.bhphotovideo.com/c/product/1584065-REG/tcl_65r635_65_6_serie_4k_hdr.html'
urlbba8h='https://www.bestbuy.com/site/sony-65-class-a8h-series-oled-4k-uhd-smart-android-tv/6401203.p?skuId=6401203'
urlamzna8h='https://www.amazon.com/Sony-A8H-65-Inch-Compatibility/dp/B084KQLVKH/'
urlbha8h='https://www.bhphotovideo.com/c/product/1545413-REG/sony_xbr65a8h_a8h_65_class_hdr.html'

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

def get_data_amzn(url):
    req = urllib.request.Request(
       url,
       data=None,
       headers={'User-Agent': user_agent }
    )
    webpage = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(webpage, "lxml")
    return soup.find('span',class_="priceBlockBuyingPriceString")

def get_data_bh(url):
    req = urllib.request.Request(
       url,
       data=None,
       headers={'User-Agent': user_agent }
    )
    webpage = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(webpage, "lxml")
    return soup.find('div',class_="price_1DPoToKrLP8uWvruGqgtaY")

pricecostco = get_data_costco(urlcostco)
pricebb = get_data_bb(urlbb)
priceamzn = get_data_amzn(urlamzn)
pricebh = get_data_bh(urlbh)
pricebbtcl = get_data_bb(urlbbtcl)
#priceamzntcl = get_data_amzn(urlamzntcl)
pricebhtcl = get_data_bh(urlbhtcl)
pricebba8h = get_data_bb(urlbba8h)
priceamzna8h = get_data_amzn(urlamzna8h)
pricebha8h = get_data_bh(urlbha8h)

now = datetime.datetime.now()

f = open('/home/drkhoe/public_html/prices.html','w')
f.write("<h1>Current Prices for Sony X900H</h1>\n")
f.write("<p>Updated: ")
f.write("<meta property='updatetime' content='")
f.write(now.strftime("%h-%d-%y %H:%M"))
f.write("'>")
f.write(now.strftime("%h-%d-%y %H:%M"))
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
f.write("<p>Amazon: \n")
f.write("<meta property='priceamzn' content='")
f.write(priceamzn.text)
f.write("'>")
f.write(priceamzn.text)
f.write("</meta>")
f.write("<p>B&H: \n")
f.write("<meta property='pricebh' content='")
f.write(pricebh.text)
f.write("'>")
f.write(pricebh.text)
f.write("</meta>")
f.write("<h1>Current Prices for TCL R635</h1>\n")
f.write("<p>Bestbuy: \n")
f.write("<meta property='pricebbtcl' content='")
f.write(pricebbtcl.text)
f.write("'>")
f.write(pricebbtcl.text)
f.write("</meta>")
#f.write("<p>Amazon: \n")
#f.write("<meta property='priceamzntcl' content='")
#f.write(priceamzntcl.text)
#f.write("'>")
#f.write(priceamzntcl.text)
#f.write("</meta>")
f.write("<p>B&H: \n")
f.write("<meta property='pricebhtcl' content='")
f.write(pricebhtcl.text)
f.write("'>")
f.write(pricebhtcl.text)
f.write("</meta>")
f.write("<h1>Sony A8H OLED</h1>\n")
f.write("<p>Bestbuy: \n")
f.write("<meta property='pricebba8h' content='")
f.write(pricebba8h.text)
f.write("'>")
f.write(pricebba8h.text)
f.write("</meta>")
f.write("<p>Amazon: \n")
f.write("<meta property='priceamzna8h' content='")
f.write(priceamzna8h.text)
f.write("'>")
f.write(priceamzna8h.text)
f.write("</meta>")
f.write("<p>B&H: \n")
f.write("<meta property='pricebha8h' content='")
f.write(pricebha8h.text)
f.write("'>")
f.write(pricebha8h.text)
f.write("</meta>")
f.close
quit()

