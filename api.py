from flask import Flask, request, jsonify, send_file
from flask_restful import Resource, Api, reqparse
import feedTools
import json
import video as vd
import workers
import queue

calls = -1

app = Flask(__name__)


@app.route('/getvideo/<string:handle>')
def get(handle):
    global calls
    calls += 1

    t_id = calls % workers.NUMBER_THREADS
    workers.producer(handle, t_id)

    if calls == 0:
        workers.thread_init()
    while True:
        if (workers.done_list[t_id] == 1):
            return send_file("media/thread%s/video.mp4" % str(t_id))


if __name__ == '__main__':
    app.run(debug=True)
