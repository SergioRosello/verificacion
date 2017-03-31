from unittest import TestCase
from code import DBConnection
import mock
import mongomock


class TestsDBConnection(TestCase):
    class TestScraper(TestCase):
        def setUp(self):
            self.dbconnection = DBConnection()
            self.dbconnection.client = mongomock.MongoClient()
            self.dbconnection.db = self.dbconnection.client[self.dbconnection.db_name]
            self.dbconnection.collection = self.dbconnection.collection[self.dbconnection.db_name]

        def tearDown(self):
            self.dbconnection.db.drop_collection(self.dbconnection.db_name)
