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
    def file_join(self, data, data2):
        join_word = []
        join_word = zip(data,data2)
        return join_word
    def file_tab(self, data):
        tab_word = []
        for line in data:
            tab_word.append("\t".join(line))
        return tab_word
