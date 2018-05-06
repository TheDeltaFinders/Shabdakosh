#!/usr/bin/env python3

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

class Constants:
    DB = SqliteExtDatabase('my_dictionary.db')
