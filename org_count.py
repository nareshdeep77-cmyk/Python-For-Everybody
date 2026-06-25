import sqlite3

# Database se connect karein aur ek fresh table banayein
conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'

try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

for line in fh:
    if not line.startswith('From '): continue
    pieces = line.split()
    email = pieces[1]
    
    # 💡 YAHAN HAI MAIN MODIFICATION: Email se domain extract karne ka logic
    parts = email.split('@')
    org = parts[1]
    
    # Database mein organization check aur update karein
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# Saara data memory se physical file mein save karein
conn.commit()

# Top organizations ko display karne ka SQL command
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print('\nTop Organizations:')
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()