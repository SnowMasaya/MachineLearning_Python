#!/usr/bin/env python

import sys

class splitPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = []

    def file_Read_split(self):
        f = open(self.fileName, 'r')
        for line in f:
            split_line = line.split(',')
            self.data.append(split_line[0])
        f.close()

    def file_sort_uniq_wc(self):
        seen = set()
        seen_add = seen.add
        self.data.sort()
        return len([x for x in self.data if x not in seen and not seen_add(x)])
