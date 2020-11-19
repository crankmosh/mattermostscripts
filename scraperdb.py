#Advanced web scraper v2 output HTML
# 11-15-2020 this one uses MySQL
# Dr. Mosh
#importing the libraries
import urllib.request
import re
from bs4 import BeautifulSoup
import datetime
import pprint as pp
import mysql.connector
from mysql.connector import errorcode

DB_NAME = "pricebot"
DB_USER = "pricebot"
DB_PASSWORD = ""
DB_HOST = "localhost"

# setup the basic list
xprice = ["Price"]
xtitle = ["Model"]
xvendor = ["Vendor"]
xurl = []
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

# pricetable = id,vendor,item,price,url
# price grabber for various sites
def get_price(url):
    req = urllib.request.Request(
       url,
       data=None,
       headers={'User-Agent': user_agent }
    )
    webpage = urllib.request.urlopen(req,timeout=30).read()
    if webpage is not None:
        soup = BeautifulSoup(webpage, "lxml")
    if 'costco' in url:
        pricetag = soup.find("meta",property="product:price:amount")
        tprice = pricetag.get('content'))
        tvendor = "Costco"
    elif 'bestbuy' in url:
        tprice = (soup.find('span',class_="price")).text
        tvendor = "Best Buy"
    elif 'amazon' in url:
        tprice = (soup.find('span',class_="priceBlockBuyingPriceString")).text
        tvendor = "Amazon"
    elif 'bhphotovideo' in url:
        tprice = (soup.find('div',class_="price_1DPoToKrLP8uWvruGqgtaY")).text
        tvendor = "B&H Photo"
    titletag = soup.title.string
    if titletag:
       if 'X90CH' in titletag:
           ttitle = "Sony X90CH"
       elif 'X900H' in titletag:
           ttitle = "Sony X900H"
       elif 'TCL' in titletag:
           ttitle = "TCL R635"
       elif 'VIZIO' in titletag:
           ttitle = "Vizio M-Series"
       elif 'A8H' in titletag:
           ttitle = "Sony OLED A8H"
       elif 'H9G' in titletag:
           ttitle = "Hisense H9G"
       elif 'CX' in titletag:
           ttitle = "LG CX OLED"
    fprice = float(tprice)
    add_item = ("INSERT INTO pricetable "
               "(vendor,item,price,url) "
               "VALUES (%(tvendor)s,%(ttitle)s,%(fprice)s,%(url)s)")

# open urls.txt which is the URLs file
with open('/home/drkhoe/mattermostscripts/urls.txt') as f:
   urls = f.read().splitlines()

cnx = mysql.connector.connect(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)
cursor = cnx.cursor()

# process the URLs
for aa in urls:
    get_price(aa)

# get current date and time
now = datetime.datetime.now()

# open the HTML output file
fhtml = open('/home/drkhoe/public_html/pricesx.html','w')


lendesc = len(xtitle)
fhtml.write("<!DOCTYPE html>")
fhtml.write("<head>")
fhtml.write("<title>TV Price Scraper Output</title>")
fhtml.write('<link rel="stylesheet" href="style.css"/>')
fhtml.write("</head><body>")
fhtml.write('<table class="styled-table">')
fhtml.write("<thead><tr><th>" + xvendor[0] + "</th><th>" + xtitle[0] + "</th><th>" + xprice[0] + "</th></tr></thead>")
for xx in range(lendesc):
   if xx:
      fhtml.write("<tr><td>" + xvendor[xx] + '</td><td><a href="' + xurl[xx-1] + '">' + xtitle[xx] + "</a></td><td>" + xprice[xx] + "</td></tr>")
fhtml.write("</table>")

# write update time to HTML file
fhtml.write("Updated: " + now.strftime("%h-%d-%y %H:%M") + "<br>")
fhtml.write("</body>")

f.close()
fhtml.close()

quit()

