# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

inputcount = input('Enter count: ')
inputcount = int(inputcount)
inputpos = input('Enter position: ')
inputpos = int(inputpos)

# Retrieve all of the anchor tags
while inputcount > 0:
    inputcount = inputcount - 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tagspos = tags[inputpos-1] #finds the url by postion
    url = tagspos.get('href', tagspos) #this line returns the new url up to the top of the loop
    print(url)
