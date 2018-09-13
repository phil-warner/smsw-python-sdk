# coding: utf-8

"""
    The SMS Works API

    The SMS Works provides a low-cost, reliable SMS API for developers. Pay only for delivered texts, all failed messages are refunded.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.message_response import MessageResponse  # noqa: F401,E501


class MessagesResponseMessages(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'schema': 'MessageResponse'
    }

    attribute_map = {
        'schema': 'schema'
    }

    def __init__(self, schema=None):  # noqa: E501
        """MessagesResponseMessages - a model defined in Swagger"""  # noqa: E501

        self._schema = None
        self.discriminator = None

        if schema is not None:
            self.schema = schema

    @property
    def schema(self):
        """Gets the schema of this MessagesResponseMessages.  # noqa: E501


        :return: The schema of this MessagesResponseMessages.  # noqa: E501
        :rtype: MessageResponse
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this MessagesResponseMessages.


        :param schema: The schema of this MessagesResponseMessages.  # noqa: E501
        :type: MessageResponse
        """

        self._schema = schema

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MessagesResponseMessages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
