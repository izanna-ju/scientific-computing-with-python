import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counts = list()


url = input('Enter url: ')
#if len(address) < 1: break


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
for result in results:
    comment_count = int(result.find('count').text)
    counts.append(comment_count)


print("Sum:", sum(counts))
