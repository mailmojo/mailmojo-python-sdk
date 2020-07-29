# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TrackFormView(object):
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
        'form_id': 'int',
        'id': 'int',
        'trigger': 'object',
        'user_agent': 'str',
        'view_url': 'str',
        'visitor_id': 'str'
    }

    attribute_map = {
        'form_id': 'form_id',
        'id': 'id',
        'trigger': 'trigger',
        'user_agent': 'user_agent',
        'view_url': 'view_url',
        'visitor_id': 'visitor_id'
    }

    def __init__(self, form_id=None, id=None, trigger=None, user_agent=None, view_url=None, visitor_id=None):  # noqa: E501
        """TrackFormView - a model defined in Swagger"""  # noqa: E501

        self._form_id = None
        self._id = None
        self._trigger = None
        self._user_agent = None
        self._view_url = None
        self._visitor_id = None
        self.discriminator = None

        self.form_id = form_id
        if id is not None:
            self.id = id
        self.trigger = trigger
        if user_agent is not None:
            self.user_agent = user_agent
        self.view_url = view_url
        self.visitor_id = visitor_id

    @property
    def form_id(self):
        """Gets the form_id of this TrackFormView.  # noqa: E501


        :return: The form_id of this TrackFormView.  # noqa: E501
        :rtype: int
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        """Sets the form_id of this TrackFormView.


        :param form_id: The form_id of this TrackFormView.  # noqa: E501
        :type: int
        """
        if form_id is None:
            raise ValueError("Invalid value for `form_id`, must not be `None`")  # noqa: E501

        self._form_id = form_id

    @property
    def id(self):
        """Gets the id of this TrackFormView.  # noqa: E501


        :return: The id of this TrackFormView.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrackFormView.


        :param id: The id of this TrackFormView.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def trigger(self):
        """Gets the trigger of this TrackFormView.  # noqa: E501


        :return: The trigger of this TrackFormView.  # noqa: E501
        :rtype: object
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this TrackFormView.


        :param trigger: The trigger of this TrackFormView.  # noqa: E501
        :type: object
        """
        if trigger is None:
            raise ValueError("Invalid value for `trigger`, must not be `None`")  # noqa: E501

        self._trigger = trigger

    @property
    def user_agent(self):
        """Gets the user_agent of this TrackFormView.  # noqa: E501


        :return: The user_agent of this TrackFormView.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this TrackFormView.


        :param user_agent: The user_agent of this TrackFormView.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

    @property
    def view_url(self):
        """Gets the view_url of this TrackFormView.  # noqa: E501


        :return: The view_url of this TrackFormView.  # noqa: E501
        :rtype: str
        """
        return self._view_url

    @view_url.setter
    def view_url(self, view_url):
        """Sets the view_url of this TrackFormView.


        :param view_url: The view_url of this TrackFormView.  # noqa: E501
        :type: str
        """
        if view_url is None:
            raise ValueError("Invalid value for `view_url`, must not be `None`")  # noqa: E501

        self._view_url = view_url

    @property
    def visitor_id(self):
        """Gets the visitor_id of this TrackFormView.  # noqa: E501


        :return: The visitor_id of this TrackFormView.  # noqa: E501
        :rtype: str
        """
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, visitor_id):
        """Sets the visitor_id of this TrackFormView.


        :param visitor_id: The visitor_id of this TrackFormView.  # noqa: E501
        :type: str
        """
        if visitor_id is None:
            raise ValueError("Invalid value for `visitor_id`, must not be `None`")  # noqa: E501

        self._visitor_id = visitor_id

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
        if issubclass(TrackFormView, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrackFormView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other