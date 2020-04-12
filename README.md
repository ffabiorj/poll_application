[![Build Status](https://travis-ci.com/ffabiorj/poll_application.svg?branch=master)](https://travis-ci.com/ffabiorj/poll_application)
[![Coverage Status](https://coveralls.io/repos/github/ffabiorj/poll_application/badge.svg?branch=master)](https://coveralls.io/github/ffabiorj/poll_application?branch=master)
# POLL APP

### Running 
Within a _virtualenv_ just install the dependencies and run database migrations before launching the server:

```console
$ python3 -m venv .venv
$ sourch .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

### Testing (with [`coverage`](https://coverage.readthedocs.io/) and HTML report)

Run the tests with `coverage`, generate and open a HTML report:

```
$ coverage run manage.py test
$ coverage html
$ open htmlcov/index.html
```
