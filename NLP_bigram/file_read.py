#!/usr/bin/env python

import sys

class readPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.word = []

    def file_Read(self):
        f = open(self.fileName, 'r')
        words = []
        for line in f:
            rline = line.replace("\n","")
            words = rline.split(" ")
            words.append("</s>")
            words.insert(0, "<s>")
            self.word.append(words)
        f.close()

