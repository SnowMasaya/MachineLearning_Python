#!/usr/bin/env python

import sys

class readPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.word = []

    def file_Read(self):
        f = open(self.fileName, 'r')
        for line in f:
            self.word.append(line.split(" "))
        f.close()
        

