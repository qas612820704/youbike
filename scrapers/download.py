import os
import SETTINGS
from datetime import datetime
from time import sleep
import requests

print ("Download Starting")
while True:
  save_file_name = os.path.join(SETTINGS.SAVE_FILE_DIR , datetime.now().strftime("%Y-%m-%d_%H-%M") + '.json')
  data = requests.get(SETTINGS.YOUBIKE_DATA_URL).content.decode('utf-8')
  with open(save_file_name, 'w+') as f:
    f.write(data)
  print ("{} is saved".format(save_file_name))
  sleep(300)
