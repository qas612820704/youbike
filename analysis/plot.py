# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import MySQLdb
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.dates as dates
from datetime import datetime

# Get the information from the user
stationlist = []
print 'What is the first date?',
first_date = input()
print 'Which day is the first date? (Enter a number from 1 to 7) ',
first_day = input()
days_to_draw = 7
"""
print "What stations do you want to draw? (If you finished, type 'end') "
while True:
    input_station = raw_input()
    if input_station == 'end':
        break
    else: stationlist.append(int(input_station))
"""
for x in range(150):
    stationlist.append(x+1)
numberOfstation = len(stationlist)
print 'Drawing the picture......'

def date_to_week(date):
    return int(first_day)+((int(date)-int(first_date))%7)

station = {x:[\
{'label':'Monday','display':'b-','time':[],'space':[]},\
{'label':'Tuesday','display':'g-','time':[],'space':[]},\
{'label':'Wednesday','display':'r-','time':[],'space':[]},\
{'label':'Thursday','display':'c-','time':[],'space':[]},\
{'label':'Friday','display':'m-','time':[],'space':[]},\
{'label':'Saturday','display':'y-','time':[],'space':[]},\
{'label':'Sunday','display':'k-','time':[],'space':[]}] for x in range(numberOfstation)}

# Open database connection
db = MySQLdb.connect("localhost","youbikeuser","youbike","youbikedb")

# prepare a cursor object using cursor() method
cur = db.cursor()

# Initialize pdf document for later printing
pdf_pages = PdfPages('plot.pdf')
nb_plots = numberOfstation
nb_plots_per_page = 5
nb_pages = nb_plots/nb_plots_per_page
grid_size = (5,1)

# Get the x,y values from database and draw the fig
for stationNo in range(numberOfstation):
    # Prepare SQL query to SELECT
    sql = "select * from individual_level where sno='%d' order by mday" % stationlist[stationNo]
    # Execute the SQL command
    cur.execute(sql)
    # Fetch the rows in a list of lists.
    results = cur.fetchall()
    title = results[0][2]
    titleTime = str(results[0][6])[0:4]+'-'+str(results[0][6])[4:6]
    for row in results:
        sbi = int(row[5])
        mday = str(row[6])

        day = mday[6:8]
        hour = mday[8:10]
        min = mday[10:12]
        sec = mday[12:14]
        timestring = hour+':'+min+':'+sec
        station[stationNo][date_to_week(day)-1]['time'].append(timestring)
        station[stationNo][date_to_week(day)-1]['space'].append(sbi)
    # Check whether we need to start a page
    if stationNo % nb_plots_per_page == 0:
        fig = plt.figure(figsize=(11,17),dpi=100)

    # Actually plot the things
    ax = plt.subplot2grid(grid_size, (stationNo % nb_plots_per_page,0))
    for i in range(days_to_draw):
        x = [datetime.strptime(date, '%H:%M:%S') for date in station[stationNo][i]['time']]
        y = station[stationNo][i]['space']
        ax.plot(x,y,station[stationNo][i]['display'],label=station[stationNo][i]['label'])

    # Setup the fig
    plt.legend(fontsize='small')
    plt.grid()
    station_name = unicode(title,errors='ignore')+'  '+titleTime
    ax.set_title(station_name)
    plt.xlabel('Time of Day')
    plt.ylabel("Number of available bikes")
    ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
    plt.setp(plt.xticks()[1], rotation=30)

    # Close the page if needed
    if (stationNo + 1) % nb_plots_per_page == 0 or (stationNo + 1) == nb_plots:
        plt.tight_layout()
        pdf_pages.savefig(fig)

# close the database, plt and pdf-pages
db.close()
plt.close()
pdf_pages.close()
