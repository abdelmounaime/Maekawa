from threading import Thread

from flask import Flask
from mutex import run_mutex
from threading import Thread

import time
app = Flask(__name__)

@app.route('/start')
def hello_world():
    cs_int = 5000
    next_req = 10
    tot_exec_time = 3600
    mutex_thread = Thread(
        target=run_mutex,
        args=(cs_int, next_req, 1),
    )
    mutex_thread.daemon = True
    mutex_thread.start()
    time.sleep(tot_exec_time)
    return 'Hello World!'

@app.route('/xhr')
def print_output():
    return str



if __name__ == '__main__':
    app.run()
