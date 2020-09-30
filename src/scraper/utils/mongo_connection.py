from typing import Any
import logging
from pymongo import MongoClient
from .mongo_connection_settings import MongoConnectionSettings


class MongoConnection:

    def __init__(self, mongo_connection_settings: MongoConnectionSettings):
        self.client: Any = None
        self.database: Any = None
        self.mongo_connection_settings = mongo_connection_settings

    def connect(self):
        # to make only single connection so that we will have only one instance of mongo
        if self.client is not None:
            return

        connection_string_template = self.mongo_connection_settings.CONNECTION_STRING_TEMPLATE
        user = self.mongo_connection_settings.username
        password = self.mongo_connection_settings.password
        host = self.mongo_connection_settings.host
        database = self.mongo_connection_settings.database
        connection_string = connection_string_template.replace('<dbuser>', user).replace('<dbpassword>', password).replace('<host>', host)
        # connection_string = 'mongodb+srv://rupesh:rupesh123@cluster0.3ie9t.mongodb.net/intelli?retryWrites=true&w=majority'

        logging.info("Attempting to connect to host: %s", host)

        # try to connect to db
        try:
            self.client = MongoClient(connection_string)
            self.database = self.client[database]
            logging.info("Successfully connected to mongo database.")
            
        # pylint: disable=broad-except
        except Exception as ex:
            logging.warning('A warning was emitted connecting to database', exc_info=ex)

    # function to insert data into db
    def insert_one(self, document, collection_str):
        self.connect()
        collection = self.database[collection_str]
        collection.insert_one(document)

    # function to check if the data is already present in db
    def is_document_present(self, search_query, collection_str) -> bool:
        self.connect()
        collection = self.database[collection_str]
        count = collection.count_documents(search_query)

        return count > 0

    # to remove all the references of the object client
    def __del__(self):
        if self.client is not None:
            self.client = None
