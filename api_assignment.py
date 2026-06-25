import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Cryptographic handshake safety bypass layer
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# API baseline target endpoint
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Explicit target location requested by the assignment
address = 'Federal University of Minas Gerais'

# Build properly encoded query parameters mapping dictionary
params = dict()
params['q'] = address
params['key'] = 42  # Static access key sequence required by dr-chuck proxy

url = serviceurl + urllib.parse.urlencode(params)
print('Retrieving:', url)

# Fire HTTP request connection and read binary data streams
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

# Fallback check routine validation
if not js or 'features' not in js or len(js['features']) == 0:
    print('==== Failure To Retrieve ====')
    print(data)
else:
    # Navigate JSON DOM tree layers to grab the top node's plus_code data matrix
    plus_code = js['features'][0]['properties'].get('plus_code')
    print('Plus code:', plus_code)