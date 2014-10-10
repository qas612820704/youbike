import json
import MySQLdb
import urllib
import sys


# Get url
url = sys.argv[1]

# Convert JSON to object and get from URL
json_data = urllib.urlopen(url).read()
data = json.loads(json_data)

# Open database connection
db = MySQLdb.connect("localhost","youbikeuser","youbike","update_youbikedb")

# Prepare a cursor object using cursor() method
cur = db.cursor()

# Loop and insert
for x in data["retVal"]:
    sno = int(str(x["sno"]))
    sna = x["sna"]
    snaen= x["snaen"]
    tot = int(str(x["tot"]))
    sbi = int(str(x["sbi"]))
    mday = long(str(x["mday"]))

    sql = "INSERT INTO Aggregated_level(sno,sna,snaen,tot,sbi,mday) VALUES('%d','%s','%s','%d','%d','%d')" % (sno,sna,snaen,tot,sbi,mday)

    # Execute the SQL command
    cur.execute(sql)

# Commit changes in the database
db.commit()

# Close the database
db.close()
