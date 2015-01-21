from __future__ import absolute_import
from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask.ext.login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from ..api import sql, app
from ..utils import hash_password
from ...srv import model


resource_user = Blueprint('user', __name__)


class UserView(MethodView):
    """ User resource
    """

    def post(self):
        """ submit function to create new user.
        """
        status_code = 200
        err = ''
        # create User object
        # TODO: input validation
        u = model.Users(
            email=request.form['email'],
            password=hash_password(request.form['password'], app.secret_key)
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

        if err == '':
            # perform login when new account created
            login_user(u)

        return jsonify(id=u.id, error=err), status_code

    @login_required
    def delete(self):
        """ delete user """
        # TODO: should we allow user to be deleted?
        # make sure that user exists
        q = sql.session.query(model.Users).filter(model.Users.email == current_user.email)
        if q.count() == 0:
            return '', 404

        u = q.first()

        # make sure password ok
        if hash_password(request.args.get('password'), app.secret_key) != u.password:
            return '', 401

        logout_user()

        # delete User
        sql.session.delete(u)
        sql.session.commit()

        return '', 200


resource_user.add_url_rule('/r/user/', view_func=UserView.as_view('res-user'), methods=['GET', 'POST', 'DELETE'])

