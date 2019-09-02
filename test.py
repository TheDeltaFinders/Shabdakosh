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
        self.dotslash = lambda x: os.path.join(base_path,x)
        #self.xml_file = os.path.join(base_path,"./res/SmallOne.xml")
        self.xml_file = os.path.join(base_path,"./res/Large/splitted_439-439.xml")
        self.output_file = os.path.join(base_path,'./res/Out_SmallOne.txt')
        #self.xml_file = os.path.join(base_path,"./res/OneChhaPage.xml")
        self.output_file = os.path.join(base_path,'./res/Out_OneChhaPage.txt')
        self.RXML = rxml.ReadXML(self.xml_file)

    def stuffs(self):
        self.converter()
        #self.read_xml()
        #self.show_font()
        self.show_text()
        self.RXML.save_to_txt(self.dotslash('res/OutputApril.txt'))

    def converter(self):
        cvcl = cvt.Converter()
        word = '''a if a aif cIf/Ù n]Vo ¿kdf  cGtflIf/L  Uo sfdbf®x¿nfO{ '''
        #word = ''' cIf/Ù '''
        word='if'
        c_word = cvcl.convert_word(word)
        print(f'{word}::{c_word}')

    def read_xml(self):
        self.RXML.show_info()
    
    def show_text(self):
        self.RXML.write_file(self.output_file)

    def show_font(self):
        self.RXML.show_font_stat()


if __name__ == '__main__':
    MP = Test()
    MP.stuffs()

