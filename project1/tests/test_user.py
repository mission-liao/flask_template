from __future__ import absolute_import
from ..tests import BaseTestCase
from flask import json


class UsersTestCase(BaseTestCase):
    """ test case for user resource """

    def test_signup(self):
        """ signup """
        # create new user
        rv = self.client.post('/r/user/', data=dict(
            email='ml',
            password='123'
        ))
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data)
        self.assertTrue(data['id'] > 0)

        # clean up
        rv = self.client.delete('/r/user/', query_string=dict(
            id=data['id'],
            password='123'
        ))
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data, '')

    def test_signup_with_duplicated_email(self):
        """ signup with duplicated email """
        # create first user
        rv = self.client.post('/r/user/', data=dict(
            email='ml',
            password='123'
        ))
        self.assertEqual(rv.status_code, 200)

        # cache id for later deletion
        data = json.loads(rv.data)
        _id = data['id']

        # create the same user 2nd time
        rv = self.client.post('/r/user/', data=dict(
            email='ml',
            password='456'
        ))
        self.assertEqual(rv.status_code, 409)

        # clean up
        rv = self.client.delete('/r/user/', query_string=dict(
            id=_id,
            password='123'
        ))
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data, '')

