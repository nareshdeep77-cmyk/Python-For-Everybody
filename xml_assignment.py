import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# SSL Cryptographic handshake validation bypass layers
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User parameter input assignment data endpoints definition
url = 'http://py4e-data.dr-chuck.net/comments_2418148.xml'
print('Retrieving:', url)

# Pull clean data streams bytes directly across remote gateways
xml_data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(xml_data), 'characters')

# Deserialize incoming flat text array chunks into an element tree
tree = ET.fromstring(xml_data)

# Execute XPath query addressing traversal map to capture targets
counts = tree.findall('.//count')

total_sum = 0
elements_count = 0

# Iteration routine array mapping counts loop
for count_tag in counts:
    # Safely cast child node text primitive string targets to standard integers
    num = int(count_tag.text)
    total_sum += num
    elements_count += 1

# Telemetry data feedback console dumps
print('Count:', elements_count)
print('Sum:', total_sum)