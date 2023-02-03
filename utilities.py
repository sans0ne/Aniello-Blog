from flask import abort
from flask_login import current_user
from functools import wraps


def admin_only(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        else:
            return function(*args, **kwargs)
    return wrapper_function
