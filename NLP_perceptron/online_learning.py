#!/usr/bin/env python

from feature_creature import createFeaturePython
from predict_one import predictOnePython
from update import updatePython

class onlineLearningPython:
    
    def __init__(self, feature, data, flabel):
        self.feature = feature
        self.data = data
        self.phi = {}
        self.label = 0
        self.flabel = flabel
        self.weight = {}
        self.iteration = 1000

    def online_learning(self):
        count = 0
    # initinalize
        for key,value in self.feature.iteritems():
            words = value.split(" ")
            [self.weight.update({self.flabel + word:0}) for word in words]
    # update weight
        while self.iteration >= count:
              count = count + 1
              for key,value in self.feature.iteritems():
                  cfeature = createFeaturePython(value, self.data, self.flabel)
                  self.phi = cfeature.creature_feature()
                  print self.phi
                  self.label = predictOnePython(self.weight, self.phi)
                  if self.label != key:
                     update_weight = updatePython(self.weight, self.phi, key)
                     update_weight.update()
