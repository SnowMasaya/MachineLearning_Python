#!/usr/bin/env python

import sys

class splitPython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.split_data = []

    def file_Read_split(self):
        f = open(self.fileName, 'r')
        for line in f:
            word = line.replace('\n','')
            self.split_data.append(word)
        f.close()
    def file_head(self, data, head_number):
        join_word = []
        count = 0
        for word in data:
            join_word.append(word)
            count = count + 1
            if count == head_number:
               break
        return join_word
