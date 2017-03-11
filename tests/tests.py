# -*- coding: utf-8 -*-

import unittest
import errno

from .context import code

class CoreTestSuite(unittest.TestCase):

#https://docs.python.org/2/library/errno.html

    def test_textAnalizer_checkInput_check_argument_is_string(self):
        test = code.textAnalizer('hola')
        self.assertEqual(test.checkImput(), 'hola')

    def test_textAnalizer_checkInput_check_argument_is_bool(self):
        test = code.textAnalizer(True)
        self.assertEqual(test.checkImput(), errno.EINVAL)

    def test_textAnalizer_checkInput_check_argument_is_int(self):
        test = code.textAnalizer(1)
        self.assertEqual(test.checkImput(), errno.EINVAL)

    def test_textAnalizer_checkInput_check_string_is_lowercase(self):
        test = code.textAnalizer('hoLa SoY SerGio')
        self.assertEqual(test.parseInput(), 'hola soy sergio')

    #def test_textAnalizer_checkInput_check_

if __name__ == '__main__':
    unittest.main()
