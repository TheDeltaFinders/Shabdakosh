#!/usr/bin/env python3

from peewee import Model,CharField,DateField,BooleanField

from pos import Pos

class Meaning(BaseModel):
    meaning = TextField()
    pos = ForeignKeyField(Pos,related_name='meanings')

