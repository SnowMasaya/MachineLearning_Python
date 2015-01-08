#!/usr/bin/env python

import sys
from math import *

class evaluateModelPython:
    
    def __init__(self, fileName, word_probability, lambda_word_map):
        self.fileName = fileName
        self.word_probability = word_probability
        self.total_word_number = 0
        self.lambda_word_P = lambda_word_map
        self.lambdaP1 = 0.95
        self.lambdaP2 = 0.95
        self.lambdaUnk1 = 1 - self.lambdaP1
        self.lambdaUnk2 = 1 - self.lambdaP2
        self.Volume = 1000000
        self.H = 0

    def evaluate_model(self):
        word = []
        f = open(self.fileName, 'r')
        for line in f:
            rline = line.replace("\n", "")
            words = rline.split(" ")
            words.append("</s>")
            words.insert(0, "<s>")
            count = 1
            while len(words) > count:
                self.total_word_number = self.total_word_number + 1
                P1 = 1.0 * self.lambdaUnk1 / self.Volume
                if self.word_probability.has_key(words[count]):
                   P1 = P1 + (1 - self.lambda_word_P[words[count - 1]] ) * self.word_probability[words[count]]
                P2 = P1 * self.lambda_word_P[words[count - 1]] / self.Volume
                bi_word = words[count - 1] + " " + words[count]
                if self.word_probability.has_key(words[count]):
                   P2 = P2 + self.lambda_word_P[words[count - 1]] * self.word_probability[bi_word]
                self.H = self.H -1 * log(P2,2)
                count = count + 1
        f.close()
        

