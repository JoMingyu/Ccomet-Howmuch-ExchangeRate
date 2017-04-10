from flask_restful import Resource


class Test(Resource):
    def get(self):
        data = {'asdf': {'sdff': 123}}
        return data
