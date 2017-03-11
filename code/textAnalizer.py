# -*- coding: utf-8 -*-
import errno
import re
import nltk
import unidecode

class textAnalizer(object):


    def __init__(self, text):
        self._text = text

    #funcion general
    #
    def textAnalizer(self):
        self.checkInput()
        self.parseInput()


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

        print parsedText
        return parsedText

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

if __name__ == "__main__":
    analizer = textAnalizer('hoLa, me llámo SoY: SerGio.')
    analizer.textAnalizer()