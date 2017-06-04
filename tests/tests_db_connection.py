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

    def tearDown(self):
        self.dbconnection.db.drop_collection("scrapper")

    def test_save_in_database(self):
        self.dbconnection.is_in_database = mock.MagicMock(return_value = False)
        self.assertIsNotNone(self.dbconnection.save_in_database(['3 jun 2017', 'Sat, 3 Jun 2017 14:36:49 +0200', { "all" : 1, "afgano" : 2, "entrevista" : 3}]))

    def test_save_in_database_already_in_db(self):
        self.dbconnection.db.scrapper.insert({'3 jun 2017': 1})
        self.dbconnection.is_in_database = mock.MagicMock(return_value = True)
        self.assertIsNotNone(self.dbconnection.save_in_database(['3 jun 2017', 'Sat, 3 Jun 2017 14:36:49 +0200', {"all": 1, "afgano": 2, "entrevista": 3}]))

    def test_check_date_in_db(self):
        self.dbconnection.db.scrapper.insert({'3 jun 2017': {'1':'2'}})
        self.dbconnection.is_in_database = mock.MagicMock(return_value = True)
        self.assertEqual(self.dbconnection.check_date_in_db('3 jun 2017', '1'), True)

    def test_get_data_from_database(self):
        self.dbconnection.db.scrapper.insert({'3 jun 2017': {'1':'2'}})
        self.dbconnection.is_in_database = mock.MagicMock(return_value = True)
        self.assertEqual(self.dbconnection.get_data_from_database('3 jun 2017', '1'), 2)

    def test_get_data_from_database_long_date_is_int(self):
        self.dbconnection.db.scrapper.insert({'3 jun 2017': {'1':'2'}})
        self.dbconnection.is_in_database = mock.MagicMock(return_value = True)
        self.assertEqual(self.dbconnection.get_data_from_database('3 jun 2017', 1), errno.EINVAL)

    def test_get_all_data_of_a_date_from_database(self):
        self.dbconnection.db.scrapper.insert({'3 jun 2017': {'1':'2'}})
        self.dbconnection.is_in_database = mock.MagicMock(return_value = True)
        self.assertEqual(self.dbconnection.get_all_data_of_a_date_from_database('3 jun 2017'), {'1':'2'})

    def test_get_all_data_of_a_date_from_database_short_date_is_int(self):
        self.dbconnection.db.scrapper.insert({'3 jun 2017': {'1':'2'}})
        self.dbconnection.is_in_database = mock.MagicMock(return_value = True)
        self.assertEqual(self.dbconnection.get_all_data_of_a_date_from_database(3), errno.EINVAL)

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
            date = '3 jun 2017'
        )

        objects = [value]
        for obj in objects:
            obj['_id'] = self.dbconnection.db.scrapper.insert(obj)

        self.assertEqual(self.dbconnection.is_in_database('2 jun 2017'), False)

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
        self.assertEqual(self.dbconnection.is_in_database('hola'), False)

    def test_is_in_database_argument_is_int(self):
        self.assertEqual(self.dbconnection.is_in_database(3), errno.EINVAL)

    def test_is_in_database_argument_is_bool(self):
        self.assertEqual(self.dbconnection.is_in_database(True), errno.EINVAL)

    def test_is_in_database_argument_is_list(self):
        self.assertEqual(self.dbconnection.is_in_database([]), errno.EINVAL)
