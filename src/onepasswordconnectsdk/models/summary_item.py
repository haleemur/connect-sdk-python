# coding: utf-8

"""
    1Password Connect

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SummaryItem(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'title': 'str',
        'vault': 'ItemVault',
        'category': 'str',
        'urls': 'list[ItemUrls]',
        'favorite': 'bool',
        'tags': 'list[str]',
        'version': 'int',
        'trashed': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'last_edited_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'vault': 'vault',
        'category': 'category',
        'urls': 'urls',
        'favorite': 'favorite',
        'tags': 'tags',
        'version': 'version',
        'trashed': 'trashed',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'last_edited_by': 'lastEditedBy'
    }

    def __init__(self, id=None, title=None, vault=None, category=None, urls=None, favorite=False, tags=None, version=None, trashed=False, created_at=None, updated_at=None, last_edited_by=None):  # noqa: E501
        self._id = None
        self._title = None
        self._vault = None
        self._category = None
        self._urls = None
        self._favorite = None
        self._tags = None
        self._version = None
        self._trashed = None
        self._created_at = None
        self._updated_at = None
        self._last_edited_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        self.vault = vault
        if category is not None:
            self.category = category
        if urls is not None:
            self.urls = urls
        if favorite is not None:
            self.favorite = favorite
        if tags is not None:
            self.tags = tags
        if version is not None:
            self.version = version
        if trashed is not None:
            self.trashed = trashed
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if last_edited_by is not None:
            self.last_edited_by = last_edited_by

    @property
    def id(self):
        """Gets the id of this Item.  # noqa: E501


        :return: The id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Item.


        :param id: The id of this Item.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Item.  # noqa: E501


        :return: The title of this Item.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Item.


        :param title: The title of this Item.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def vault(self):
        """Gets the vault of this Item.  # noqa: E501


        :return: The vault of this Item.  # noqa: E501
        :rtype: ItemVault
        """
        return self._vault

    @vault.setter
    def vault(self, vault):
        """Sets the vault of this Item.


        :param vault: The vault of this Item.  # noqa: E501
        :type: ItemVault
        """

        self._vault = vault

    @property
    def category(self):
        """Gets the category of this Item.  # noqa: E501


        :return: The category of this Item.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Item.


        :param category: The category of this Item.  # noqa: E501
        :type: str
        """
        allowed_values = ["LOGIN", "PASSWORD", "SERVER", "DATABASE", "CREDIT_CARD", "MEMBERSHIP", "PASSPORT", "SOFTWARE_LICENSE", "OUTDOOR_LICENSE", "SECURE_NOTE", "WIRELESS_ROUTER", "BANK_ACCOUNT", "DRIVER_LICENSE", "IDENTITY", "REWARD_PROGRAM", "DOCUMENT", "EMAIL_ACCOUNT", "SOCIAL_SECURITY_NUMBER", "API_CREDENTIAL", "CUSTOM"]  # noqa: E501
        if category not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def urls(self):
        """Gets the urls of this Item.  # noqa: E501


        :return: The urls of this Item.  # noqa: E501
        :rtype: list[ItemUrls]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this Item.


        :param urls: The urls of this Item.  # noqa: E501
        :type: list[ItemUrls]
        """

        self._urls = urls

    @property
    def favorite(self):
        """Gets the favorite of this Item.  # noqa: E501


        :return: The favorite of this Item.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this Item.


        :param favorite: The favorite of this Item.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def tags(self):
        """Gets the tags of this Item.  # noqa: E501


        :return: The tags of this Item.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Item.


        :param tags: The tags of this Item.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def version(self):
        """Gets the version of this Item.  # noqa: E501


        :return: The version of this Item.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Item.


        :param version: The version of this Item.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def trashed(self):
        """Gets the trashed of this Item.  # noqa: E501


        :return: The trashed of this Item.  # noqa: E501
        :rtype: bool
        """
        return self._trashed

    @trashed.setter
    def trashed(self, trashed):
        """Sets the trashed of this Item.


        :param trashed: The trashed of this Item.  # noqa: E501
        :type: bool
        """

        self._trashed = trashed

    @property
    def created_at(self):
        """Gets the created_at of this Item.  # noqa: E501


        :return: The created_at of this Item.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Item.


        :param created_at: The created_at of this Item.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Item.  # noqa: E501


        :return: The updated_at of this Item.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Item.


        :param updated_at: The updated_at of this Item.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def last_edited_by(self):
        """Gets the last_edited_by of this Item.  # noqa: E501


        :return: The last_edited_by of this Item.  # noqa: E501
        :rtype: str
        """
        return self._last_edited_by

    @last_edited_by.setter
    def last_edited_by(self, last_edited_by):
        """Sets the last_edited_by of this Item.


        :param last_edited_by: The last_edited_by of this Item.  # noqa: E501
        :type: str
        """

        self._last_edited_by = last_edited_by

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Item):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Item):
            return True

        return self.to_dict() != other.to_dict()
