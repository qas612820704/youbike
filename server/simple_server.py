import os
import json
from SETTINGS import BASE_DIR, SAVE_FILE_DIR
from bottle import Bottle, run, template, static_file
from bottle import TEMPLATE_PATH

SERVER_DIR = os.path.join(BASE_DIR, 'server')
SERVER_VIEW_DIR = os.path.join(SERVER_DIR, 'views')
SERVER_STATIC_DIR = os.path.join(SERVER_DIR, 'bower_components')

TEMPLATE_PATH.append(SERVER_VIEW_DIR)
app = Bottle()

@app.route('/')
def index():
    json_list = []
    for f in os.listdir(SAVE_FILE_DIR):
        if f.endswith(".json"):
            json_list.append(f.replace('.json', ''))
    json_list.sort()

    return template('index', json_list = json_list)

@app.route('/<json_file>/')
def json_f(json_file):
    # with open(SAVE_FILE_DIR + '/' + json_file + '.json') as f:
    #     data = json.loads(f.read())
    return template('json_view', json_file=json_file + '.json')

@app.route('/static/<path:path>')
def static(path):
    return static_file(path, root=SERVER_STATIC_DIR)

@app.route('/<json_file>')
def json_file(json_file):
    return static_file(json_file, root=SAVE_FILE_DIR)
run(app, host='140.113.208.132', port="8080")
