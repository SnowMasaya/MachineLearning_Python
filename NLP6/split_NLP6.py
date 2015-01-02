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
    def file_tail(self, data, tail_number):
        data.reverse()
        join_word = []
        count = 0
        for word in data:
            join_word.append(word)
            count = count + 1
            if count == tail_number:
               break
        join_word.reverse()
        return join_word
