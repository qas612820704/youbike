# -*- coding: utf-8 -*-
import pandas as pd
import json

with open('youbike.json') as data_file:
    data = json.load(data_file)

stations = data['retVal']
station_id = [ k for k in stations ]
station_value = [ v for v in stations.values() ]

station_df = pd.DataFrame(station_value)
station_df['id'] = station_id
