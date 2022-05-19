from datetime import datetime
import json
from flask import Flask, request, render_template, session
from flask_socketio import SocketIO, emit
import requests
from threading import Lock

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


url = 'http://127.0.0.1:5000/getData'
productionUrl = 'https://inqool.jakubduris.com/getData'

fakeDBcoordinates = []
fakeDBorders = []


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(1)
        count += 1
        orders = ((requests.get(productionUrl)).json())['orders']
        coors = ((requests.get(productionUrl)).json())['coors']
        socketio.emit('my_response',
                      {'orders': orders, 'coors': coors})


@socketio.event
def my_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@app.route('/gps', methods=['GET', 'POST'])
def gps():
    fakeDBcoordinates.append(request.json)
    return {'status': 'ok'}, 200


@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
    fakeDBorders.append(request.json)
    return {'status': 'ok'}, 200


@app.route('/getData', methods=['GET', 'POST'])
def getData():
    return {'status': 'ok', 'orders': fakeDBorders,
            'coors': fakeDBcoordinates}, 200


@ app.route('/delete', methods=['GET', 'POST'])
def delete():
    fakeDBcoordinates.clear()
    fakeDBorders.clear()
    return 'fakeDBcoordinates is empty', 200


@ app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('main.html',  async_mode=socketio.async_mode, coors=fakeDBcoordinates, orders=fakeDBorders)


if __name__ == '__main__':
    socketio.run(app)
