# coding=utf-8
from functools import wraps
from flask import abort
from flask_login import current_user
from app.models import Permission


def permission_require(permission):
    def decorators(f):
        @wraps(f)
        def decorators_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorators_function

    return decorators


def admin_required(f):
    return permission_require(Permission.ADMINISTER)(f)
