statuscake-py |build|
=====================

The `Python <https://www.python.org/>`_ implementation of the `StatusCake API
<https://developers.statuscake.com/api/>`_ client. Documentation for this
library can be found on the `StatusCake Developer Portal
<https://developers.statuscake.com/guides/sdks/introduction>`_.

Prerequisites
-------------

You will need the following things properly installed on your computer:

- `Python <https://www.python.org/>`_: any one of the **three latest major**
  `releases <https://www.python.org/downloads/>`_

Installation
------------

PyPi
----

Using `PyPi <https://pypi.org/project/statuscake-py/>`_, add the following
to ``requirement.txt``:

.. code:: text

   statuscake_py

And then execute:

.. code:: bash

    pip install -r requirements.txt

Or install it yourself:

.. code:: bash

    pip install statuscake_py

GitHub
------

Installing the latest version from Github:

.. code:: bash

    pip install git+https://github.com/StatusCakeDev/statuscake-py

Usage
-----

Import the module from any Python file, instantiate an API client and execute a
request:

.. code:: python

   import os

   from statuscake import Client, credentials, validation_errors

   client = Client(credentials.Bearer(os.environ["STATUSCAKE_API_TOKEN"]))

   try:
       tests = client.uptime.list_uptime_tests()
       print(tests.data)
   except Exception as e:
       print(e)
       print(validation_errors(e))

Examples
--------

The `examples <examples>`_ directory has a program for each kind of check, which
creates, reads, updates, lists and deletes it. They create resources in your
account, and delete them again before exiting:

.. code:: bash

   export STATUSCAKE_API_TOKEN=...
   python examples/uptime.py

License
-------

This project is licensed under the `MIT License <LICENSE.txt>`_.

.. |build| image:: https://github.com/StatusCakeDev/statuscake-py/workflows/test/badge.svg
