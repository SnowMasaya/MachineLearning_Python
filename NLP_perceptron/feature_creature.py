#!/usr/bin/env python

import sys

class createFeaturePython:
    
    def __init__(self):
        self.phi = {}

    def creature_feature(self, feature, data, flabel):
        words = feature.split(" ")
        for word in words:
            feature  = flabel + word
            self.phi.update({feature:data[word]})
        return self.phi
