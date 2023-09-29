# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPredictController(BaseTestCase):
    """PredictController integration test stubs"""

    def test_get_predict_result(self):
        """Test case for get_predict_result

        Get prediction result
        """
        response = self.client.open(
            '/api/v3/predict/{testData}'.format(test_data='test_data_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
