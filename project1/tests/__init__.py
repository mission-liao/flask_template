import unittest
from ..srv.api import app

class BaseTestCase(unittest.TestCase):
    """ base test case
    """

    @classmethod
    def setUpClass(kls):
        kls.client = app.test_client(use_cookies=True)

