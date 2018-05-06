#!/usr/bin/env python3

import re


from mapping.mapping import Mapping as mpg



class Sabdakosh():
    def __init__(self):
        self.prerex = mpg.getPreRex()
        self.postrex = mpg.getRexArray()
        self.outfile = './res/Chha.txt'
        #self.outfile = './res/Out.txt'
        #self.infile  = './res/Page.txt'
        self.infile  = './res/ChhaASCII.txt'
        #self.infile = '/home/pranphy/Desktop/Dictionarys.txt'

    def rexSub(self,line,rex):
        for rx in rex:
            line = re.sub(rx[0],rx[1],line)
        return line 


    def connvert(self):
        dicmap = mpg.getMapping()
        rexarray = mpg.getRexArray()
        extmap = mpg.getExtraMap()
        with open (self.outfile,'w') as ofl:
            with open(self.infile,'r') as fil:
                content = fil.read()
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
                
                cnt = self.rexSub(cnt,self.postrex)
                ofl.write(cnt)
                            


if __name__ == '__main__':
    obj = Sabdakosh()
    obj.connvert()
