from crawler.helpers.mongodb import load_data_to_mongodb


def save_measures(data: list, collection: str) -> ():
    """
        Function to save measure data to the MongoDB database
    :param  data: List containing at least one JSON document
    :param  collection: Collection name to insert the data into
    :return: None
    """
    load_data_to_mongodb(list_documents=data, collection=collection)
