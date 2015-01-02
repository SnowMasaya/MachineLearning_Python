#!/usr/bin/env python

import sys

class writePython:
    
    def __init__(self, fileName, data):
        self.name = fileName
        self.data = data

    def file_write_split(self):
        f = open(self.name, 'w')
        for line in self.data:
            f.write(line)
            f.write("\n")
        f.close()
