#!/usr/bin/env python

import sys

class unigramPython:
    
    def __init__(self, word):
        self.word = word
        self.word_map = {}
        self.total_word = 0

    def unigram_train(self):
        self.total_word = len(self.word)
        for word_line in self.word:
            for word_unit in word_line:
                if self.word_map.has_key(word_unit):
                   value = self.word_map[word_unit]
                   self.word_map.update({word_unit:value+1})
                else:
                   self.word_map[word_unit] = 1
        for k,v in self.word_map.items():
            probability = 1.0 * v / self.total_word
            self.word_map.update({k:probability})

