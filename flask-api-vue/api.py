from flask_restful import Resource

ticker = 0


class Ticker(Resource):

    def get(self):
        global ticker
        ticker += 1
        return {'tick': ticker}
