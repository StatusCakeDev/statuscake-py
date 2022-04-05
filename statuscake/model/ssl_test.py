"""
    StatusCake API

    Copyright (c) 2022

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

    API Version: 1.0.0-beta.3
    Contact: support@statuscake.com

    Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.
"""


import re  # noqa: F401
import sys  # noqa: F401

from statuscake.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from statuscake.exceptions import ApiAttributeError


def lazy_import():
    from statuscake.model.ssl_test_check_rate import SSLTestCheckRate
    from statuscake.model.ssl_test_flags import SSLTestFlags
    from statuscake.model.ssl_test_mixed_content import SSLTestMixedContent
    globals()['SSLTestCheckRate'] = SSLTestCheckRate
    globals()['SSLTestFlags'] = SSLTestFlags
    globals()['SSLTestMixedContent'] = SSLTestMixedContent


class SSLTest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('certificate_score',): {
            'inclusive_maximum': 100,
            'inclusive_minimum': 0,
        },
        ('cipher_score',): {
            'inclusive_maximum': 100,
            'inclusive_minimum': 0,
        },
        ('last_reminder',): {
            'inclusive_minimum': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'website_url': (str,),  # noqa: E501
            'check_rate': (SSLTestCheckRate,),  # noqa: E501
            'alert_at': ([int],),  # noqa: E501
            'alert_broken': (bool,),  # noqa: E501
            'alert_expiry': (bool,),  # noqa: E501
            'alert_mixed': (bool,),  # noqa: E501
            'alert_reminder': (bool,),  # noqa: E501
            'contact_groups': ([str],),  # noqa: E501
            'follow_redirects': (bool,),  # noqa: E501
            'mixed_content': ([SSLTestMixedContent],),  # noqa: E501
            'paused': (bool,),  # noqa: E501
            'certificate_score': (int,),  # noqa: E501
            'certificate_status': (str,),  # noqa: E501
            'cipher': (str,),  # noqa: E501
            'cipher_score': (int,),  # noqa: E501
            'issuer_common_name': (str,),  # noqa: E501
            'flags': (SSLTestFlags,),  # noqa: E501
            'hostname': (str,),  # noqa: E501
            'last_reminder': (int,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'user_agent': (str,),  # noqa: E501
            'valid_from': (datetime,),  # noqa: E501
            'valid_until': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'id': 'id',  # noqa: E501
        'website_url': 'website_url',  # noqa: E501
        'check_rate': 'check_rate',  # noqa: E501
        'alert_at': 'alert_at',  # noqa: E501
        'alert_broken': 'alert_broken',  # noqa: E501
        'alert_expiry': 'alert_expiry',  # noqa: E501
        'alert_mixed': 'alert_mixed',  # noqa: E501
        'alert_reminder': 'alert_reminder',  # noqa: E501
        'contact_groups': 'contact_groups',  # noqa: E501
        'follow_redirects': 'follow_redirects',  # noqa: E501
        'mixed_content': 'mixed_content',  # noqa: E501
        'paused': 'paused',  # noqa: E501
        'certificate_score': 'certificate_score',  # noqa: E501
        'certificate_status': 'certificate_status',  # noqa: E501
        'cipher': 'cipher',  # noqa: E501
        'cipher_score': 'cipher_score',  # noqa: E501
        'issuer_common_name': 'issuer_common_name',  # noqa: E501
        'flags': 'flags',  # noqa: E501
        'hostname': 'hostname',  # noqa: E501
        'last_reminder': 'last_reminder',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'user_agent': 'user_agent',  # noqa: E501
        'valid_from': 'valid_from',  # noqa: E501
        'valid_until': 'valid_until',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, website_url, check_rate, alert_at, alert_broken, alert_expiry, alert_mixed, alert_reminder, contact_groups, follow_redirects, mixed_content, paused, *args, **kwargs):  # noqa: E501
        """SSLTest - a model defined in OpenAPI

        Args:
            id (str): SSL check ID
            website_url (str): URL of the server under test
            check_rate (SSLTestCheckRate):
            alert_at ([int]): List representing when alerts should be sent (days).
            alert_broken (bool): Whether to enable alerts when SSL certificate issues are found
            alert_expiry (bool): Whether to enable alerts when the SSL certificate is to expire
            alert_mixed (bool): Whether to enable alerts when mixed content is found
            alert_reminder (bool): Whether to enable alert reminders
            contact_groups ([str]): List of contact group IDs
            follow_redirects (bool): Whether to follow redirects when testing. Disabled by default
            mixed_content ([SSLTestMixedContent]): List of mixed content resources
            paused (bool): Whether the check should be run

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            certificate_score (int): SSL certificate score (%). [optional]  # noqa: E501
            certificate_status (str): SSL certificate status. [optional]  # noqa: E501
            cipher (str): SSL/TLS cipher suite belonging to the SSL certificate. [optional]  # noqa: E501
            cipher_score (int): SSL certificate cipher strength (%). [optional]  # noqa: E501
            issuer_common_name (str): Issuer of the SSL certificate. [optional]  # noqa: E501
            flags (SSLTestFlags): [optional]  # noqa: E501
            hostname (str): Hostname of the server under test. [optional]  # noqa: E501
            last_reminder (int): The last reminder to have been sent (days). [optional]  # noqa: E501
            updated_at (datetime): When the SSL certificate was last updated (RFC3339 format). [optional]  # noqa: E501
            user_agent (str): Custom user agent string set when testing. [optional]  # noqa: E501
            valid_from (datetime): SSL certificate validity start (RFC3339 format). [optional]  # noqa: E501
            valid_until (datetime): SSL certificate validity end (RFC3339 format). [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.website_url = website_url
        self.check_rate = check_rate
        self.alert_at = alert_at
        self.alert_broken = alert_broken
        self.alert_expiry = alert_expiry
        self.alert_mixed = alert_mixed
        self.alert_reminder = alert_reminder
        self.contact_groups = contact_groups
        self.follow_redirects = follow_redirects
        self.mixed_content = mixed_content
        self.paused = paused
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                    self._configuration is not None and \
                    self._configuration.discard_unknown_keys and \
                    self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, website_url, check_rate, alert_at, alert_broken, alert_expiry, alert_mixed, alert_reminder, contact_groups, follow_redirects, mixed_content, paused, *args, **kwargs):  # noqa: E501
        """SSLTest - a model defined in OpenAPI

        Args:
            id (str): SSL check ID
            website_url (str): URL of the server under test
            check_rate (SSLTestCheckRate):
            alert_at ([int]): List representing when alerts should be sent (days).
            alert_broken (bool): Whether to enable alerts when SSL certificate issues are found
            alert_expiry (bool): Whether to enable alerts when the SSL certificate is to expire
            alert_mixed (bool): Whether to enable alerts when mixed content is found
            alert_reminder (bool): Whether to enable alert reminders
            contact_groups ([str]): List of contact group IDs
            follow_redirects (bool): Whether to follow redirects when testing. Disabled by default
            mixed_content ([SSLTestMixedContent]): List of mixed content resources
            paused (bool): Whether the check should be run

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            certificate_score (int): SSL certificate score (%). [optional]  # noqa: E501
            certificate_status (str): SSL certificate status. [optional]  # noqa: E501
            cipher (str): SSL/TLS cipher suite belonging to the SSL certificate. [optional]  # noqa: E501
            cipher_score (int): SSL certificate cipher strength (%). [optional]  # noqa: E501
            issuer_common_name (str): Issuer of the SSL certificate. [optional]  # noqa: E501
            flags (SSLTestFlags): [optional]  # noqa: E501
            hostname (str): Hostname of the server under test. [optional]  # noqa: E501
            last_reminder (int): The last reminder to have been sent (days). [optional]  # noqa: E501
            updated_at (datetime): When the SSL certificate was last updated (RFC3339 format). [optional]  # noqa: E501
            user_agent (str): Custom user agent string set when testing. [optional]  # noqa: E501
            valid_from (datetime): SSL certificate validity start (RFC3339 format). [optional]  # noqa: E501
            valid_until (datetime): SSL certificate validity end (RFC3339 format). [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.website_url = website_url
        self.check_rate = check_rate
        self.alert_at = alert_at
        self.alert_broken = alert_broken
        self.alert_expiry = alert_expiry
        self.alert_mixed = alert_mixed
        self.alert_reminder = alert_reminder
        self.contact_groups = contact_groups
        self.follow_redirects = follow_redirects
        self.mixed_content = mixed_content
        self.paused = paused
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                    self._configuration is not None and \
                    self._configuration.discard_unknown_keys and \
                    self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                        f"class with read only attributes.")
