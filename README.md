opair
=====

a web-app focuses on massive group-discussion

Dev environment prepare
=====
- virtualenv with python 2.7.x
- pip install flask
- sudo port install libevent
- CFLAGS="-I /opt/local/include -L /opt/local/lib" pip install gevent
  - [Refer to...](http://stackoverflow.com/questions/7630388/how-can-i-install-the-python-library-gevent-on-mac-os-x-lion)
- pip install sqlalchemy
- pip install tornado
- prepare javascript dev
  - sudo port install npm
  - npm install bower
  - npm install grunt
    - install compass
      - sudo port install ruby (kind of mess, but ruby is required by compass, and compass is required by grunt)
      - gem install compass
  - Yeman
    - npm install -g yo
    - npm install -g generator-webapp
    - install generators
      - npm install -g generator-angular generator-karma
