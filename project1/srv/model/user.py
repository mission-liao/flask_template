from __future__ import absolute_import
from ..rest import login_serializer, db
from flask.ext.login import UserMixin

class User(UserMixin, db.Model):
    """
    class User

    only kept static information here. For dynamic info, ex. last-login,
    we would kept them in other table
    """
    id = db.Column(db.Integer, db.Sequence('user_id_seq', start=1, increment=1), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.LargeBinary, nullable=False)

    def get_auth_token(self):
        return login_serializer.dumps(self.email, self.password)

