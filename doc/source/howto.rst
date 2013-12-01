=======
 Howto
=======

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

	$ freeboxos freebox authorize


Track authorization progress
----------------------------

The app should monitor the status until it is different from pending::

	$ freeboxos freebox authorization_status


Open a session
--------------

Once you have the authorization for your application, you just need to
start a new session::

	$ freeboxos freebox start_session


Close a session
---------------

To close the current session you can use the following call::

	$ freeboxos freebox stop_session
