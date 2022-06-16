from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

c=0;sum=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
for span in spans:
    # Look at the parts of a tag
    l=re.findall('[0-9]+',str(span))
    if len(l)<1:    continue
    for i in l:
        c=c+1
        sum=sum+int(i)
print("Count "+str(c))
print("Sum "+str(sum))