#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-11 19:36
    

from pdfminer.pdfpage import PDFPage #
from pdfminer.pdfinterp import PDFResourceManager #
from pdfminer.pdfinterp import PDFPageInterpreter #
from pdfminer.layout import LAParams #
from pdfminer.converter import  PDFPageAggregator #

from sampadak import Converter 


class ReadPDF():
    """
    Read the PDF file and extract the text and font information

    """
    def  __init__(self,filename=None):
        """
        Initialize the pdf reader class

        :type    filename: str
        :param   filename: the name of pdf file to read

        """

        self.filename = filename
        self.font_set = set()


    def get_text(self,nepali=False):
        """
        Extracts all text from the page and returns it.

        :type    nepali: bool
        :param   nepali: whether we want the text converted to nepali

        """

        text = ''
        for word,font in self.get_word_font(nepali):
            text += ' '+word
        return text



    def get_font_char(self,filename):
        """ 
        Reads the pdf with filename and 
        reads the contents characterwise. This function was 
        copied straight from the documentation of pdfminer 
        library. 
        
        :type    filename: str
        :param   filename: the path of file

        """ 

        #For some reason it reads characterwise, but
        #we are fine with it 

        document = open(self.filename, 'rb')
        rsrcmgr = PDFResourceManager()
        # Set parameters for analysis.
        laparams = LAParams()
        # Create a PDF page aggregator object.
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        #print(f'Number of pages is {len([ x for x in PDFPage.get_pages(document)])}')
        for page in PDFPage.get_pages(document):
            interpreter.process_page(page)
            #print('Page found')
            #print(type(device))
            # receive the LTPage object for the page.
            layout = device.get_result()
            for element in layout:
                #print('I am here')
                print(type(element))
                for obj in element:
                    #print('There are elements more ',type(obj))
                    try:
                        #print(obj.get_text(),end='')
                        #print(type(obj))
                        #print(obj.fontname)
                        yield (obj.get_text(),obj.fontname)
                    except:
                        pass

    def  convert_to_nepali(self,word,font):
        """
        Convert the word into Nepali unicode
        Depends on converter package of sampadak library

        :type   word: str
        :param  word: preeti like font character sequence of word

        :type  font: str
        :param font: the font name of the characters in word

        """
        CVT = Converter()
        nep_word = word
        if 'roman' not in font and 'mbol' not in font:
            nep_word = CVT.convert_preeti(word)

        return nep_word

    def  get_word_font(self,nepali=False):
        """
        From the file read the words and corresponding fonts. 
        The change in font or sppearence of space character
        marks the word boundary.

        :type     nepali: bool
        :param    nepali: whether we want the words actually converted to Nepali

        """
        filename = self.filename
        cur_font = None
        word = ''
        for char,font in self.get_font_char(filename):
            if font != cur_font or char == ' ':
                self.font_set.add(font)
                word = self.convert_to_nepali(word,font) if nepali else word
                yield  word,cur_font
                cur_font = font
                word = ''
            word += char

if __name__ == '__main__':
    pass



