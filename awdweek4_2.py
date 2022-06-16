# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count=int(input('Enter count: '))+1
position=int(input('Enter position: '))
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    print("Retrieving: "+url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    c=1
    for tag in tags:
        s=str(tag.get('href', None))
        if c==position:
            url=s
            break
        c=c+1