import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
html = urllib.request.urlopen(url, context=ctx).read()
print("Retrieving "+url)
print('Retrieved '+str(len(html))+' characters')
info=ET.fromstring(html)
lst=info.findall('comments/comment')
print('Count: '+str(len(lst)))
sum=0
for item in lst:
    sum=sum+int(item.find('count').text)
print('Sum: '+str(sum))