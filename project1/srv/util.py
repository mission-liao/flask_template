from werkzeug.utils import find_modules, import_string
from flask import Blueprint
import hashlib


def hash_password(password, secret):
    m = hashlib.sha1()
    m.update(password)
    return m.hexdigest()

def register_all_blueprints(app, blueprint_module):
    if blueprint_module:
        for name in find_modules(blueprint_module, include_packages=True, recursive=True):
            mod = import_string(name)
            for item_name in dir(mod):
                item = getattr(mod, item_name)
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)

