#!/usr/bin/env python

import sys

class createFeaturePython:
    
    def __init__(self, x, data):
        self.feature = x
        self.data = data
        self.phi = {}
    def creature_feature(self):
        print {k:v for k,v in self.data.items()}
        words = self.feature.split(" ")
        for word in words:
            feature  = "UNI:" + word
            self.phi.update({feature:self.data[word]})
        return self.phi
