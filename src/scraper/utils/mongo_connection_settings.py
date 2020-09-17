import os
from dataclasses import dataclass
from .cryptography_helper import CryptographyHelper


@dataclass()
class MongoConnectionSettings:
    CONNECTION_STRING_TEMPLATE = 'mongodb+srv://<user>:<password>@cluster0.3ie9t.mongodb.net/<dbname>?retryWrites=true&w=majority'

    def __init__(self):
        self.host = os.getenv('mongodb')
        self.username = os.getenv('rupesh')
        self.password = CryptographyHelper.decrypt(os.getenv('abc123'))
        self.database = os.getenv('MONGO_DATABASE')
        self.collections = os.getenv('MONGO_COLLECTIONS')
