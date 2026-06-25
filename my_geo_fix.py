import sqlite3
import json
import codecs

# 1. Database connection layer setup
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# 2. Direct static bypass injection layer for your location
my_address = "Chhattishgarh Raipur New Rajendra"
# Realistic geocoding mapping dictionary mock for Raipur, India Standard Coordinates
my_geo_data = {
    "status": "OK",
    "results": [{
        "formatted_address": "New Rajendra Nagar, Raipur, Chhattisgarh 492001, India",
        "geometry": {
            "location": {
                "lat": 21.2333,
                "lng": 81.6444
            }
        }
    }]
}

# Insert custom entry into database cache cleanly
cur.execute('SELECT address FROM Locations WHERE address = ?', (my_address,))
row = cur.fetchone()
if row is None:
    cur.execute('''INSERT INTO Locations (address, geodata) 
                VALUES (?, ?)''', (my_address, json.dumps(my_geo_data)))
    conn.commit()
    print(f"[SUCCESS] Custom entry injected: {my_address}")

# 3. Trigger immediate serialization dump directly to where.js
print("Generating where.js file layout maps data...")
cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', 'utf-8')
fhand.write("myData = [\n")

count = 0
for row in cur:
    data = str(row[1].decode()) if isinstance(row[1], bytes) else str(row[1])
    try:
        js = json.loads(data)
    except:
        continue

    if not('status' in js and js['status'] == 'OK'): continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    
    try:
        count = count + 1
        if count > 1: fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(f"[SUCCESS] {count} records successfully generated inside where.js!")
print("Please refresh your where.html browser window now.")