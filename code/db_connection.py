import pymongo
from pymongo import errors
from pymongo import MongoClient
import errno


class DBConnection:
    client = None
    query_result = None

    @staticmethod
    def db_connect():
        DBConnection.client = MongoClient('localhost', 27017)
        collection = DBConnection.client.scrapper.scrapper
        return collection

    @staticmethod
    def db_close():
        DBConnection.client.close()

    @staticmethod
    def save_in_database(list_of_arguments):
        collection = DBConnection.db_connect()
        try:
            collection.insert_one({'frase': list_of_arguments})
            print "Successful"
        except errors.ConnectionFailure as e:
            print "Something went wrong: " % e

        DBConnection.db_close()


    @staticmethod
    def query(list_of_instructions=None):
        collection = DBConnection.db_connect()
        result = collection.find(list_of_instructions)
        DBConnection.db_close()
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
