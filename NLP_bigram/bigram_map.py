#!/usr/bin/env python

import sys

class bigramMapPython:
    
    def __init__(self, word_map, word):
        self.word_map = word_map
        self.word = word

    def bigram_map(self):
        if self.word_map.has_key(self.word):
           value = self.word_map[self.word]
           self.word_map.update({self.word:value + 1})
        else:
           self.word_map[self.word] = 1
        return self.word_map

