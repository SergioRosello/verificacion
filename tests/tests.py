# -*- coding: utf-8 -*-

import unittest
import errno

from .context import code

class CoreTestSuite(unittest.TestCase):


    def test_concatenate(self):
        # SET-UP
        str1 = 'hola'
        str2 = 'hola'

        # EXECUTION
        result = code.concatenate(str1, str2)

        # ASSERT
        self.assertEqual(result, 'holahola', "El resultado no es el esperado")

#https://docs.python.org/2/library/errno.html

    def test_concatenate_check_args_arent_strings(self):
        self.assertEqual(code.concatenate(True, 2), errno.EINVAL)

    def test_concatenate_check_args_are_strings(self):
        self.assertEqual(code.concatenate('hola', 'hola'), 'holahola')

    def test_concatenate_check_whitespaces(self):
        self.assertEqual(code.concatenate('pr ueb a', 'es paci o'), 'pruebaespacio', "El resultado no es el esperado")

    def test_concatenate_string_with_more_than_ten_characters(self):
        self.assertEqual(code.concatenate('moreThanTenCharacters', '<10Chars'), errno.EINVAL)

    def test_concatenate_one_string(self):
        self.assertEqual(code.concatenate('hola'), errno.EPERM)

    def test_concatenate_more_than_ten_strings(self):
        self.assertEqual(code.concatenate('h', 'o', 'l', 'a', ', ', 'q', 'u', 'e', 't', 'a', 'l'), errno.E2BIG)


if __name__ == '__main__':
    unittest.main()
