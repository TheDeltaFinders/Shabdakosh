#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-11 20:41

class Word():
    """
    word class to have a complete word and its details with meaning 
    and subwords and their meaning

    """
    def __init__(self):
        """
        This function initializes th meaning of the words

        """

        self.meaning = list()
        self.subwords = list()
        self.construction = ''
        self.is_root = True

    
    def make_plot(self,other_params):
        """
        Make plot fo the words and their meaning

        :type    other_params: str
        :param   other_params: other parameter required to make the plot

        """
        
        pass

    def add_meaning(self,pos,meaning): 
        """
        This function adds the meaning of the word with its part of speech

        :type    pos: str
        :param   pos: The part of speech of the meaning added

        :type    meaning: str
        :param   meaning: The meaning of word with this part of speech

        """

        self.meaings.append((pos,meaning))


if __name__ == '__main__':
    MP = Word()
    MP.make_plot(other_params)
