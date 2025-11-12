# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_avg_get(self):
        """Test case for avg_get

        Get average readings for all appliances
        """
        response = self.client.open(
            '//avg',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
