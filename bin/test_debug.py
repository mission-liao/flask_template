"""
this script allow debugging one test case

```
    pudb test_debug.py 
```

Step to patch this script for one test suite you need to debug.
(take project1.tests.test_user as example)
- modify the import string from `project1.tests.test_session` to `project1.tests.test_user`
- modify `SessionTestCase` to `UsersTestCase`

If you just want to run one test case, modify the parameter passed into makeSuite:
- modify 'test_' to 'test_login_fail' for example
"""


from __future__ import absolute_import
import unittest
import os
import sys
# add parent folder as module search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from project1.srv import utils
from project1.srv.api import sql
from project1.srv import model # make sure all table definition are loaded
from project1.tests.test_session import SessionTestCase as t


if __name__ == '__main__':
    # clear test db
    db_path = os.path.join(utils.get_root_path(), 'test.db')
    if os.path.isfile(db_path):
        os.remove(db_path)

    # make sure all table is created
    sql.create_all()

    unittest.TextTestRunner().run(
        unittest.makeSuite(t, 'test_')
    )

