#!/usr/bin/env python

import sys
from math import *

class evaluateModelPython:
    
    def __init__(self, fileName, word_probability):
        self.fileName = fileName
        self.word_probability = word_probability
        self.total_word_number = 0
        self.unknown_word_number = 0
        self.lambdaP = 0.95
        self.lambdaUnk = 1 - self.lambdaP
        self.Volume = 1000000
        self.H = 0

    def evaluate_model(self):
        word = []
        f = open(self.fileName, 'r')
        for line in f:
            rline = line.replace("\n", "")
            words = rline.split(" ")
            words.append("</s>")
            for word in words:
                self.total_word_number = self.total_word_number + 1
                P = 1.0 * self.lambdaUnk / self.Volume
                if self.word_probability.has_key(word):
                   P = P + self.lambdaP * self.word_probability[word]
                else:
                   self.unknown_word_number = self.unknown_word_number + 1
                self.H = self.H -1 * log(P,2)
        f.close()
        

