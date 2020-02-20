from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import feedTools


app = Flask(__name__)


@app.route('/<string:handle>/<int:count>')
def get(handle, count):
    return feedTools.getFeed(handle, count)


app.run()

if __name__ == '__main__':
    app.run(debug=True)
