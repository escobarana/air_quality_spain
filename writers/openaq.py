from crawler.helpers.mongodb import load_data_to_mongodb


def save_measures(data: list) -> ():
    """
        Function to save measure data to the MongoDB database
    :param  data: List containing at least one JSON document
    :return: None
    """
    for each in data:
        load_data_to_mongodb(db='local', collection='openaq', document=each)
