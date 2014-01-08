python-operative
=========


##Setup

###Development

Setup virtualenv using virtualenvwrapper:

	makevirtualenv python-operative
	workon python-operative


###Installation

Run setup script:

	python setup.py install

Copy default settings file:

	cp operative/settings.py.default operative/settings.py

Run tests:

	python setup.py nosetests


###Settings

Update settings file with your own:

- Operative FTP login


####Error options:
All default to False
MISSING_COLUMN_ERROR
EXTRA_COLUMN_ERROR




