#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2020-06-10 15:15

from enum import Enum
from enum import auto

from .data_structure import FIFO


class Font(Enum):
    TNR_I    = "ANOKCH+TimesNewRoman,Italic"
    NONE     = "None"
    HIMALI   = "EABPNK+FONTASYHIMALITTNORMAL"
    TNR      = "AICLFF+TimesNewRoman"
    SYMB     = "AICMCB+Symbol"
    KANTIPUR = "EACCFI+Kantipur"
    PREETI   = "EABPMI+Preeti"
    HIMALAYA = "EABPNM+Himalayabold"

class State(Enum):
    NEW_BEGIN          = auto()
    WORD_END           = auto()
    START_WORD         = auto()
    MEANING_FOUND      = auto()
    MAIN_WORD          = auto()

class CharFontType(Enum):
    START_POS_BRACKET  = auto()
    END_POS_BRACKET    = auto()
    SUB_WORD_START     = auto()
    SUB_WORD_END       = auto()
    REGULAR_CHAR       = auto()
    WORD_DASH          = auto()
    HBCHAR             = auto()
    
class CharFont(object):
    def __init__(self,char,font):
        self.char = char
        self.font = font
    
    def add_char_font(self,char,font):
        self.char = char
        self.font = font


    @property
    def docfont(self):
        fontobj = Font(self.font)
        return fontobj

    @property
    def category(self):
        if self.char == '[' and self.docfont == Font.TNR:
            return CharFontType.START_POS_BRACKET
        elif self.char == ']' and self.docfont == Font.TNR:
            return CharFontType.END_POS_BRACKET
        elif self.char == '>' and self.docfont == Font.TNR:
            return CharFontType.SUB_WORD_START
        elif self.docfont == Font.TNR:
            return CharFontType.REGULAR_CHAR
    


class StateMachine():
    def __init__(self):
        self.current_state = State.NEW_BEGIN
        self.status = State.START_WORD
        self.identity_buffer = FIFO()
        self.char_buffer = FIFO()
    
    def identify_buffer(self,charfont):
        return self.identity_buffer

    def add_char(self,charfont):
        current_buffer = self.identify_buffer(charfont) 
        current_buffer.push(charfont)
        if self.current_state == State.NEW_BEGIN:
            if charfont.category == CharFontType.WORD_DASH:
                self.char_buffer.push(charfont.char)
                self.current_state = State.WORD_END
            if charfont.category == CharFontType.HBCHAR:
                self.main_word.push(charfont.char)
                self.current_state = State.MAIN_WORD


    def evaluate_input(self,charfont):
        pass


def run_machine(RPF):
    machine = StateMachine()
    for char,font in RPF.get_font_char():
        chfont = CharFont(char,font)
        print(chfont.docfont,' is the char font')
        try:
            machine.add_char(chfont)
        except Exception as e:
            print(f'Exception occured ',e)

