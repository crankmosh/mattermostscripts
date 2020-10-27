#scrape costco URL
#importing the libraries
import urllib.request
import re
from bs4 import BeautifulSoup
import datetime

urlcostco='https://www.costco.com/sony-65%22-class---x90ch-series---4k-uhd-led-lcd-tv.product.100657324.html'
urlbb='https://www.bestbuy.com/site/sony-65-class-x900h-series-led-4k-uhd-smart-android-tv/6401205.p?skuId=6401205'
urlbh='https://www.bhphotovideo.com/c/product/1545417-REG/sony_xbr65x900h_x900h_65_class_hdr.html'
urlamzn='https://www.amazon.com/dp/B084KQLVFH'
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

now = datetime.datetime.now()

f = open('public_html/prices.html','w')
f.write("<p>Current Prices for Sony X900H<p>\n")
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
f.close
quit()

