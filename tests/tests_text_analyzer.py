# -*- coding: utf-8 -*-

import unittest
import errno
from collections import Counter
from .context import code


class CoreTestSuite(unittest.TestCase):

    # https://docs.python.org/2/library/errno.html

    def test_textAnalizer_checkInput_check_argument_is_string(self):
        test = code.TextAnalyzer('hola')
        self.assertEqual(test.text_analyzer(), Counter({'hola':1}))

    def test_textAnalizer_checkInput_check_argument_is_bool(self):
        test = code.TextAnalyzer(True)
        self.assertEqual(test.text_analyzer(), errno.EINVAL)

    def test_textAnalizer_checkInput_check_argument_is_int(self):
        test = code.TextAnalyzer(1)
        self.assertEqual(test.text_analyzer(), errno.EINVAL)

    def test_textAnalizer_parseinput_check_string_is_lowercase(self):
        test = code.TextAnalyzer('hoLa SerGio')
        self.assertEqual(test.parse_input(), ['hola', 'sergio'])

    def test_textAnalizer_parseinput_check_string_is_lowercase_with_punctuation(self):
        test = code.TextAnalyzer('hóLa: SerGió.')
        self.assertEqual(test.parse_input(), ['hola', 'sergio'])

    def test_textAnalizer_parseinput_check_string_is_lowercase_with_punctuation_and_stopwords(self):
        test = code.TextAnalyzer('hóLa: sóY SerGió.')
        self.assertEqual(test.parse_input(), ['hola', 'sergio'])

    def test_textAnalizer_sortinput(self):
        test = code.TextAnalyzer.sort_input(['hola', 'hola', 'mesa', 'cama'])
        self.assertEqual(test, {'hola': 2, 'mesa': 1, 'cama': 1})

if __name__ == '__main__':
    unittest.main()
