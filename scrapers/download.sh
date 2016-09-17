#!/bin/bash

while [ 1   ]; do
  DATE=`date +%Y-%m-%d_%H-%M`
  wget --output-document youbike.json.gz http://data.taipei/youbike
  # gunzip youbike.json.gz
  # mv youbike.json data/$DATE.json
  mv youbike.json ../data/$DATE.json.gz
  # python upload.py $DATE
  echo $DATE
  sleep 60
done
