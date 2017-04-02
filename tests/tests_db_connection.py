from unittest import TestCase
from code import DBConnection
import mock
import mongomock
import errno


class TestsDBConnection(TestCase):
    def setUp(self):
        self.dbconnection = DBConnection()
        self.dbconnection.client = mongomock.MongoClient()
        self.dbconnection.db = self.dbconnection.client[self.dbconnection.db_name]
        # self.dbconnection.collection = self.dbconnection.collection[self.dbconnection.db_name]

    def tearDown(self):
        self.dbconnection.db.drop_collection("scrapper")

    def test_save_in_database(self):
        self.dbconnection.is_in_database = mock.MagicMock(return_value = False)
        self.assertIsNotNone(self.dbconnection.save_in_database(['roberto', 'dias', 'buenos', 'haciendo']))

    def test_save_in_database_allready_in_db(self):
        self.dbconnection.is_in_database = mock.MagicMock(return_value = True)
        self.assertIsNone(self.dbconnection.save_in_database(['roberto', 'dias', 'buenos', 'haciendo']))

    def test_query(self):
        value = [{u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']},
                                   {u'frase': [u'sergio', u'noches', u'malos', u'deshaciendo']}]
        self.dbconnection.db.scrapper.find = mock.MagicMock(return_value = value)
        expected_result = [{u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']},
                           {u'frase': [u'sergio', u'noches', u'malos', u'deshaciendo']}]

        result = self.dbconnection.query()
        self.assertEqual(result, expected_result)

    def test_is_in_database(self):
        value = dict(
            frase = ['roberto', 'dias', 'buenos', 'haciendo']
        )

        objects = [value]
        for obj in objects:
            obj['_id'] = self.dbconnection.db.scrapper.insert(obj)

        self.assertTrue(self.dbconnection.is_in_database(['roberto', 'dias', 'buenos', 'haciendo']))

    def test_is_in_database_not_in_db(self):
        value = dict(
            frase = ['roberto', 'dias', 'buenos', 'haciendo']
        )

        objects = [value]
        for obj in objects:
            obj['_id'] = self.dbconnection.db.scrapper.insert(obj)

        self.assertFalse(self.dbconnection.is_in_database(['dias', 'buenos', 'haciendo']))

    def test_next_result_returns_result(self):
        self.dbconnection.query_result = [{u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']},
                                   {u'frase': [u'sergio', u'noches', u'malos', u'deshaciendo']}]
        result = self.dbconnection.next_result()
        expected_result = {u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']}
        self.assertEqual(result, expected_result)

    def test_next_result_returns_error_because_out_of_bounds(self):
        self.dbconnection.query_result = [{u'frase': [u'roberto', u'dias', u'buenos', u'haciendo']},
                                   {u'frase': [u'sergio', u'noches', u'malos', u'deshaciendo']}]
        result = None
        for i in range(0, 3):
            result = self.dbconnection.next_result()
        expected_result = errno.ERANGE
        self.assertEqual(result, expected_result)

    def test_save_in_database_argument_is_str(self):
        self.assertEqual(self.dbconnection.save_in_database('hola'), errno.EINVAL)

    def test_save_in_database_argument_is_int(self):
        self.assertEqual(self.dbconnection.save_in_database(3), errno.EINVAL)

    def test_save_in_database_argument_is_bool(self):
        self.assertEqual(self.dbconnection.save_in_database(True), errno.EINVAL)

    def test_is_in_database_argument_is_str(self):
        self.assertEqual(self.dbconnection.is_in_database('hola'), errno.EINVAL)

    def test_is_in_database_argument_is_int(self):
        self.assertEqual(self.dbconnection.is_in_database(3), errno.EINVAL)

    def test_is_in_database_argument_is_bool(self):
        self.assertEqual(self.dbconnection.is_in_database(True), errno.EINVAL)

    def test_is_in_database_argument_is_list(self):
        self.assertEqual(self.dbconnection.is_in_database([]), False)


