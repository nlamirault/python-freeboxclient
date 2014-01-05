=======
 Howto
=======

Help
====

The CLI could display all available commands:

.. code-block:: bash

    $ freeboxos -h
    usage: freeboxos [--version] [-v] [--log-file LOG_FILE] [-q] [-h] [--debug]

    freeboxos

    optional arguments:
      --version            show program's version number and exit
      -v, --verbose        Increase verbosity of output. Can be repeated.
      --log-file LOG_FILE  Specify a file to log output. Disabled by default.
      -q, --quiet          suppress output except warnings and errors
      -h, --help           show this help message and exit
      --debug              show tracebacks on errors

    Commands:
      about          A command that prints information about this tool.
      config         A command that prints available configuration.
      [....]
      help           print detailed help for another command


Configuration
=============

Creates a personal configuration file in **$HOME/.config** directory::

.. code-block:: bash

  $ cat $HOME/.config/freeboxos.yml
  app_id: 'python-freeboxclient'
  app_name: 'Python-Freeboxclient'
  app_version: '0.1.0'
  device_name: 'Python-Freeboxclient-Laptop'


Autorization
============

Each application identified with an ``app_name`` must gain access to Freebox API
before being able to use the api.

This procedure can only be initiated from the local network, and the user must
have access to the Freebox front panel to grant access to the app.

Request authorization
---------------------

The app will ask for an authorization using the following call.
A message will be displayed on the Freebox LCD asking the user
to grant/deny access to the requesting app::

.. code-block:: bash

  $ freeboxos freebox authorize
  [FreeboxCmd] Authorization request
  Starting new HTTP connection (1): mafreebox.freebox.fr
  Accept this application. Look at the LCD screen.


Track authorization progress
----------------------------

The app should monitor the status until it is different from pending::

.. code-block:: bash

  $ freeboxos freebox approuved
  [FreeboxCmd] Check Authorization
  Application already granted on the FreeboxOS.


Login
-----

Before doing any requests to the Freebox OS, you must request a challenge:

.. code-block:: bash

  $ freeboxos freebox login
  [FreeboxCmd] Login
  Freebox Login OK


Open a session
--------------

Once you have the authorization for your application, you just need to
start a new session::

.. code-block:: bash

  $ freeboxos freebox session open
  [FreeboxCmd] Open sesion
  Freebox Session opened.


Close a session
---------------

To close the current session you can use the following call::

.. code-block:: bash

  $ freeboxos freebox stop_session
