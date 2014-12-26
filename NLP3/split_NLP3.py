#!/usr/bin/env python

import sys

class splitPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.split_data = []
        self.split_data2 = []

    def file_Read_split(self):
        f = open(self.fileName, 'r')
        for line in f:
            split_line = line.split(',')
            self.split_data.append(split_line[1])
            self.split_data2.append(split_line[2])
        f.close()
