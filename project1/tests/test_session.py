from __future__ import absolute_import
from ..tests import BaseTestCase
from flask import json


class SessionTestCase(BaseTestCase):
    """ test case for session resource """

    @classmethod
    def setUpClass(kls):
        super(SessionTestCase, kls).setUpClass()

        # create a user
        rv = kls.client.post('/r/users/', data=dict(
            email='ml',
            password='123'
        ))
        if rv.status_code != 200:
            raise Exception('Unable to create user for testing')

        # cache user data for later clean-up
        kls.data = json.loads(rv.data)

    @classmethod
    def tearDownClass(kls):
        # clean up
        # to delete an account, we need to login first
        rv = kls.client.post('/r/session/', data=dict(
            email='ml',
            password='123'
        ))
        if rv.status_code != 200:
            raise Exception('Unablt to login user for testing')

        # delete account
        rv = kls.client.delete('/r/users/', query_string=dict(
            password='123'
        ))
        if rv.status_code != 200:
            raise Exception('Unable to delete user for testing')

        super(SessionTestCase, kls).tearDownClass()

    def test_login_and_logout(self):
        """ login success """
        # attemp to login
        rv = self.client.post('/r/session/', data=dict(
            email='ml',
            password='123'
        ))
        self.assertEqual(rv.status_code, 200)

        # clean up
        rv = self.client.delete('/r/session/')
        self.assertEqual(rv.status_code, 200)

    def test_login_fail(self):
        """ login failure, login with invalid password """
        rv = self.client.post('/r/session/', data=dict(
            email='ml',
            password='356'
        ))
        self.assertEqual(rv.status_code, 401)

