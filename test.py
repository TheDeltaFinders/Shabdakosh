#!/usr/bin/env python3

# vim: ai ts=4 sts=4 et sw=4 ft=python

from processor import converter as cvt

class Test():
    def __init__(self):
        pass

    def test_stuffs(self):
        cvcl = cvt.Converter()
        word = ';latf 5Q  cIf/Ù n]Vo ¿kdf '
        c_word = cvcl.convert_word(word)
        print(' {} == > {} '.format(word,c_word))
        
if __name__ == '__main__':
    MP = Test()
    MP.test_stuffs()

