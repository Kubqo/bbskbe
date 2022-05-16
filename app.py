from datetime import datetime
import json
from flask import Flask, request, render_template


app = Flask(__name__)


fakeDBcoordinates = []
fakeDBorders = []	


@app.route('/gps', methods=['GET', 'POST'])
def date():
    fakeDBcoordinates.append(request.json)
    return {'status': 'ok'}, 200

@app.route('/orders', methods=['GET', 'POST'])
def date():
    fakeDBorders.append(request.json)
    return {'status': 'ok'}, 200


@ app.route('/delete', methods=['GET', 'POST'])
def delete():
    fakeDBcoordinates.clear()
    return 'fakeDBcoordinates is empty', 200


@ app.route('/', methods=['GET', 'POST'])
def home():
    res = ''

    for i in range(len(fakeDBcoordinates)-1, -1, -1):
        res += "<p>" + fakeDBcoordinates[i]['latitude'] + ' ' + fakeDBcoordinates[i]['longitude'] + \
            ' ' + fakeDBcoordinates[i]['date'] + ' ' + fakeDBcoordinates[i]['time'] + "</p>"


    return render_template('index.html', coors=res, orders=fakeDBorders) 



if __name__ == '__main__':
    app.run()
