from bottle import Bottle, JSONPlugin

import datetime
import decimal
import json


class JSONEncoder(json.JSONEncoder):

    def default(self, object):
        if isinstance(object, datetime.date):
            return object.isoformat()
        if isinstance(object, datetime.datetime):
            return object.isoformat()
        if isinstance(object, decimal.Decimal):
            return float(object)
        return json.JSONEncoder.default(self, object)


def create_application():
    application = Bottle()
    application.install(JSONPlugin(json_dumps=lambda object: json.dumps(object, cls=JSONEncoder)))
    return application
