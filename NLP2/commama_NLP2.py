#!/usr/bin/env python

import sys

class tabPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.filedata = []

    def file_Read(self):
        f = open(self.fileName, 'r')
        for line in f:
            commama_space = line.replace(',',' ')
            self.filedata.append(commama_space)
        f.close()

