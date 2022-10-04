import json


class OpenaqAPIWrapper:
    def __init__(self, do_request, root_url):
        """
            Initialization of the class with the root URL and the do_request method to make the request to the API
        """
        self.do_request = do_request
        self.root_url = root_url

    # --- ENDPOINTS --- #
    def get_measurements_2021(self, page: int = 1, count: int = 0):
        """
            Function to retrieve the measurements in Spain between 01/09/2021 and 30/09/2021
        :param page:    Page number to do the request
        :param count:   Current number of records retrieved
        :return:        Dictionary containing all the results
        """
        content = self.do_request(f"{self.root_url}/measurements?date_from=2021-09-01&date_to=2021-09-30&limit=1000"
                                  f"&page={page}&offset=0&sort=desc&unit=&country_id=ES&order_by=location")
        total_records = content['found']
        num_page = content['page']
        count += len(content['results'])

        return_dict = {"data": json.loads(content)['results'],
                       "next_page": num_page+1 if count < total_records else None,
                       "current_count": count}
        return return_dict

    def get_measurements_2022(self, page: int = 1, count: int = 0):
        """
            Function to retrieve the measurements in Spain between 01/09/2022 and 30/09/2022
        :param page:    Page number to do the request
        :param count:   Current number of records retrieved
        :return:        Dictionary containing all the results
        """
        content = self.do_request(f"{self.root_url}/measurements?date_from=2022-09-01&date_to=2022-09-30&limit=1000"
                                  f"&page={page}&offset=0&sort=desc&unit=&country_id=ES&order_by=location")
        total_records = content['found']
        num_page = content['page']
        count += len(content['results'])

        return_dict = {"data": json.loads(content)['results'],
                       "next_page": num_page + 1 if count < total_records else None,
                       "current_count": count}
        return return_dict
