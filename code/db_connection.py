import pymongo
from pymongo import errors
from pymongo import MongoClient
import errno
import ast


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

                if not self.is_in_database(list_of_arguments[0]):
                    output_id = self.db.scrapper.insert_one({list_of_arguments[0] :{list_of_arguments[1]: list_of_arguments[2]}}).inserted_id
                else:
                    id = self.db.scrapper.find_one({list_of_arguments[0]: {"$exists": 'true'}}).get('_id')
                    self.db.scrapper.update({'_id': id}, {'$set': {list_of_arguments[0] + '.' + list_of_arguments[1]: list_of_arguments[2]}})
                    output_id = id
                return output_id
            except errors.ConnectionFailure as e:
                print "Something went wrong: " % e
                return e
        else:
            return errno.EINVAL

    def is_in_database(self, short_date):
        if type(short_date) is str:
            element = self.db.scrapper.find({short_date: {"$exists": 'true'}}).count()
            print element
            return element is not 0
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

    def check_date_in_db(self, short_date, long_date):
        if type(short_date) is str and type(long_date) is str:
            element = self.db.scrapper.find({short_date + '.' + long_date: {"$exists": 'true'}}).count()
            return element is not 0
        else:
            return errno.EINVAL

    def get_data_from_database(self, short_date, long_date):
        if type(short_date) is str and type(long_date) is str:
            id = self.db.scrapper.find_one({short_date: {"$exists": 'true'}}).get('_id')
            element = self.db.scrapper.find_one({'_id': id})
            element = str(element[short_date][long_date])
            element = ast.literal_eval(element)
            print element
            print type(element)
            return element
        else:
            return errno.EINVAL

    def get_all_data_of_a_date_from_database(self, date):
        if type(date) is str:
            id = self.db.scrapper.find_one({date: {"$exists": 'true'}}).get('_id')
            element = self.db.scrapper.find_one({'_id': id})
            element = str(element[date])
            element = ast.literal_eval(element)
            print element
            print type(element)
            return element
        else:
            return errno.EINVAL

    @staticmethod
    def mongodb_conn():
        try:
            return pymongo.MongoClient()
        except pymongo.errors.ConnectionFailure, e:
            print "Could not connect to server: %s" % e
            return None
