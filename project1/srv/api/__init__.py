from __future__ import absolute_import
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from ..util import register_all_blueprints
from ..factory import create_app, create_rest_app

# globals to avoid import error
app = create_app()
login_mgr = LoginManager()
# session encrypt/decrypt
login_serializer = URLSafeTimedSerializer(app.secret_key)

# real initialization
app = create_rest_app(app=app)

# put everything that need to be initialized with flask-object here.
# -- flask-login
login_mgr.init_app(app)
# -- flask-sqlalchemy
sql = SQLAlchemy(app)

# register blue-prints
register_all_blueprints(app, blueprint_module='project1.srv.api')

