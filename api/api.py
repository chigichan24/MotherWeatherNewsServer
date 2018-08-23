from flask import *
import api.exception as myex

app = Blueprint('api', __name__, url_prefix='/api/v1')

def try_request(func):
    try:
        ret = func()
    except ValueError:
        exception = myex.MethodNotAllowException()
        return exception.respnse()
    except Exception:
        exception = myex.InternalServerException()
        return exception.response()
    return ret
