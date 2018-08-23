import sys
import traceback
from flask import Flask, jsonify

class MyException(Exception):

    @classmethod
    def __call__(cls, message=None):
        cls.error_message = message
        return cls

    @classmethod
    def response(cls):
        traceback.print_exc()
        return jsonify (
            {'error': str(cls.error_message)}
        ), cls.status_code

class MethodNotAllowedException(MyException):
    status_code = 405
    error_message = 'parse error. json format is not correct.'

class InternalServerException(MyException):
    status_code = 500
    error_message = 'unknown error.'
