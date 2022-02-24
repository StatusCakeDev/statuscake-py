statuscake-py
=============

This README outlines the details of collaborating on this Python module. A
short introduction of this module could easily go here.

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
