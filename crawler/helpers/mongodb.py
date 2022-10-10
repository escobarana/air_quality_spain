import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")


def load_data_to_mongodb(db: str, collection: str, document: dict):
    """
        Function to load a document to MongoDB
    :param  db: Database name
    :param  collection: Collection name
    :param  document: Dictionary document to load to MongoDB
    :return: None
    """
    database = client[db]
    collection = database[collection]
    collection.insert_one(document)
