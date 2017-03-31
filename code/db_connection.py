import pymongo
from pymongo import errors
from pymongo import MongoClient
import errno


class DBConnection:
    mongo_info = 'mongodb://localhost:27017/'
    db_name = 'scrapper'
    query_result = None

    def __init__(self):
        self.client = MongoClient(self.mongo_info)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.db_name]

    def save_in_database(self, list_of_arguments):
        try:
            self.collection.insert_one({'frase': list_of_arguments})
            print "Successful"
        except errors.ConnectionFailure as e:
            print "Something went wrong: " % e

    def query(self, list_of_instructions=None):
        result = self.collection.find(list_of_instructions)
        DBConnection.query_result = result

    @staticmethod
    def next_result():
        if DBConnection.query_result.alive:
            try:
                return DBConnection.query_result.next()
            except StopIteration:
                return errno.EBADRQC
        else:
            return errno.ERANGE
