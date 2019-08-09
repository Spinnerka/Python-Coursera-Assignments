# This assignment is to pull numbers from XML file and sum them
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # get url from user
html = urllib.request.urlopen(url, context=ctx).read() # to get the data from the user url

numlist = list() #create an empty list

stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment') #list of tags/trees not strings

for item in lst:
    num = item.find('count').text
    num = int(num)
    numlist.append(num)
print(sum(numlist))
