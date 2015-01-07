#!/usr/bin/env python

import sys
from bigram_map import bigramMapPython

class bigramPython:
    
    def __init__(self, word):
        self.word = word
        self.word_map = {}
        self.context_count = {}
        self.lambda_word_map = {}

    def bigram_train(self):
        uni_word_number = 0
        bi_word_number = 0
        bi_diff_word_map = {}
        u_count_map = {}
        count_word_map = {}
        for word_line in self.word:
            count = 1
            while len(word_line) > count:
                word_map = bigramMapPython(self.word_map, word_line[count])
                self.word_map = word_map.bigram_map()

                count_word_map = bigramMapPython(count_word_map, word_line[count - 1])
                count_word_map = count_word_map.bigram_map()

                context_count = bigramMapPython(self.context_count, "")
                self.context_count = context_count.bigram_map()

                bi_word = word_line[count - 1] + " " + word_line[count]
                word_map = bigramMapPython(self.word_map, bi_word)
                self.word_map = word_map.bigram_map()
                bi_diff_word_map.update({bi_word:word_line[count - 1]})

                context_count = bigramMapPython(self.context_count, word_line[count - 1])
                self.context_count = context_count.bigram_map()

                count = count + 1
        # Witten Bell Smoothing
        for k,v in bi_diff_word_map.items():
            words = k.split(" ")
            if u_count_map.has_key(v):
               bi_value = u_count_map[v]
               u_count_map.update({v:bi_value + 1})
            else:
               u_count_map[v] = 1

        for k in count_word_map.keys():
            lambda_w =  1 - ( 1.0 * u_count_map[k] / ( u_count_map[k] + count_word_map[k]))
            self.lambda_word_map.update({k:lambda_w})
        #
        for ngram,count in self.word_map.items():
            words = ngram.split(" ")
            words.pop()
            context = "".join(words)
            probability = 1.0 * self.word_map[ngram] / self.context_count[context]
            self.word_map.update({ngram:probability})
