#!/usr/bin/env python

import sys
from ngram_map import ngramMapPython

class ngramPython:
    
    def __init__(self, word, ngram_number):
        self.word = word
        self.ngram_number = ngram_number
        self.word_map = {}
        self.context_count = {}
        self.lambda_word_map = {}

    def ngram_train(self):
        uni_word_number = 0
        bi_word_number = 0
        bi_diff_word_map = {}
        u_count_map = {}
        count_word_map = {}
        for word_line in self.word:
            count = 1
            while len(word_line) > count:
                ngram_count = 2
                word_map = ngramMapPython(self.word_map, word_line[count])
                self.word_map = word_map.ngram_map()

                count_word_map = ngramMapPython(count_word_map, word_line[count - 1])
                count_word_map = count_word_map.ngram_map()

                context_count = ngramMapPython(self.context_count, "")
                self.context_count = context_count.ngram_map()
                
                while self.ngram_number >= ngram_count:
                      n_word = []
                      for counter in range(0, ngram_count):
                          unit_number = count -1 + counter
                          if len(word_line) <= unit_number:
                             break
                          n_word.append(word_line[unit_number])
                      join_nword = " ".join(n_word)
                      word_map = ngramMapPython(self.word_map, join_nword)
                      self.word_map = word_map.ngram_map()
                      context_count = ngramMapPython(self.context_count, join_nword)
                      self.context_count = context_count.ngram_map()
                      ngram_count = ngram_count + 1
                bi_word = word_line[count - 1] + " " + word_line[count]
                bi_diff_word_map.update({bi_word:word_line[count - 1]})
                context_count = ngramMapPython(self.context_count, word_line[count - 1])
                self.context_count = context_count.ngram_map()

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
        print {k:v for k,v in self.word_map.items()}
        for ngram,count in self.word_map.items():
            words = ngram.split(" ")
            words.pop()
            if len(words) < 2:
               context = "".join(words)
            else:
               context = " ".join(words)
            probability = 1.0 * self.word_map[ngram] / self.context_count[context]
            self.word_map.update({ngram:probability})
