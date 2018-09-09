#!/usr/bin/env python3

# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : प्रकाश   (Prakash)
# date   : 2018/09/08

import os
import xml.etree.ElementTree as et

#import .converter as cvt
from . import converter as cvt



class ReadXML():
    def __init__(self,pxmlfile):
        self.xml_file = pxmlfile


        self.ns = {'office':'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
              'draw':'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
              'text':'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
              'table':'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
              'style':'urn:oasis:names:tc:opendocument:xmlns:style:1.0'}

    
    def read_xml(self,xml_file):
        tree = et.parse(xml_file)
        root = tree.getroot()
        lw = []
        for body in root.findall('office:body',self.ns):
            for drawing in body.findall('office:drawing',self.ns):
                for page in drawing.findall('draw:page',self.ns):
                    for frame in page.findall('draw:frame',self.ns):
                        for text_box in frame.findall('draw:text-box',self.ns):
                            for p in text_box.findall('text:p',self.ns):
                                for span in p.findall('text:span',self.ns):
                                    atrb = span.attrib
                                    nst = '{'+self.ns['text']+'}style-name'
                                    style = atrb[nst]
                                    #print(atrb)
                                    tp = (style,span.text)
                                    #print(style, ' ',span.text,end='\n')
                                    lw.append(tp)

        return lw

    def show_info(self):
        lw = self.read_xml(self.xml_file)
        for ft,word in lw:
            #ft = lw[i][0]
            #word = lw[i][1]
            cvcl = cvt.Converter()
            c_word = word
            if ft != 'T8':
                c_word = cvcl.convert_word(word)

            print('{} :: {}  || {}'.format(ft,word,c_word))

    def write_file(self,output_file):
        with open(output_file,'w') as ofl:
            for i in range(len(lw)):
                ft = lw[i][0]
                word = lw[i][1]
                cvcl = cvt.Converter()
                c_word = word
                if ft != 'T8':
                    c_word = cvcl.convert_word(word)

                # T5 147 is chandrabindu
                # T5 151 is -

                if ft == 'T5':
                    if len(word) == 1:
                        if ord(word) == 151:
                            ofl.write('\n')
                            print('\n')

                print('{}'.format(c_word),end='')
                ofl.write('{}'.format(c_word))


if __name__ == '__main__':
    MP = ReadXML()
    MP.show_info()
