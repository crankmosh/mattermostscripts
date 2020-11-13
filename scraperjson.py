#Advanced web scraper JSON OUTPUT for Mattermost
# Dr. Mosh
#importing the libraries
import urllib.request
import re
from bs4 import BeautifulSoup
import datetime
import pprint as pp

# setup the basic list
xprice = []
xtitle = []

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

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
        if pricetag is not None:
            xprice.append("$" + pricetag.get('content'))
        else:
            xprice.append('notfound')
    elif 'bestbuy' in url:
        pricetag = (soup.find('span',class_="price")).text
        if pricetag is not None:
            xprice.append(pricetag)
        else:
            xprice.append('notfound')
    elif 'amazon' in url:
        pricetag = (soup.find('span',class_="priceBlockBuyingPriceString")).text
        if pricetag is not None:
            xprice.append(pricetag)
        else:
            xprice.append('notfound')
    elif 'bhphotovideo' in url:
        pricetag = (soup.find('div',class_="price_1DPoToKrLP8uWvruGqgtaY")).text
        if pricetag is not None:
            xprice.append(pricetag)
        else:
            xprice.append('notfound')
    titletag = soup.title.string
    if titletag:
       if 'bhphotovideo' in url:
           xtitle.append('B&H ' + titletag)
       elif 'costco' in url:
           xtitle.append('Costco ' + titletag)
       else:
           xtitle.append(titletag)

# open urls.txt which is the URLs file
with open('/home/drkhoe/mattermostscripts/urls.txt') as f:
   urls = f.read().splitlines()

# process the URLs
for aa in urls:
    get_price(aa)

# get current date and time
now = datetime.datetime.now()

# open the HTML output file
fhtml = open('/home/drkhoe/public_html/prices.json','w')

# write out update time to HTML file
fhtml.write('Updated: ' + now.strftime("%h-%d-%y %H:%M"))

# mattermost write out JSON header
fhtml.write('\\n---\\n#### TV Prices from PriceBOT 9000\\n')

# write table header
fhtml.write('| Description                                                                  | Price     |\\n')
fhtml.write('|:-----------------------------------------------------------------------------|:----------|\\n')
for bb in range(len(xprice)):
    fhtml.write('| '  + xtitle[bb].replace(':','').replace('"','inch') + ' | ' + xprice[bb].replace(',','') + ' | \\n')

fhtml.write('---\\n","username" : "PriceBOT9000"}')

f.close()
fhtml.close()

quit()

