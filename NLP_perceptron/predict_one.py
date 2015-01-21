#!/usr/bin/env python

class predictOnePython:
    
    def __init__(self, fileName, weight, phi, flabel):
        self.fileName = fileName
        self.weight = weight
        self.phi = phi
        self.flabel = flabel
        self.score = 0

    def predict(self):
        f = open(self.fileName, 'r')
        words = []
        for line in f:
            rline = line.replace("\n","")
            words = rline.split(" ")
            score = 0
            for word in words:
                name = self.flabel + word
                if self.weight[name]:
                   score = score + self.phi[name] * self.weight[name]
            if score >= 0:
               print str(1) + "\t"+ line
            else:
               print str(-1) + "\t"  + line
