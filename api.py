from flask import Flask, request, jsonify, send_file
from flask_restful import Resource, Api, reqparse
import feedTools
import json
import video as vd


app = Flask(__name__)


@app.route('/<string:handle>')
def get(handle):
    try:
        vd.makeVideo(handle)
        return send_file("media/video.mp4")
    except:
        return "Error, please make sure handle is correct"


if __name__ == '__main__':
    app.run(debug=True)
