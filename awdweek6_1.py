import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print("Retrieving "+url)
html = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved '+str(len(html))+' characters')
info=json.loads(html)
print('Count:',len(info['comments']))
sum=0
for item in info['comments']:
    sum=sum+item['count']
print('Sum: '+str(sum))