#!/usr/bin/env python

from feature_creature import createFeaturePython

class onlineLearningPython:
    
    def __init__(self, feature, data):
        self.feature = feature
        self.data = data
        self.phi = {}
        self.label = 0
        self.weight = []
        self.iteration = 1000

    def online_learning(self):
        count = 0
        while self.iteration >= count:
              count = count + 1
              for x,y in self.feature.iteritems():
                  cfeature = createFeaturePython(y, self.data)
                  self.phi = cfeature.creature_feature()
                  print self.phi
                  #self.label = predict_one(self.weight, self.phi)
                  #if self.label != y:
                  #   update_weight(self.weight, self.phi, self.label)
