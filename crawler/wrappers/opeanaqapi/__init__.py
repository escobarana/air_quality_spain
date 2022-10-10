from crawler.wrappers.opeanaqapi.exceptions import OpenaqApiException
from crawler.wrappers.opeanaqapi.openaq import OpenaqAPIWrapper
import logging
import requests

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class OpenaqAuthWrapper:
    """
        Class OpenaqAuthWrapper to handle the requests for the OpenAQ API
    """

    def __init__(self):
        """
            Initialization of the class
        """
        self.root_url = "https://api.openaq.org/v2"
        self.openaq = OpenaqAPIWrapper(self.do_request, self.root_url)

    def do_request(self, endpoint):
        """
            Function to make the request to the API given an endpoint
        :param endpoint:    Endpoint to make the request to
        :return:            JSON response of the call to the API or error message
        """
        logger.info(f"Doing request to {endpoint}")
        headers = {"accept": "application/json"}
        resp = requests.get(endpoint, headers=headers)

        if resp.status_code == 200:
            return resp.text
        else:
            raise OpenaqApiException(resp, endpoint)
