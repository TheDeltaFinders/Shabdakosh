#!/usr/bin/env python3

# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : प्रकाश   (Prakash)
# date   : 2018/09/08


import os

from processor import converter as cvt
from processor import xmlread as rxml

class Test():
    def __init__(self):
        base_path = os.path.dirname(os.path.realpath(__file__))
        self.xml_file = os.path.join(base_path,"res/OneChhaPage.xml")
        self.output_file = os.path.join(base_path,'res/Out_OneChhaPage.txt')

    def test_stuffs(self):
        self.test_converter()
        #self.test_read_xml()
        self.test_show_font()

    def test_converter(self):
        cvcl = cvt.Converter()
        word = ''' cIf/Ù n]Vo ¿kdf  cGtflIf/L  Uo sfdbf®x¿nfO{ '''
        c_word = cvcl.convert_word(word)
        print(' {} == > {} '.format(word,c_word))

    def test_read_xml(self):
        RXML = rxml.ReadXML(self.xml_file)
        RXML.show_info()

    def test_show_font(self):
        RXML = rxml.ReadXML(self.xml_file)
        RXML.show_font_stat()
        RXML.write_file(self.output_file)


if __name__ == '__main__':
    MP = Test()
    MP.test_stuffs()

