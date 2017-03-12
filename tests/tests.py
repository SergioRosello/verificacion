# -*- coding: utf-8 -*-

import unittest
import errno

from .context import code

class CoreTestSuite(unittest.TestCase):

#https://docs.python.org/2/library/errno.html

    def test_textAnalizer_checkInput_check_argument_is_string(self):
        test = code.textAnalizer('hola')
        self.assertEqual(test.checkInput(), 'hola')

    def test_textAnalizer_checkInput_check_argument_is_bool(self):
        test = code.textAnalizer(True)
        self.assertEqual(test.checkInput(), errno.EINVAL)

    def test_textAnalizer_checkInput_check_argument_is_int(self):
        test = code.textAnalizer(1)
        self.assertEqual(test.checkInput(), errno.EINVAL)

    def test_textAnalizer_parseinput_check_string_is_lowercase(self):
        test = code.textAnalizer('hoLa SerGio')
        self.assertEqual(test.parseInput(), ['hola', 'sergio'])

    def test_textAnalizer_parseinput_check_string_is_lowercase_with_punctuation(self):
        test = code.textAnalizer('hóLa: SerGió.')
        self.assertEqual(test.parseInput(), ['hola', 'sergio'])

    def test_textAnalizer_parseinput_check_string_is_lowercase_with_punctuation_and_stopwords(self):
        test = code.textAnalizer('hóLa: sóY SerGió.')
        self.assertEqual(test.parseInput(), ['hola', 'sergio'])


    def test_textAnalizer_sortinput(self):
        test = code.textAnalizer.sortInput(['hola', 'hola', 'mesa', 'cama'])
        self.assertEqual(test, {'hola': 2, 'mesa': 1, 'cama': 1})


if __name__ == '__main__':
    unittest.main()
