#!/usr/bin/env python3

from peewee import *

from database.constants import Constants as Cst
from processor.indexmaper import IndexMaper as IdMap
from database.pos import Pos 
from database.basemodel import BaseModel

class Seed():
    def __init__(self):
        self.idxmap = IdMap().getIndexMap()
        db = Cst.DB
        db.connect()
        #db.create_tables([Pos])

    def seedNow(self):
        print('the index amp is ')
        print(self.idxmap)
        for k in self.idxmap:
            curpos = Pos(partname = self.idxmap[k],abbreviation=k)
            curpos.save()

    def showNow(self):
        for pos in Pos.select():
            print('key {} and value {}'.format(pos.abbreviation,pos.partname))



if __name__ == '__main__':
    a = Seed()
    #a.seedNow()
    a.showNow()

