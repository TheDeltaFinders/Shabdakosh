#!/usr/bin/env python3
from constants import Constants as Cnsts
from prcmap import PrcMap as Prm

import re

class Processor():
    def __init__(self):
        self.filename = Cnsts.RESDIR + Cnsts.ONE_LETTER_FILE
        self.outFile = Cnsts.RESDIR + Cnsts.ONE_LETTER_OUT_FILE
        self.prerex = Prm.getPreRex() 

    def preProcess(self):
        with open(self.filename,'r') as inf:
            with open(self.outFile,'w') as otf:
                wholeFile = inf.read()
                for rex in self.prerex:
                    wholeFile = re.sub(rex[0],rex[1],wholeFile)

                otf.write(wholeFile)



    def processIt(self):
        pass
        #with open(self.filename,'r') as fil:
        #    wholeFile = fil.read() :




if __name__ == '__main__':
    Processor().preProcess()
