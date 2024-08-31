"""
    StatusCake API

    Copyright (c) 2023

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or  sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.

    API Version: 1.2.0
    Contact: support@statuscake.com

    Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.
"""


import codecs
from setuptools import setup, find_packages  # noqa: H301

NAME = 'statuscake_py'
VERSION = '1.2.0-beta.1'
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    'urllib3~=2.2.1',
    'python-dateutil~=2.5.3',
]

TESTS_REQUIRE = [
    'pytest~=7.1.3',
]


# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name=NAME,
    version=VERSION,
    description='StatusCake API',
    author='StatusCake',
    author_email='support@statuscake.com',
    url='https://github.com/StatusCakeDev/statuscake-py',
    keywords=[
        'python',
        'sdk',
        'statuscake',
    ],
    python_requires='>=3.6',
    install_requires=REQUIRES,
    tests_require=TESTS_REQUIRE,
    packages=find_packages(exclude=['test', 'tests']),
    include_package_data=True,
    license='MIT',
    long_description=long_description
)
