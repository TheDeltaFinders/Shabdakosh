#!/usr/bin/env python3

# vim: ai ts=4 sts=4 et sw=4 ft=python

import os

from processor import converter as cvt
from processor import xmlread as rxml

class Test():
    def __init__(self):
        pass

    def test_stuffs(self):
        self.test_converter()
        self.test_read_xml()

    def test_converter(self):
        cvcl = cvt.Converter()
        word = ';latf 5Q  cIf/Ù n]Vo ¿kdf '
        c_word = cvcl.convert_word(word)
        print(' {} == > {} '.format(word,c_word))

    def test_read_xml(self):
        base_path = os.path.dirname(os.path.realpath(__file__))
        xml_file = os.path.join(base_path,"res/OneChhaPage.xml")
        RXML = rxml.ReadXML(xml_file)
        RXML.show_info()


if __name__ == '__main__':
    MP = Test()
    MP.test_stuffs()

