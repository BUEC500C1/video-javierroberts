from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import feedTools


app = Flask(__name__)
api = Api(app)


class feedRetrieve(Resource):

    def get(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('handle', type=str, help='Twitter handle')
        # handle = parser.parse_args()
        return feedTools.getFeed()


api.add_resource(feedRetrieve, '/')

if __name__ == '__main__':
    app.run(debug=True)
