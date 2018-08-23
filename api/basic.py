from flask import *
import api.exception as myex

app = Blueprint('basic', __name__, url_prefix='/api/v1')

def try_request(func):
    try:
        ret = func()
    except ValueError:
        exception = myex.MethodNotAllowException()
        return exception.respnse()

    return ret
