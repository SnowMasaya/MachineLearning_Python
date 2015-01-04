#!/usr/bin/env python

import sys

class writePython:
    
    def __init__(self, fileName, unigram_model):
        self.name = fileName
        self.unigram_model = unigram_model

    def file_write(self):
        f = open(self.name, 'w')
        for k,v in self.unigram_model.items():
            word = k.replace('\n','')
            f.write(word + ' ' + str(v))
            f.write("\n")
        f.close()
