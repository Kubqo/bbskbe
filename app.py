from datetime import datetime
import json
from flask import Flask, request

app = Flask(__name__)

fakeDB = []


@app.route('/gps', methods=['GET', 'POST'])
def date():
    content_type = request.headers.get('Content-Type')

    # if (content_type == 'application/json'):
    now = datetime.now()
    string_date = now.strftime("%m/%d/%Y")
    string_time = now.strftime("%H:%M:%S")

    print(string_date + string_time)
    print(request.json)
    fakeDB.append(
        {**request.json, "date": string_date, "time": string_time})
    print(fakeDB)
    return {'date': string_date, 'time': string_time}, 200
    # else:
    #     return 'Content-Type not supported!'


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    for _ in fakeDB:
        fakeDB.pop()
    fakeDB.pop()
    return 'fakeDB is empty', 200


@app.route('/', methods=['GET', 'POST'])
def home():
    res = ''

    for i in range(len(fakeDB)-1, -1, -1):
        res += "<p>" + fakeDB[i]['latitude'] + ' ' + fakeDB[i]['longitude'] + \
            ' ' + fakeDB[i]['date'] + ' ' + fakeDB[i]['time'] + "</p>"

    return res, 200


if __name__ == '__main__':
    app.run()
