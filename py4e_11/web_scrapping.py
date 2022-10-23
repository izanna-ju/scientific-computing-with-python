from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

content_list = []
ind_num = None
sum = 0

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
#    print('TAG:', tag)
#    print('Contents:', tag.contents[0])
    content_list.append(tag.contents[0])

for i in content_list:
    ind_num = int(i)
    sum += ind_num

print('The sum of numbers in the html doc is', sum)
#print(num_list)
#    print('URL:', tag.get('href', None))
#    print('Contents:', tag.contents[0])
#    print('Attrs:', tag.attrs)
