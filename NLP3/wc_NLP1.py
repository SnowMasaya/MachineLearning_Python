#!/usr/bin/env python

import sys

class wcPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.filedata = []

    def file_Read(self):
        f = open(self.fileName, 'r')
        for line in f:
            self.filedata.append(line)
        f.close()

