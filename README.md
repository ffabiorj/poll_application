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
