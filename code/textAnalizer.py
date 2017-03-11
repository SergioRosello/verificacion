# -*- coding: utf-8 -*-
import errno

class textAnalizer(object):


    def __init__(self, text):
        self._text = text

    #funcion general
    #
    def textAnalizer(self):
        self.checkImput()


    def checkImput(self):
        if type(self.text) is str:
            return str(self.text).lower()
        else:
            return errno.EINVAL


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

if __name__ == "__main__":
    analizer = textAnalizer('hola')
    analizer.textAnalizer()