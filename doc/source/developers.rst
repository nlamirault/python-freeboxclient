================
 For Developers
================

If you would like to contribute to **python-freeboxclient** directly, these instructions
should help you get started.  Patches, bug reports, and feature
requests are all welcome through the `GitHub project
<https://github.com/nlamirault/python-freeboxclient>`_.  Contributions in the form of
patches or pull requests are easier to integrate and will receive
priority attention.

Building Documentation
======================

The documentation for **python-freeboxclient** is written in ``rst``  and
converted to HTML using ``Sphinx``. The build itself is driven by make.
You will need the following packages in order to build the docs:

Once all of the tools are installed into a virtualenv using
pip, run ``make doc`` to generate the HTML version of the
documentation::

    $ make doc
    sphinx-build -b html -d build/doctrees   source build/html
    Running Sphinx v1.1.3
    loading pickled environment... done
    building [html]: targets for 1 source files that are out of date
    updating environment: 1 added, 1 changed, 0 removed
    reading sources... [100%] index
    looking for now-outdated files... none found
    pickling environment... done
    done
    preparing documents... done
    writing output... [100%] index
    writing additional files... genindex search
    copying static files... done
    dumping search index... done
    dumping object inventory... done
    build succeeded, 2 warnings.

    Build finished. The HTML pages are in build/html.

The output version of the documentation ends up in
``./doc/build/html`` inside your sandbox.

Running Tests
=============

.. image:: https://secure.travis-ci.org/nlamirault/python-freeboxclient.png?branch=master

The test suite for **python-freeboxclient** uses tox_, which must be installed separately
(``pip install tox``).

To run the tests under Python 2.7, run ``tox`` from the top
level directory of the git repository.

To run tests under a single version of Python, specify the appropriate
environment when running tox::

  $ tox -e py27

Add new tests by modifying an existing file or creating new script in
the ``tests`` directory.

.. _rst: http://docutils.sourceforge.net/rst.html

.. _tox: http://codespeak.net/tox

.. _developer-templates:

.. _Sphinx: http://sphinx-doc.org/
