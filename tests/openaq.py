import unittest
from crawler.wrappers import opeanaqapi


class OpenaqTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(OpenaqTest, self).__init__(*args, **kwargs)
        self.openaqapi_wrapper = opeanaqapi.OpenaqAuthWrapper()

    def test_get_measurements_2021(self):
        """
            Get dictionary of measurements of 2021 - first page
        - OK: function response is not empty
        """
        self.assertTrue(self.openaqapi_wrapper.openaq.get_measurements_2021())

    def test_get_measurements_2022(self):
        """
            Get dictionary of measurements of 2022 - first page
        - OK: function response is not empty
        """
        self.assertTrue(self.openaqapi_wrapper.openaq.get_measurements_2022())
