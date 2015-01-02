#!/usr/bin/env python

import sys
from operator import itemgetter

class splitPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = []

    def file_Read_split(self):
        f = open(self.fileName, 'r')
        for line in f:
            split_line = line.split(',')
            self.data.append(split_line)
        f.close()

    def file_sort_column2_column1(self):
        return sorted(self.data, key=itemgetter(1,0), reverse=True)
