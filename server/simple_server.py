import os
from SETTINGS import BASE_DIR, SAVE_FILE_DIR
from bottle import Bottle, run, template, static_file
from bottle import TEMPLATE_PATH

TEMPLATE_PATH.append(BASE_DIR + '/server/')
app = Bottle()

@app.route('/')
def index():
    json_list = []
    for f in os.listdir(SAVE_FILE_DIR):
        if f.endswith(".json"):
            json_list.append(f)
    json_list.sort()

    return template('./index', json_list = json_list)
@app.route('/<json_file>')
def json_file(json_file):
    return static_file(json_file, root=SAVE_FILE_DIR)
run(app, host='140.113.208.132', port="8080")
