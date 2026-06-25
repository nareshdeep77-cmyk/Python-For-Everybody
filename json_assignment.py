import urllib.request, urllib.parse, urllib.error
import json
import ssl

# SSL Certificate validation errors ko bypass karne ka standard engine block
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Aapke problem set ka exact actual data endpoint link
url = 'http://py4e-data.dr-chuck.net/comments_2418149.json'
print('Retrieving:', url)

# Remote server se data streams pull karna
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Deserialization phase: Flat string data ko native dictionary mein badalna
info = json.loads(data)

# 'comments' key ke andar chhupe huye array list objects ko target karna
comments_list = info['comments']

total_sum = 0
count = 0

# JSON Array structures par iteration loop chalana
for item in comments_list:
    # Key index name 'count' se direct value extract karke list matrix mein jodna
    total_sum += int(item['count'])
    count += 1

# Final data execution console outputs dump karna
print('Count:', count)
print('Sum:', total_sum)