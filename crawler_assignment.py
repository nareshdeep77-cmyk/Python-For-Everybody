import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# SSL Exception automation handler block
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Dynamic parameter arrays mapping directly from user submission grid
url = 'http://py4e-data.dr-chuck.net/known_by_Siubhan.html'
count = 7
position = 18

print('Retrieving:', url)

# Web crawling automation loop matrix
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    
    # Python arrays zero-based index normalization wrapper (18th item is index 17)
    target_tag = tags[position - 1]
    url = target_tag.get('href', None)
    
    print('Retrieving:', url)

# Final page extraction trace to output the target string sequence name
final_name = target_tag.contents[0]
print('\nFinal Name Result:', final_name)