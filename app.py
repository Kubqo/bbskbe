from datetime import datetime
import json
from flask import Flask, request, render_template
import threading


app = Flask(__name__)


fakeDBcoordinates = []
fakeDBorders = []	


@app.route('/gps', methods=['GET', 'POST'])
def date():
    fakeDBcoordinates.append(request.json)
    return {'status': 'ok'}, 200

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    fakeDBorders.append(request.json)
    return {'status': 'ok'}, 200


@ app.route('/delete', methods=['GET', 'POST'])
def delete():
    fakeDBcoordinates.clear()
    return 'fakeDBcoordinates is empty', 200


@ app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('main.html', coors=fakeDBcoordinates, orders=fakeDBorders) 



if __name__ == '__main__':
    app.run()
