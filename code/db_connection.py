import pymongo
from pymongo import errors
from pymongo import MongoClient
import errno


class DBConnection:
    mongo_info = 'mongodb://localhost:27017/'
    db_name = 'scrapper'
    query_result = []
    indice = 0

    def __init__(self):
        self.client = MongoClient(self.mongo_info)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.db_name]

    def save_in_database(self, list_of_arguments):
        try:
            output_id = None
            if not self.is_in_database(list_of_arguments):
                output_id = self.collection.insert_one({'frase': list_of_arguments}).inserted_id
                print "Successful"
            else:
                print "data already exists in DB"
            return output_id
        except errors.ConnectionFailure as e:
            print "Something went wrong: " % e
            return e

    def is_in_database(self, list_of_arguments):
        element = self.collection.find_one({'frase': list_of_arguments})
        return element is not None

    def query(self, list_of_instructions=None):
        result = self.collection.find(list_of_instructions, {'_id': False})
        for x in result:
            self.query_result.append(x)
        self.indice = 0
        return self.query_result



    def next_result(self):
        if self.indice < len(self.query_result):
            return_value = self.query_result[self.indice]
            self.indice += 1
            return return_value
        else:
            return errno.ERANGE