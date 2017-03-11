# -*- coding: utf-8 -*-

import unittest
import errno

from .context import code

class CoreTestSuite(unittest.TestCase):

    '''def test_libreriaTextos(self):
        str1 = 'hola'
        str2 = 'hola'

        result = code.libreriaTextos()

        self.assertEqual(code.libreriaTextos(), 'hola')
    '''



#https://docs.python.org/2/library/errno.html

    def test_textAnalizer_check_argument_is_string(self):
        test = code.textAnalizer('hola')
        self.assertEqual(test.checkImput(), 'hola')

    def test_textAnalizer_check_argument_is_bool(self):
        test = code.textAnalizer(True)
        self.assertEqual(test.checkImput(), errno.EINVAL)

    def test_textAnalizer_check_argument_is_int(self):
        test = code.textAnalizer(1)
        self.assertEqual(test.checkImput(), errno.EINVAL)



if __name__ == '__main__':
    unittest.main()
