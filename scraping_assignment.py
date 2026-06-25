import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# SSL Errors ko bypass karne ka configuration block
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Aapka explicit actual data link setting array
url = 'http://py4e-data.dr-chuck.net/comments_2418146.html'
html = urllib.request.urlopen(url, context=ctx).read()

# BeautifulSoup element DOM parser setup
soup = BeautifulSoup(html, 'html.parser')

# Initialize counters
total_sum = 0
count = 0

# Pure page se saare 'span' tags ko target karna
tags = soup('span')
for tag in tags:
    # Tag ke andar chhupe huye text contents ko integer mein cast karna
    num = int(tag.contents[0])
    total_sum += num
    count += 1

# Output display logic lines terminal par print karne ke liye
print('Count:', count)
print('Sum:', total_sum)