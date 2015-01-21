what's inside?
==============
- MVC
  - REST in `json` as 'V', therefore no html/css/template-engine
  - `project1/srv/model` for 'M'
  - `project1/srv/api` for 'C'
- a very basic user-related logic, including: signUp, login/logout
- unittest `project1/srv/tests`
- A swagger doc to describe APIs `docs/api/swagger.json`
- easy environment preparation via pip and env/requirements-dev.txt

commands
==============
prepare develop environment
```
	pip install -r env/requirements-dev.txt
```

launch server
```
	python bin/run.py
```

unittest
```
	python bin/test.py
```

debug
```
	pudb bin/test_debug.py
```
