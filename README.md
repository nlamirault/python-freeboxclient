Python Freebox Client
======================

This tools is a client to manage the FreeboxV6.

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
