#!/usr/bin/env python

class predictOnePython:
    
    def __init__(self, weight, phi):
        self.weight = weight
        self.phi = phi
        self.score = 0

    def predict(self):
        for name,value in self.phi.iteritems():
            if self.weight[name]:
               score = score + value * self.weight[name]
        if score >= 0:
           return 1
        else:
           return -1
