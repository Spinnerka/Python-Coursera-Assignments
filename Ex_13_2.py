import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

js = json.loads(data)
#print(js)
#print(json.dumps(js, indent=4))

numlist = list()

for value in js['comments']:
    num = int(value['count'])
    numlist.append(num)

print('Sum =', sum(numlist))


#----------------------------------------------------------------------------
