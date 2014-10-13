# -*- coding: utf-8 -*-
import MySQLdb
import sys
from scipy.cluster.vq import *

nu_groups = int(sys.argv[1])
# Open database connection
db = MySQLdb.connect("localhost","youbikeuser","youbike","kmeansdb")

# prepare a cursor object using cursor() method
cur = db.cursor()

# Prepare SQL query to SELECT
sql = "SELECT * FROM time_average_tot"
# Execute the SQL command
cur.execute(sql)
# Fetch the rows in a list of lists.
results = cur.fetchall()
features = []
station_name = []
station_nu = []
for row in results:
    station_nu.append(row[0])
    station_name.append(row[1])
    input = [float(row[i]) for i in range(2,9)]
    features.append(input)

whiten_features = whiten(features)
centroid, label = kmeans2(whiten_features,nu_groups)

groups = ([range(nu_groups)[i] for i in label])

print 'group | sno | station_name'
for i in range(len(features)):
    print str(groups[i])+'|'+str(station_nu[i])+'|'+str(station_name[i])

# close the database, plt and pdf-pages
db.close()
