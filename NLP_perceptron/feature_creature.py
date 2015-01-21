#!/usr/bin/env python

import sys

class createFeaturePython:
    
    def __init__(self, x, data, flabel):
        self.flabel = flabel
        self.feature = x
        self.data = data
        self.phi = {}

    def creature_feature(self):
        words = self.feature.split(" ")
        for word in words:
            feature  = self.flabel + word
            self.phi.update({feature:self.data[word]})
        return self.phi
