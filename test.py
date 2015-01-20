import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-v', '--cov=project1', '--cov-config=.converagerc', 'project1/tests'])
