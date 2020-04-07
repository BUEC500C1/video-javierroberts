from flask import Flask, request, jsonify, send_file
import feedTools
import json
import video as vd
import workers
import queue
import os

calls = -1

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "my-google-api-credentials.json"


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
