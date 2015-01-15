from __future__ import absolute_import
from .core import Core
from ..model.user import User
from ..util import hash_password


g = Core()


@g.app.task()
def create_user(email, password):
    """
    """

    # check if this email is already used.
    q = User.objects(User.email == email)
    u = q.first()
    if u:
        if u.password == hash_password(password):
            login_user(u)

