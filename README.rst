Python Freebox Client
=====================

.. image:: https://badge.fury.io/py/python-freeboxclient.png
    :target: http://badge.fury.io/py/python-freeboxclient

.. image:: https://pypip.in/d/python-freeboxclient/badge.png
    :target: https://crate.io/packages/python-freeboxclient

.. image:: https://travis-ci.org/nlamirault/python-freeboxclient.png
    :target: http://travis-ci.org/nlamirault/python-freeboxclient

.. image:: https://app.wercker.com/status/3fad72a1bb6196a9ab3093bcf60cf7b4
    :target: https://app.wercker.com/project/bykey/3fad72a1bb6196a9ab3093bcf60cf7b4

.. image:: https://drone.io/github.com/nlamirault/python-freeboxclient/status.png
    :target: http://drone.io/github.com/nlamirault/python-freeboxclient/latest

.. image:: https://coveralls.io/repos/nlamirault/python-freeboxclient/badge.png?branch=master
    :target: https://coveralls.io/r/nlamirault/python-freeboxclient?branch=master

.. image:: https://gemnasium.com/nlamirault/python-freeboxclient.png
    :target: https://gemnasium.com/nlamirault/python-freeboxclient

.. image:: https://d2weczhvl823v0.cloudfront.net/nlamirault/python-freeboxclient/trend.png
    :target: https://bitdeli.com/free

.. image:: https://badge.waffle.io/nlamirault/python-freeboxclient.png?label=ready
    :target: http://waffle.io/nlamirault/python-freeboxclient

This tools is a Command Line Interface to manage the FreeboxV6_

Install
-------

* Install Python tools:

.. code-block:: bash

        $ apt-get install python-pip
        $ pip install virtualenvwrapper
        $ source /usr/local/bin/virtualenvwrapper.sh

* Install dependencies :

.. code-block:: bash

        $ mkvirtualenv freeboxclient
	New python executable in python-freeboxclient/bin/python
	Installing Setuptools..................done.
	Installing Pip.........................done.
        $ pip install -r requirements.txt


Development
-----------

* Unit tests using Tox_

.. code-block:: bash

        $ tox

* Code coverage:

.. code-block:: bash

        $ tox -ecoverage


Documentation
-------------

This documentation is written by contributors, for contributors.
The source is maintained in the *doc/source* folder using
reStructuredText_ and built by Sphinx_

Building Manually:

.. code-block:: bash

        $ sphinx-build -b html doc/source build/sphinx/html

Results are in the *build/sphinx/html* directory.

Documentation is available at: http://readthedocs.org/docs/python-freeboxclient/en/latest


Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :)
#. Make sure to add yourself to AUTHORS_.

ChangeLog
---------

A changelog is available ChangeLog_.


Contact
-------

Nicolas Lamirault <nicolas.lamirault@gmail.com>


.. _FreeboxV6: http://www.free.fr/adsl/index.html
.. _Tox: http://tox.testrun.org
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org
.. _`the repository`: http://github.com/nlamirault/python-freeboxclient
.. _ChangeLog: http://github.com/nlamirault/python-freeboxclient/blob/master/ChangeLog.md
.. _AUTHORS: http://github.com/nlamirault/python-freeboxclient/blob/master/AUTHORS.rst
