from __future__ import absolute_import
from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask.ext.login import login_user, login_required, current_user, logout_user
from .rest import login_mgr, app, login_serializer
from ..srv import model
from datetime import datetime

api_user = Blueprint('user', __name__)


@login_mgr.token_loader
def load_token(token):
    """
    decrypt token and load User
    """
    max_age = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()

    data = login_serializer.loads(token, max_age=max_age)
    u = model.User.query.filter_by(email=data[0]).first()

    if u and data[1] == u.password:
        return u
    return None


@login_mgr.user_loader
def load_user(uid):
    return model.User.query.get(uid)


@login_mgr.unauthorized_handler
def unauthorized():
    return '', 401


class LoginView(MethodView):
    def post(self):
        """
        a login attempt, email & password should be
        passed via post-data.
        """
        # try to create a new record in database
        data = request.get_json()

        u = model.User.query.filter_by(email=data['email']).first()
        if u:
            if u.password == hash_password(data['password']):
                login_user(u)
                return jsonify(id=u.id, email=u.email, error=""), 200
            else:
                return jsonify(error="Password Wrong"), 401

        return jsonify(error="User not exists"), 404

    @login_required 
    def get(self):
        """
        a login attempt via token stored in session-cookie
        """
        return jsonify(email=current_user.email), 200


class LogoutView(MethodView):
    def get(self):
        """
        a logout attempt
        """
        logout_user()
        return "", 200

class UserView(MethodView):
    def get(self):
        """
        get a specific user resource
        """
        pass

    def post(self):
        """
        submit function to create new user.
        """
        status_code = 200
        err = ""
        # try to create a new record in database
        data = request.get_json()

        # convert date string to date object
        d = datetime.strptime(data['bday'], '%Y-%m-%d')
        # create User object
        # TODO: input validation
        u = model.User(
            email = data['email'],
            bDay = d.date(),
            password = hash_password(data['password']),
            joinTime = datetime.now(),
            gender = data['gender'],
            nation = data['loc']
        )

        sql.session.add(u)
        try:
            sql.session.commit()
        except IntegrityError:
            # the email already used
            sql.session.rollback()

            # error code for conflict
            status_code = 409
            err = "this email already exists"

        # perform login when new account created
        login_user(u)

        return jsonify(id=u.id, error=err), status_code


api_user.add_url_rule('/r/users/', view_func=UserView.as_view('res-user'), methods=['GET', 'POST', ])
api_user.add_url_rule('/p/users/login/', view_func=LoginView.as_view('api-login'), methods=['GET', 'POST', ])
api_user.add_url_rule('/p/users/logout/', view_func=LogoutView.as_view('api-logout'), methods=['GET', ])

