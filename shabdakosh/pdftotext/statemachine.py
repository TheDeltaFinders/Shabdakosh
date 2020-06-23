#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2020-06-10 15:15

from enum import Enum
from enum import auto

from .data_structure import FIFO


class Font(Enum):
    TNR = 'TimesNewRoman'
    PREETI = 'Preeti'

class State(Enum):
    WORD_END           = auto()
    START_WORD         = auto()
    MEANING_FOUND      = auto()

class CharFontType(Enum):
    START_POS_BRACKET  = auto()
    END_POS_BRACKET    = auto()
    SUB_WORD_START     = auto()
    SUB_WORD_END       = auto()
    


class CharFont(object):
    def __init__(self):
        pass
    
    def add_char_font(self,char,font):
        self.char = char
        self.font = font


    @property
    def docfont(self):
        return Font.TNR

    @property
    def category(self):
        if self.char == '[' and self.docfont == Font.TNR:
            return CharFontType.START_POS_BRACKET
        elif self.char == ']' and self.docfont == Font.TNR:
            return CharFontType.END_POS_BRACKET
        elif self.char == '>' and self.docfont == Font.TNR:
            return CharFontType.SUB_WORD_START
    


class StateMachine():
    def __init__(self):
        self.status = State.START_WORD
        self.identity_buffer = FIFO()
    
    def identify_buffer(self,charfont):
        

    def add_char(self,charfont):
        current_buffer = self.identify_buffer(charfont) 
        current_buffer.push(charfont)

    def evaluate_input(self,charfont):
        pass