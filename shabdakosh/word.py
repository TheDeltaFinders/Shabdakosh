#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-11 20:41

class Word(ParentClass):
    def __init__(self):
        self.meaning = list()
        self.subwords = list()
        self.construction = ''
        self.is_root = True

    
    def make_plot(self,other_params):
        pass

    def add_meaning(self,pos,meaning):
        self.meaings.append((pos,meaning))


if __name__ == '__main__':
    MP = Word()
    MP.make_plot(other_params)
