#!/usr/bin/env python

import sys

class readPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.word = []
        self.total_word = 0

    def file_Read(self):
        f = open(self.fileName, 'r')
        words = []
        for line in f:
            rline = line.replace("\n","")
            words = rline.split(" ")
            words.append("</s>")
            self.word.append(words)
            self.total_word = self.total_word + len(words)
        f.close()
