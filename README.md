python-operative
=========
**python-operative** is a very light-weight Python bridge to the Operative FTP flatfile system.

Setup
-----

Setup virtualenv:
```
$ mkvirtualenv --distribute python-operative
$ workon python-operative
```

Run installation script:
```
$ python setup.py install
```

Testing
-------

There are two options for running the tests.
If you prefer not to test using a live FTP endpoint, then you can use the caliendo cache instead.

###Using Live FTP endpoint

Copy default settings file:
```
cp operative/settings.py.default operative/settings.py
```
Update the settings.py file with your own FTP credentials

###Using caliendo cache

Set caliendo env vars:
```
$ export USE_CALIENDO=True
$ export CALIENDO_CACHE_PREFIX=/absolute/path/to/caliendo/dir
```

Run tests:
```
$ python setup.py nosetests
```

Usage
-----

Using **python-operative** to retrieve data from an Operative flatfile report is very straightforward.

First step is to define an FTPCredentials object:
```python
import operative

FTP_LOGIN_DICT = {
    'host': <str>,
    'port': <optional int>,
    'username': <str>,
    'password': <str>}

ftp_creds = operative.FTPCredentials(**FTP_LOGIN_DICT)
```

From there you can pull an array of Report objects:
```python
import datetime
from operative.reports.line_item_report import LineItemReport

since = datetime.datetime.today() - datetime.timedelta(days=1)
path = '/flatfile'

line_item_reports = LineItemReport().get_report_files(ftp_credentials=ftp_creds, ftp_path=path, since=since)
```

Each Report object has a 'data' array attribute that represents the rows in the report.
Each item in the 'data' array is a **python-operative** model. In the case of this example, they would be LineItem models.

See the [model definitions](https://github.com/buzzfeed/python-operative/blob/master/operative/models/__init__.py) for more info.

Extending / Contributing
------------------------

If you need to represent an Operative object that is not currently supported, then simply add it to the [model definitions](https://github.com/buzzfeed/python-operative/blob/master/operative/models/__init__.py).

If you need a report that is currently not supported, then add it to the [report definitions](https://github.com/buzzfeed/python-operative/tree/master/operative/reports).
