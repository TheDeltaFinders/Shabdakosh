#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2018/09/08


import os

from processor import converter as cvt
from processor import xmlread as rxml

class Test():
    def __init__(self):
        base_path = os.path.dirname(os.path.realpath(__file__))
        self.xml_file = os.path.join(base_path,"./res/SmallOne.xml")
        self.output_file = os.path.join(base_path,'./res/Out_SmallOne.txt')
        self.xml_file = os.path.join(base_path,"./res/OneChhaPage.xml")
        self.output_file = os.path.join(base_path,'./res/Out_OneChhaPage.txt')
        self.RXML = rxml.ReadXML(self.xml_file)

    def test_stuffs(self):
        self.test_converter()
        #self.test_read_xml()
        #self.test_show_font()
        self.test_show_text()

    def test_converter(self):
        cvcl = cvt.Converter()
        word = ''' cIf/Ù n]Vo ¿kdf  cGtflIf/L  Uo sfdbf®x¿nfO{ '''
        word = ''' cIf/Ù '''
        c_word = cvcl.convert_word(word)
        print(f'{word} == > {c_word}')

    def test_read_xml(self):
        self.RXML.show_info()
    
    def test_show_text(self):
        self.RXML.write_file(self.output_file)

    def test_show_font(self):
        self.RXML.show_font_stat()


if __name__ == '__main__':
    MP = Test()
    MP.test_stuffs()

