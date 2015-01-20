from __future__ import absolute_import
from ..tests import BaseTestCase
from flask import json


class UsersTestCase(BaseTestCase):

    def test_signup(self):
        # create new user
        rv = self.client.post('/r/users/', data=dict(
            username='ml',
            password='123'
        ))
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data)
        self.assertTrue(data['id'] > 0)

        # clean up
        rv = self.client.delete('/r/users/', query_string=dict(
            id=data['id'],
            password='123'
        ))
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data, '')

