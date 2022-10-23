import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))-1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
name_list = []

tags = soup('a')

for i in range(count):
    name_list.append(tags[position].text)
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)


print(name_list[-1])
