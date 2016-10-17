import os
import SETTINGS
from datetime import datetime
from time import sleep
import requests

print ("Download Starting")
while True:
  data = None
  save_file_name = os.path.join(SETTINGS.SAVE_FILE_DIR , datetime.now().strftime("%Y-%m-%d_%H-%M") + '.json')
  for _ in range(3):
    try:
      data = requests.get(SETTINGS.YOUBIKE_DATA_URL).content.decode('utf-8')
      break
    except:
      pass
  if not data is None:
    with open(save_file_name, 'w+') as f:
      f.write(data)
    print ("{} is saved".format(save_file_name))
  else:
    print ("Data is None, requests error");
  sleep(300)
