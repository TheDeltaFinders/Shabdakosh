#!/usr/bin/env python3

from peewee import *

class BaseWord(BaseModel):
    word = CharField()



class WordMeaning(BaseModel):
    word = ForeignKey(BaseWord)
    meaning = ForeignKey(Meaning)
