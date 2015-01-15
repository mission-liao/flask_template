from werkzeug.utils import find_modules, import_string
from flask import Blueprint
import hashlib


def hash_password(password):
    m = hashlib.sha1()
    m.update(password)
    m.update(app.secret_key)
    return m.hexdigest()

def register_all_blueprints(app, blueprint_module):
    if blueprint_module:
        for name in find_modules(blueprint_module, include_packages=True, recursive=True):
            mod = import_string(name)
            for item_name in dir(mod):
                item = getattr(mod, item_name)
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)


class _Singleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Singleton(_Singleton('SingletonMeta', (object,), {})):
    """
    a singleton implementation, refer to
        http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    """
    pass
