import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")


def load_data_to_mongodb(list_documents: list, collection: str, db: str = 'local'):
    """
        Function to load a document to MongoDB
    :param  db: Database name
    :param  collection: Collection name
    :param  list_documents: List of document to load to MongoDB
    :return: None
    """
    database = client[db]
    collection = database[collection]
    collection.insert_many(list_documents)


def get_data_from_mongodb(parameter: str, collection: str, db: str = 'local'):
    """
        Function to retrieve documents from MongoDB
    :param  db: Database name
    :param  collection: Collection name
    :param  parameter: Parameter to filter the data by (NO2, PM10, PM2,5)
    :return: List of documents
    """
    my_list = []

    database = client[db]
    collection = database[collection]

    query = {"parameter": parameter}

    documents = collection.find(query)

    for each in documents:
        my_list.append(each)

    return my_list
