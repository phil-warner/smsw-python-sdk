# coding: utf-8

"""
    The SMS Works API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CancelledMessageResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'messageid': 'str',
        'status': 'str'
    }

    attribute_map = {
        'messageid': 'messageid',
        'status': 'status'
    }

    def __init__(self, messageid=None, status=None):
        """
        CancelledMessageResponse - a model defined in Swagger
        """

        self._messageid = None
        self._status = None

        self.messageid = messageid
        self.status = status

    @property
    def messageid(self):
        """
        Gets the messageid of this CancelledMessageResponse.

        :return: The messageid of this CancelledMessageResponse.
        :rtype: str
        """
        return self._messageid

    @messageid.setter
    def messageid(self, messageid):
        """
        Sets the messageid of this CancelledMessageResponse.

        :param messageid: The messageid of this CancelledMessageResponse.
        :type: str
        """
        if messageid is None:
            raise ValueError("Invalid value for `messageid`, must not be `None`")

        self._messageid = messageid

    @property
    def status(self):
        """
        Gets the status of this CancelledMessageResponse.

        :return: The status of this CancelledMessageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CancelledMessageResponse.

        :param status: The status of this CancelledMessageResponse.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CancelledMessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other