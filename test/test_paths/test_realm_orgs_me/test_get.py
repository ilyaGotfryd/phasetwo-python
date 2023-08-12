# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import phasetwo
from phasetwo.paths.realm_orgs_me import get  # noqa: E501
from phasetwo import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRealmOrgsMe(ApiTestMixin, unittest.TestCase):
    """
    RealmOrgsMe unit test stubs
        Get orgs and roles for authenticated user  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()