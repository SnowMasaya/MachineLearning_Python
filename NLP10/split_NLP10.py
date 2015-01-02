#!/usr/bin/env python

import sys
from collections import OrderedDict

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
        return self.data

    def file_Read(self):
        f = open(self.fileName, 'r')
        for line in f:
            word = line.replace('\n','')
            self.data.append(word)
        f.close()
        return self.data

    def file_frequency(self, data):
       data.sort()
       data_uniq = []
       data_frequency = {}
       for x in data:
           if x not in data_uniq:
              data_uniq.append(x)
              data_frequency.update({x:data.count(x)})
       data_frequency_sort = {}
       return OrderedDict(sorted(data_frequency.items(), key=lambda x:x[1], reverse=True))

    def file_sort(self, data, data_frequency):
        data_sort = [] 
        for k in data_frequency.keys():
            for x in data:
                if x[1] == k:
                   data_sort.append(x)
        return data_sort
