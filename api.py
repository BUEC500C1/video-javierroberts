from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import feedTools
import json


app = Flask(__name__)


@app.route('/<string:handle>/<int:count>')
def get(handle, count):
    return json.dumps(feedTools.getFeed(handle, count))


if __name__ == '__main__':
    app.run(debug=True)
