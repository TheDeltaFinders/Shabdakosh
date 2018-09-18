#!/usr/bin/env python3

import re

from processor.mapping import Mapping as mpg
from processor.prcmap import PrcMap as Prm


class Sabdakosh():
    def __init__(self):
        self.unirex = Prm.getPreRex()
        self.prerex = mpg.getPreRex()
        self.postrex = mpg.getRexArray()
        self.asciifile= './res/ChhaASCII.txt'
        self.rawunifile= './res/ChhaRaw.txt'
        self.unifile = './res/ChhaProc.txt'
        self.sepfile = './res/ChhaSep.txt'

    def rexSub(self,line,rex):
        for rx in rex:
            line = re.sub(rx[0],rx[1],line)
        return line


    def asciiToUnicode(self):
        '''This function converts the ASCII Nepali characters to Unicode
           since the ASCII for Nepali based on Priti font    is not used
           everywhere in the original dictionary  there are  going to be
           problems which we subsequently address and try to correct
        '''
        '''There are two parts of regular expression substution, the first
           part one to one substitutes the Preeti ascii characters by  the
           corresponding unicode character for Nepali. The post part tries
           to correct the misplacement of certain characters in the mapping
        '''
        dicmap   = mpg.getMapping()
        rexarray = mpg.getRexArray()
        extmap   = mpg.getExtraMap()

        with open(self.asciifile,'r') as asc_fil:
            with open (self.rawunifile,'w') as raw_uni_ofl:
                content = asc_fil.read()
                content = self.rexSub(content,self.prerex)
                cnt = ''
                for char in content:
                    try:
                        ucc = dicmap[char]
                        cnt += ucc
                    except KeyError:
                        try:
                            euc = extmap[char]
                            cnt += euc
                        except KeyError:
                            cnt += char

                print('doing a post process')
                cnt = self.rexSub(cnt,self.postrex)
                raw_uni_ofl.write(cnt)


    def postProcess(self):
        '''This  Post process part  tries to correct errors that are  seen
           during manual inspection. I've added errors found by inspection
           and tried to generalize them to include other such errors to do
           the correction later. Also this part tries to remove the recur-
           rent advertiesment from the downloader. Crazy right??
        '''
        with open(self.rawunifile,'r') as inf:
            with open(self.unifile,'w') as otf:
                wholeFile = inf.read()
                for rex in self.unirex:
                    wholeFile = re.sub(rex[0],rex[1],wholeFile)

                otf.write(wholeFile)

    def doStuffs(self):
        self.asciiToUnicode()
        self.postProcess()
        self.separateWords()

    def separateWords(self):
        seprex = r'[^\x00-\x7F]*[/~]*([^\x00-\x7F]+—)'
        comprex = re.compile(seprex)
        cnt = 0
        lastPos = 0
        curPos  = 0
        with open(self.unifile,'r') as inf:
            with open(self.sepfile,'w') as otf:
                wholeFile = inf.read()
                for m in comprex.finditer(wholeFile):
                    lastPos = curPos
                    curPos = m.start()
                    otf.write('\n >> \n'+wholeFile[lastPos:curPos]+'\n << \n')
                    otf.write(m.group()+'\n')
                    print(cnt,' ',m.start(),' ' , m.group())
                    cnt += 1

if __name__ == '__main__':
    obj = Sabdakosh()
    obj.doStuffs()
