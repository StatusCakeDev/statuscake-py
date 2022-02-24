statuscake-py |build|
=====================

**NOTE**: This library is in alpha and not production ready. Whilst it can be
used we will not offer support until it is generally available.

The Python implementation of the `StatusCake API
<https://www.statuscake.com/api/v1>`_ client. Documentation for this library
can be found `here <https://www.statuscake.com/api/v1>`_.

Prerequisites
-------------

You will need the following things properly installed on your computer.

* `Python <https://www.python.org/>`_: any one of the **three latest major**
  `releases <https://www.python.org/download/releases/3.0/>`_

Installation
------------

PyPi
----

Using `PyPi <https://pypi.org/project/statuscake-py/>`_, add the following
to ``requirement.txt``:

.. code:: python

   statuscake_py

And then execute:

.. code:: bash

    $ pip install -r requirements.txt

Or install it yourself:

.. code:: bash

    $ pip install statuscake_py

GitHub
------

Installing the latest version from Github:

.. code:: bash

    $ git clone https://github.com/StatusCakeDev/statuscake-py
    $ cd statuscake-py
    $ python setup.py install

Usage
-----

Import the module from any Python file, instantiate an API client and execute a
request:

.. code:: python

   from statuscake import ApiClient
   from statuscake.apis import (
       ContactGroupApu,
       LocationsApi,
       MaintenanceWindowsApi,
       PagespeedApi,
       SslApi,
       UptimeApi,
   )

   client = ApiClient(
      header_name='Authorization',
      header_value='Bearer %s' % api_token,
   )

   service = UptimeApi(api_client=client)
   service.list_uptime_tests()

License
-------

This project is licensed under the `MIT License <LICENSE.txt>`_.

.. |build| image:: https://github.com/StatusCakeDev/statuscake-py/workflows/test/badge.svg
