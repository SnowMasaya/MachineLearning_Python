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
            label = rline.split("\t")
            words = label[1].split(" ")
            join_words = " ".join(words)
            self.feature.update({label[0]:join_words})
        f.close()
