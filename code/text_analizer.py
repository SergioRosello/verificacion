# -*- coding: utf-8 -*-
import errno
import re
import nltk
import sys


class TextAnalyzer(object):


    def __init__(self, text):
        self._text = text

    def text_analizer(self):
        self.check_input()
        parsed_input = self.parse_input()
        sorted_input = self.sort_input(parsed_input)
        self.print_result(sorted_input)

    def check_input(self):
        if type(self.text) is str:
            return str(self.text)
        else:
            return errno.EINVAL

    def parse_input(self):
        nltk.download("stopwords")
        from nltk.corpus import stopwords
        from unidecode import unidecode
        #elimina los signos especiales
        text_unicode = unicode(self.text,'utf-8','ignore')

        self.text = unidecode(text_unicode)
        self.text = (self.text).lower()

        #Borra la puntuacion y devuelve una lista de grupos con las palabras que aparecen en el texto.
        words = re.findall(r'\w+', self.text, flags=re.UNICODE | re.LOCALE)

        parsed_text = []
        for word in words:
            if word not in stopwords.words('spanish'):
                parsed_text.append(word)

        return parsed_text

    @classmethod
    def sort_input(self, list):
        from collections import Counter
        result = Counter(list)
        return result

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
    analizer = TextAnalyzer(sys.argv[1])
    analizer.text_analizer()