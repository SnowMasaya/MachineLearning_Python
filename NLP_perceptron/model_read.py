#!/usr/bin/env python

import sys

class readModelPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.word_map = {}

    def file_read_model(self):
        word = []
        f = open(self.fileName, 'r')
        for line in f:
            word = line.split(" ")
            probability = float(word[1])
            self.word_map.update({word[0]:probability})
        f.close()
        

