#!/usr/bin/env python3

from peewee import *
import datetime

from database.basemodel import BaseModel

class Pos(BaseModel):
    partname = CharField()
    abbreviation = CharField()
    create_date = DateField(default=datetime.datetime.now)
    is_active = BooleanField(default=True)

