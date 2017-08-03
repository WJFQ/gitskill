#检查用户权限的自定义修饰器 page101

from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args,**kwargs):
            if not current_user.can(permission):
                abort(403)
                #这里要写403.html
                #如果用户不具有指定权限，则返回403错误码
            return f(*args,**kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
