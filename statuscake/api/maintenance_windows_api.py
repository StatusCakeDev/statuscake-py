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

    API Version: 1.0.0
    Contact: support@statuscake.com

    Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.
"""


import re  # noqa: F401
import sys  # noqa: F401

from statuscake.api_client import ApiClient, Endpoint as _Endpoint
from statuscake.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from statuscake.model.api_error import APIError
from statuscake.model.api_response import APIResponse
from statuscake.model.maintenance_window_repeat_interval import MaintenanceWindowRepeatInterval
from statuscake.model.maintenance_window_response import MaintenanceWindowResponse
from statuscake.model.maintenance_windows import MaintenanceWindows


class MaintenanceWindowsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_maintenance_window_endpoint = _Endpoint(
            settings={
                'response_type': (APIResponse,),
                'auth': [],
                'endpoint_path': '/maintenance-windows',
                'operation_id': 'create_maintenance_window',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'end_at',
                    'start_at',
                    'timezone',
                    'repeat_interval',
                    'tags',
                    'tests',
                ],
                'required': [
                    'name',
                    'end_at',
                    'start_at',
                    'timezone',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'end_at':
                        (datetime,),
                    'start_at':
                        (datetime,),
                    'timezone':
                        (str,),
                    'repeat_interval':
                        (MaintenanceWindowRepeatInterval,),
                    'tags':
                        ([str],),
                    'tests':
                        ([str],),
                },
                'attribute_map': {
                    'name': 'name',
                    'end_at': 'end_at',
                    'start_at': 'start_at',
                    'timezone': 'timezone',
                    'repeat_interval': 'repeat_interval',
                    'tags': 'tags',
                    'tests': 'tests',
                },
                'location_map': {
                    'name': 'form',
                    'end_at': 'form',
                    'start_at': 'form',
                    'timezone': 'form',
                    'repeat_interval': 'form',
                    'tags': 'form',
                    'tests': 'form',
                },
                'collection_format_map': {
                    'tags': 'csv',
                    'tests': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )
        self.delete_maintenance_window_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/maintenance-windows/{window_id}',
                'operation_id': 'delete_maintenance_window',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'window_id',
                ],
                'required': [
                    'window_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'window_id':
                        (str,),
                },
                'attribute_map': {
                    'window_id': 'window_id',
                },
                'location_map': {
                    'window_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_maintenance_window_endpoint = _Endpoint(
            settings={
                'response_type': (MaintenanceWindowResponse,),
                'auth': [],
                'endpoint_path': '/maintenance-windows/{window_id}',
                'operation_id': 'get_maintenance_window',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'window_id',
                ],
                'required': [
                    'window_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'window_id':
                        (str,),
                },
                'attribute_map': {
                    'window_id': 'window_id',
                },
                'location_map': {
                    'window_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_maintenance_windows_endpoint = _Endpoint(
            settings={
                'response_type': (MaintenanceWindows,),
                'auth': [],
                'endpoint_path': '/maintenance-windows',
                'operation_id': 'list_maintenance_windows',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'limit',
                    'state',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'state',
                ],
                'validation': [
                    'page',
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 1,
                    },
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('state',): {

                        "ACTIVE": "active",
                        "PAUSED": "paused",
                        "PENDING": "pending"
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'limit':
                        (int,),
                    'state':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'limit': 'limit',
                    'state': 'state',
                },
                'location_map': {
                    'page': 'query',
                    'limit': 'query',
                    'state': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_maintenance_window_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/maintenance-windows/{window_id}',
                'operation_id': 'update_maintenance_window',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'window_id',
                    'name',
                    'end_at',
                    'repeat_interval',
                    'start_at',
                    'tags',
                    'tests',
                    'timezone',
                ],
                'required': [
                    'window_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'window_id':
                        (str,),
                    'name':
                        (str,),
                    'end_at':
                        (datetime,),
                    'repeat_interval':
                        (MaintenanceWindowRepeatInterval,),
                    'start_at':
                        (datetime,),
                    'tags':
                        ([str],),
                    'tests':
                        ([str],),
                    'timezone':
                        (str,),
                },
                'attribute_map': {
                    'window_id': 'window_id',
                    'name': 'name',
                    'end_at': 'end_at',
                    'repeat_interval': 'repeat_interval',
                    'start_at': 'start_at',
                    'tags': 'tags',
                    'tests': 'tests',
                    'timezone': 'timezone',
                },
                'location_map': {
                    'window_id': 'path',
                    'name': 'form',
                    'end_at': 'form',
                    'repeat_interval': 'form',
                    'start_at': 'form',
                    'tags': 'form',
                    'tests': 'form',
                    'timezone': 'form',
                },
                'collection_format_map': {
                    'tags': 'csv',
                    'tests': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )

    def create_maintenance_window(
        self,
        name,
        end_at,
        start_at,
        timezone,
        **kwargs
    ):
        """Create a maintenance window  # noqa: E501

        Creates a maintenance window with the given parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_maintenance_window(name, end_at, start_at, timezone, async_req=True)
        >>> result = thread.get()

        Args:
            name (str): Name of the maintenance window
            end_at (datetime): End of the maintenance window (RFC3339 format)
            start_at (datetime): Start of the maintenance window (RFC3339 format)
            timezone (str): Standard [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) associated with this maintenance window

        Keyword Args:
            repeat_interval (MaintenanceWindowRepeatInterval): [optional]
            tags ([str]): List of tags used to include matching uptime checks in this maintenance window. At least one of `tests` and `tags` must be present in the request. [optional]
            tests ([str]): List of uptime check IDs explicitly included in this maintenance window. At least one of `tests` and `tags` must be present in the request. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            APIResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['name'] = \
            name
        kwargs['end_at'] = \
            end_at
        kwargs['start_at'] = \
            start_at
        kwargs['timezone'] = \
            timezone
        return self.create_maintenance_window_endpoint.call_with_http_info(**kwargs)

    def delete_maintenance_window(
        self,
        window_id,
        **kwargs
    ):
        """Delete a maintenance window  # noqa: E501

        Deletes a maintenance window with the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_maintenance_window(window_id, async_req=True)
        >>> result = thread.get()

        Args:
            window_id (str): Maintenance window ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['window_id'] = \
            window_id
        return self.delete_maintenance_window_endpoint.call_with_http_info(**kwargs)

    def get_maintenance_window(
        self,
        window_id,
        **kwargs
    ):
        """Retrieve a maintenance window  # noqa: E501

        Returns a maintenance window with the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_maintenance_window(window_id, async_req=True)
        >>> result = thread.get()

        Args:
            window_id (str): Maintenance window ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MaintenanceWindowResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['window_id'] = \
            window_id
        return self.get_maintenance_window_endpoint.call_with_http_info(**kwargs)

    def list_maintenance_windows(
        self,
        **kwargs
    ):
        """Get all maintenance windows  # noqa: E501

        Returns a list of maintenance windows for an account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_maintenance_windows(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page of results. [optional] if omitted the server will use the default value of 1
            limit (int): The number of maintenance windows to return per page. [optional] if omitted the server will use the default value of 25
            state (str): Maintenance window state. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MaintenanceWindows
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_maintenance_windows_endpoint.call_with_http_info(**kwargs)

    def update_maintenance_window(
        self,
        window_id,
        **kwargs
    ):
        """Update a maintenance window  # noqa: E501

        Updates a maintenance window with the given parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_maintenance_window(window_id, async_req=True)
        >>> result = thread.get()

        Args:
            window_id (str): Maintenance window ID

        Keyword Args:
            name (str): Name of the maintenance window. [optional]
            end_at (datetime): End of the maintenance window (RFC3339 format). [optional]
            repeat_interval (MaintenanceWindowRepeatInterval): [optional]
            start_at (datetime): Start of the maintenance window (RFC3339 format). [optional]
            tags ([str]): List of tags used to include matching uptime checks in this maintenance window. [optional]
            tests ([str]): List of uptime check IDs explicitly included in this maintenance window. [optional]
            timezone (str): Standard [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) associated with this maintenance window. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['window_id'] = \
            window_id
        return self.update_maintenance_window_endpoint.call_with_http_info(**kwargs)
