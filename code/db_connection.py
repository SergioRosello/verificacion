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

    def save_in_database(self, list_of_arguments):
        if type(list_of_arguments) is (list or dict):
            try:
                output_id = None
                if not self.is_in_database(list_of_arguments):
                    output_id = self.db.scrapper.insert_one({'fecha': list_of_arguments[0], 'frase': list_of_arguments[1]}).inserted_id
                    print "Successful"
                else:
                    print "data already exists in DB"
                return output_id
            except errors.ConnectionFailure as e:
                print "Something went wrong: " % e
                return e
        else:
            return errno.EINVAL

    def is_in_database(self, date):
        if type(date) is (str):
            element = self.db.scrapper.find_one({'fecha': date})
            return element is not None
        else:
            return errno.EINVAL

    def query(self):
        result = self.db.scrapper.find({},{'_id': False})
        for x in result:
            self.query_result.append(x)
        self.indice = 0
        return self.query_result

    def next_result(self):
        print self.indice
        print len(self.query_result)
        if self.indice < len(self.query_result):
            return_value = self.query_result[self.indice]
            self.indice += 1
            return return_value
        else:
            return errno.ERANGE

    @staticmethod
    def mongodb_conn():
        try:
            return pymongo.MongoClient()
        except pymongo.errors.ConnectionFailure, e:
            print "Could not connect to server: %s" % e
            return None