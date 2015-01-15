from __future__ import absolute_import
from cqlengine import connection
from ..factory import create_celery_app
from ..util import Singleton


class Core(Singleton):
    """
    """

    def __init__(self, app=None):
        self.__app = create_celery_app()
        connection.setup(hosts=self.__app.conf['CQLENGINE_HOSTS'])

    @property
    def app(self):
        """
        celery app
        """
        return self.__app

