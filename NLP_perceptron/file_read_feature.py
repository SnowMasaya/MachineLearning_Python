#!/usr/bin/env python

import sys

class readFeaturePython:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.feature = {}

    def feature_Read(self):
        f = open(self.fileName, 'r')
        words = []
        for line in f:
            rline = line.replace("\n","")
            words = rline.split(" ")
            label = words.pop(0)
            join_words = " ".join(words)
            self.feature.update({label:join_words})
        f.close()
