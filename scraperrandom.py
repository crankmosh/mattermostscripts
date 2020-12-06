#Advanced web scraper v2 output HTML
# Dr. Mosh
#importing the libraries
import urllib.request
import re
from bs4 import BeautifulSoup
import datetime
import pprint as pp
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import logging

# setup the basic list
xprice = []
xtitle = []
xvendor = []
xmodels = []
xurl = []
rsize = []
xsize = ['65','75','77','82','86','Blu-ray']

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

# price grabber for various sites
def get_price(url):
    webpage = req_proxy.generate_proxied_request(test_url)
    if webpage is not None:
        soup = BeautifulSoup(webpage, "lxml")
    if 'costco' in url:
        pricetag = soup.find("meta",property="product:price:amount")
        if pricetag is not None:
            xprice.append("$" + pricetag.get('content'))
        else:
            xprice.append('notfound')
        xvendor.append("Costco")
        xurl.append(url)
    elif 'bestbuy' in url:
        #pricetag = (soup.find('span',class_="aria-hidden")).text
        pricetag = (soup.find('span',class_="sr-only")).text.replace('Your price for this item is','')
        if pricetag is not None:
            xprice.append(pricetag)
        else:
            xprice.append('notfound')
        xvendor.append("Best Buy")
        xurl.append(url)
    elif 'amazon' in url:
        pricetag = (soup.find('span',class_="priceBlockBuyingPriceString")).text
        if pricetag is not None:
            xprice.append(pricetag)
        else:
            xprice.append('notfound')
        xvendor.append("Amazon")
        xurl.append(url)
    elif 'bhphotovideo' in url:
        pricetag = (soup.find('div',class_="price_1DPoToKrLP8uWvruGqgtaY")).text
        if pricetag is not None:
            xprice.append(pricetag)
        else:
            xprice.append('notfound')
        xvendor.append("B&H Photo")
        xurl.append(url)
    titletag = soup.title.string
    if titletag:
       res = [ele for ele in xsize if (ele in titletag)]
       rsize.append(str(res))
       if 'X90CH' in titletag:
           xtitle.append("Sony X90CH")
       elif 'X900H' in titletag:
           xtitle.append("Sony X900H")
       elif 'TCL' in titletag:
           xtitle.append("TCL R635")
       elif 'VIZIO' in titletag:
           xtitle.append("Vizio M-Series")
       elif 'A8H' in titletag:
           xtitle.append("Sony OLED A8H")
       elif 'H9G' in titletag:
           xtitle.append("Hisense H9G")
       elif 'H8G' in titletag:
           xtitle.append("Hisense H8G")
       elif 'CX' in titletag:
           xtitle.append("LG CX OLED")
       else:
           xtitle.append(titletag)

            
# open urls.txt which is the URLs file
with open('/home/drkhoe/mattermostscripts/urls.txt') as f:
   urls = f.read().splitlines()

req_proxy = RequestProxy(log_level=logging.ERROR)

# process the URLs
for aa in urls:
    get_price(aa)

# get current date and time
now = datetime.datetime.now()

# open the HTML output file
fhtml = open('/home/drkhoe/public_html/prices.html','w')

# sort into product lists
lendesc = len(xtitle)

fhtml.write("<!DOCTYPE html>\n")
fhtml.write("<head>\n")
fhtml.write("<title>TV Price Scraper Output</title>\n")
fhtml.write('<link rel="stylesheet" href="style.css"/>\n')
fhtml.write("</head><body>\n")
fhtml.write('<table class="styled-table">\n')

for jj in range(lendesc):
   if xtitle[jj] not in xmodels:
    xmodels.append(xtitle[jj])

lenmodels = len(xmodels)    
# iterate list and write html
for jj in range(lenmodels):
    fhtml.write('<thead><tr><th colspan="6">')
    fhtml.write(xmodels[jj] + "</th></tr></thead>\n")
    for xx in range(lendesc):
        if xtitle[xx] in xmodels[jj]:
            ssize = re.sub(r'\W+', '', rsize[xx])
            fhtml.write("<tr><td>" + xvendor[xx] + '</td><td> Size: ' + ssize + '</td><td><a href="' + xurl[xx] + '" target=_newlookup>Click Here</a></td><td>' + xprice[xx] + "</td></tr>\n")
fhtml.write("</table>\n")

# write update time to HTML file
fhtml.write("Updated: " + now.strftime("%h-%d-%y %H:%M") + "<br>\n")
fhtml.write("</body>")

f.close()
fhtml.close()

quit()

