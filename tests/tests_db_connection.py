from unittest import TestCase
from code import DBConnection
import mock
import mongomock


class TestsDBConnection(TestCase):
    def setUp(self):
        self.dbconnection = DBConnection()
        self.dbconnection.client = mongomock.MongoClient()
        self.dbconnection.db = self.dbconnection.client[self.dbconnection.db_name]
        self.dbconnection.collection = self.dbconnection.collection[self.dbconnection.db_name]

    def tearDown(self):
        self.dbconnection.db.drop_collection(self.dbconnection.db_name)

    def test_save_in_database(self):
        self.dbconnection.is_in_database = mock.MagicMock(return_value = False)

        self.assertIsNotNone(self.dbconnection.save_in_database({u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']}))

    def test_save_in_database_allready_in_db(self):
        self.dbconnection.is_in_database = mock.MagicMock(return_value = True)

        self.assertIsNone(self.dbconnection.save_in_database({u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']}))


    def test_query(self):
        value = [{u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']},
                                   {u'frase': [u'sergio', u'noches', u'malos', u'deshaciendo']}]
        self.dbconnection.collection.find = mock.MagicMock(return_value = value)
        expected_result = [{u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']},
                           {u'frase': [u'sergio', u'noches', u'malos', u'deshaciendo']}]

        result = self.dbconnection.query()
        self.assertEqual(result, expected_result)


    def test_is_in_database(self):
        value = {u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']}
        self.dbconnection.collection.find_one = mock.MagicMock(return_value = value)
        expected_result = True

        result = self.dbconnection.is_in_database(value)
        self.assertEqual(result, expected_result)

    def test_is_in_database_not_in_db(self):
        value = None
        self.dbconnection.collection.find_one = mock.MagicMock(return_value = value)
        expected_result = False

        result = self.dbconnection.is_in_database(value)
        self.assertEqual(result, expected_result)