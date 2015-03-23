#!/usr/bin/env python

import sys
from math import log

class viterbiForwardPython:
    
    def __init__(self, unigram_model_name, fileName):
        self.unigram_model_name = unigram_model_name
        self.unigram = {}
        self.fileName = fileName
        self.best_edge = []
        self.best_score = []

    def viterbi_forward(self):
        model = open(self.unigram_model_name, 'r')
        words = []
        my_score = 0
        for line in model:
            rline = line.replace("\n","")
            words = rline.split(" ")
            self.unigram.update({words[0]:words[1]})
        print {k:v for k,v in self.unigram.items()}
        f = open(self.fileName, 'r')
        for line in f:
            rline = line.replace("\n","")
            words = rline.decode("utf-8")
            #[self.best_edge[index] for index in range(len(words))]
            self.best_edge = []
            self.best_score = []
            self.best_edge.insert(0,None)
            self.best_score.insert(0,0)
            for word_end in range(1, len(words) + 1):
                self.best_score.insert(word_end,10**10)
                for word_begin in range(0, word_end):
                    word = words[word_begin:word_end]
                    if self.unigram.has_key(word)  or len(word) == 1:
                       prob = self.unigram[word]
                       my_score = self.best_score[word_begin] - log(float(prob))
                       if my_score < self.best_score[word_end]:
                          self.best_score.insert(word_end, my_score)
                          self.best_edge.insert(word_end, (word_begin, word_end))
            words = []
            print self.best_edge
            next_edge = self.best_edge[len(self.best_edge) - 1]
            while next_edge != None:
                word = line[next_edge[0]:next_edge[1]]
                uwords = word.decode("utf-8")
                words.append(uwords)
                next_edge = self.best_edge[ next_edge[0] ]
            rword = words[::-1]
            print words
            print rword
