from __future__ import absolute_import
from ..api import login_serializer, sql
from flask.ext.login import UserMixin

class Users(UserMixin, sql.Model):
    """
    class Users

    only kept static information here. For dynamic info, ex. last-login,
    we would kept them in other table
    """
    id = sql.Column(sql.Integer, sql.Sequence('user_id_seq', start=1, increment=1), primary_key=True)
    email = sql.Column(sql.String(255), unique=True)
    password = sql.Column(sql.LargeBinary, nullable=False)

    def get_auth_token(self):
        return login_serializer.dumps(self.email, self.password)

