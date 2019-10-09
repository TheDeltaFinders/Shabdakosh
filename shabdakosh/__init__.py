#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-11 22:17

import click
import os

from shabdakosh.readpdf import ReadPDF

TEMPLATE_PDF = os.path.join(os.path.dirname(__file__),'../res/splitted_438-438.pdf')

def show_text(pdf_file):
    """
    Show all the parsed text from the pdf

    :type    pdf_file: str
    :param   pdf_file: the name of pdf file to show text of

    """
    pdf_file = pdf_file or TEMPLATE_PDF
    PR = ReadPDF(pdf_file)
    print(PR.get_text(nepali=True))

def show_info(pdf_file):
    """
    Show the information of the pdf file with text and font

    :type    pdf_file: str
    :param   pdf_file: the name of pdf file to show info of

    """
    pdf_file = pdf_file or TEMPLATE_PDF
    PR = ReadPDF(pdf_file)
    for word,font in PR.get_word_font(True):
        print(f' {font } :: {word} ')

    for font in PR.font_set:
        print(font)

@click.command()
@click.option('-f','--file','pdf_file',type=str,help='pdf file to read')
@click.option('-i','--info','show_info',default=False,type=bool,help='show file detail')
def  main(pdf_file,show_info):
    if show_info:
        show_info(pdf_file)
    else:
        show_text(pdf_file)


def  get_meaning(word):
    """
    Get the meaning of the word supplied

    :type    word: str
    :param   word: the meaning of word we supply

    """
    pass

if __name__ == '__main__':
    main()

