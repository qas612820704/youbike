#!/bin/sh

while [ 1 ]; do
    python database_scraper.py http://210.69.61.60:8080/you/gwjs_cityhall.json
    echo update
    sleep 300
done
