import os

# Project Directory

HOST, PORT = '0.0.0.0', '8888'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# YouBike Data Url
YOUBIKE_DATA_URL = 'http://data.taipei/youbike'

# SAVE FILE DIR
SAVE_FILE_DIR = os.path.join(BASE_DIR, 'data')

if not os.path.exists(SAVE_FILE_DIR):
    os.makedirs(SAVE_FILE_DIR)

#
