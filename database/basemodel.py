#!/usr/bin/env python3

from peewee import *

from .constants import Constants as Cst

class BaseModel(Model):
    class Meta:
        database = Cst.DB
