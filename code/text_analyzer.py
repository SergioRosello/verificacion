# -*- coding: utf-8 -*-
import errno
import re
import nltk
import sys
import unicodedata
from db_connection import DBConnection


class TextAnalyzer(object):

    def __init__(self, text):
        self._text = text

    def text_analyzer(self):
        self.check_input()
        parsed_input = self.parse_input()
        sorted_input = self.sort_input(parsed_input)
        self.print_result(sorted_input)
        result_list = []
        for w in sorted(sorted_input, key=sorted_input.get, reverse=True):
            result_list.append(w)
        resultado = []
        resultado.append(result_list)
        resultado.append(sorted_input)
        return resultado

    def check_input(self):
        if type(self.text) is str:
            return str(self.text)
        else:
            return errno.EINVAL

    def parse_input(self):
        nltk.download("stopwords")
        from nltk.corpus import stopwords
        from unidecode import unidecode
        # elimina los signos especiales

        print type(self.text)
        if type(self.text) is not unicode:
            self.text = unicode(self.text,'utf-8','ignore')

        self.text = unidecode(self.text)
        self.text = self.text.lower()

        # Borra la puntuacion y devuelve una lista de grupos con las palabras que aparecen en el texto.
        words = re.findall(r'\w+', self.text, flags=re.UNICODE | re.LOCALE)

        parsed_text = []
        for word in words:
            if word not in stopwords.words('spanish'):
                parsed_text.append(word)
        return parsed_text

    @classmethod
    def sort_input(self, words):
        from collections import Counter
        return Counter(words)

    @classmethod
    def print_result(self, result):
        for w in sorted(result, key=result.get, reverse=True):
            print w, result[w]

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

if __name__ == "__main__":
    analyzer = TextAnalyzer(sys.argv[1])
    phrase = analyzer.text_analyzer()
    dbconnection = DBConnection()
    dbconnection.save_in_database(phrase[0])
    # DBConnection.query()
    # DBConnection.next_result()
