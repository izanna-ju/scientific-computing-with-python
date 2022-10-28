import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL: ')

counts = list()

data = urllib.request.urlopen(url, context=ctx).read().decode()

info = json.loads(data)
print('User count:', len(info))

for item in info['comments']:
    counts.append(int(item['count']))

print('Sum: ', sum(counts))
