# -*- coding: utf-8 -*-
import errno
import re
import nltk
class textAnalizer(object):


    def __init__(self, text):
        self._text = text

    def textAnalizer(self):
        self.checkInput()
        parsedinput = self.parseInput()
        sortedinput = self.sortInput(parsedinput)
        self.printresult(sortedinput)

    def checkInput(self):
        if type(self.text) is str:
            return str(self.text)
        else:
            return errno.EINVAL

    def parseInput(self):
        nltk.download("stopwords")
        from nltk.corpus import stopwords
        from unidecode import unidecode
        #elimina los signos especiales
        textUnicode = unicode(self.text,'utf-8','ignore')

        self.text = unidecode(textUnicode)
        self.text = (self.text).lower()

        #Borra la puntuacion y devuelve una lista de grupos con las palabras que aparecen en el texto.
        words = re.findall(r'\w+', self.text, flags=re.UNICODE | re.LOCALE)

        parsedText = []
        for word in words:
            if word not in stopwords.words('spanish'):
                parsedText.append(word)

        return parsedText

    @classmethod
    def sortInput(self, list):
        from collections import Counter
        result = Counter(list)
        return result

    @classmethod
    def printresult(self, result):
        for w in sorted(result, key=result.get, reverse=True):
            print w, result[w]

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

if __name__ == "__main__":
    analizer = textAnalizer('HólA me llamo Sergio y teNgo sergio hola una guitárra hola')
    analizer.textAnalizer()