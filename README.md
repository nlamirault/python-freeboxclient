# Python Freebox Client [![Build Status](https://travis-ci.org/nlamirault/python-freeboxclient.png)](https://travis-ci.org/nlamirault/python-freeboxclient) [![Dependency Status](https://gemnasium.com/nlamirault/python-freeboxclient.png)](https://gemnasium.com/nlamirault/python-freeboxclient) [![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/nlamirault/python-freeboxclient/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

This tools is a Command Line Interface to manage the
[Freebox V6](http://www.free.fr/adsl/index.html).

## Install

* Install Python tools:

        $ apt-get install python-pip
		$ pip install virtualenvwrapper
		$ source /usr/local/bin/virtualenvwrapper.sh

* Install dependencies :

        $ mkvirtualenv freeboxclient
		New python executable in python-freeboxclient/bin/python
		Installing Setuptools..................done.
		Installing Pip.........................done.
        $ pip install -r requirements.txt


## Development

* Unit tests using [Tox](http://tox.testrun.org/):

        $ tox

* Code coverage:

        $ tox -ecoverage


## Documentation

This documentation is written by contributors, for contributors.
The source is maintained in the *doc/source* folder using
[reStructuredText](http://docutils.sourceforge.net/rst.html)
and built by [Sphinx](http://sphinx-doc.org/)

Building Manually:

    $ sphinx-build -b html doc/source build/sphinx/html

Results are in the *build/sphinx/html* directory.

Documentation for **python-freeboxclient** is hosted on
[readthedocs.org](http://readthedocs.org/docs/python-freeboxclient/en/latest/).


## ChangeLog

A changelog is available [here](ChangeLog.md).


## Contact

Nicolas Lamirault <nicolas.lamirault@gmail.com>
