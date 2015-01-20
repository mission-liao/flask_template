import pytest
import os
from project1.srv import utils
from project1.srv.api import sql
from project1.srv import model # make sure all table definition are loaded

if __name__ == '__main__':
    # clear test db
    db_path = os.path.join(utils.get_root_path(), 'test.db')
    if os.path.isfile(db_path):
        os.remove(db_path)

    # make sure all table is created
    sql.create_all()

    pytest.main(['-s', '-v', '--cov=project1', '--cov-config=.converagerc', 'project1/tests'])

