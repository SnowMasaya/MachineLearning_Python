#!/usr/bin/env python

import sys
from bigram_map import bigramMapPython

class bigramPython:
    
    def __init__(self, word):
        self.word = word
        self.word_map = {}
        self.context_count = {}

    def bigram_train(self):
        uni_word_number = 0
        bi_word_number = 0
        for word_line in self.word:
            count = 1
            while len(word_line) > count:
                word_map = bigramMapPython(self.word_map, word_line[count])
                self.word_map = word_map.bigram_map()

                context_count = bigramMapPython(self.context_count, "")
                self.context_count = context_count.bigram_map()

                bi_word = word_line[count - 1] + " " + word_line[count]
                word_map = bigramMapPython(self.word_map, bi_word)
                self.word_map = word_map.bigram_map()

                context_count = bigramMapPython(self.context_count, word_line[count - 1])
                self.context_count = context_count.bigram_map()

                count = count + 1
        print {k:v for k,v in self.word_map.items()}
        print {k:v for k,v in self.context_count.items()}
        for ngram,count in self.word_map.items():
            words = ngram.split(" ")
            words.pop()
            context = "".join(words)
            print ngram + " " + context + " " + str(self.word_map[ngram]) + " " + str(self.context_count[context])
            probability = 1.0 * self.word_map[ngram] / self.context_count[context]
            self.word_map.update({ngram:probability})
