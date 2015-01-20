from __future__ import absolute_import
from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask.ext.login import login_user, login_required, current_user, logout_user
from ..api import login_mgr, app, login_serializer, sql
from ..utils import hash_password
from ...srv import model


resource_session = Blueprint('session', __name__)


@login_mgr.token_loader
def load_token(token):
    """
    decrypt token and load User
    """
    max_age = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()

    data = login_serializer.loads(token, max_age=max_age)
    u = model.Users.query.filter_by(email=data[0]).first()

    if u and data[1] == u.password:
        return u
    return None


@login_mgr.user_loader
def load_user(uid):
    return model.Users.query.get(uid)


@login_mgr.unauthorized_handler
def unauthorized():
    return jsonify(error='not login'), 401


class SessionView(MethodView):
    """ Session resource
    """

    def post(self):
        """ a login attempt, email & password should be
        passed via post-data.
        """
        # try to create a new record in database
        q = sql.session.query(model.Users).filter(model.Users.email == request.form['email'])
        if q.count() == 0:
            return jsonify(error='User not exists'), 404

        u = q.first()
        if u:
            if u.password == hash_password(request.form['password'], app.secret_key):
                login_user(u)
                return jsonify(id=u.id, email=u.email, error=""), 200
            else:
                return jsonify(error="Password Wrong"), 401

        return jsonify(error='User not exists'), 404

    @login_required 
    def get(self):
        """ a login attempt via token stored in session-cookie
        """
        return jsonify(email=current_user.email), 200

    @login_required
    def delete(self):
        """ a logout attempt
        """
        logout_user()
        return "", 200

resource_session.add_url_rule('/r/session/', view_func=SessionView.as_view('resource-session'), methods=['GET', 'POST', 'DELETE'])

