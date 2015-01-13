#!/usr/bin/env python

class updatePython:
    
    def __init__(self, weight, phi, y):
        self.weight = weight
        self.phi = phi
        self.y = y

    def update(self):
        for name,value in self.phi.iteritems():
            self.weight[name] = self.weight[name] + value * self.y
