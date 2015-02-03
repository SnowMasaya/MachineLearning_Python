#!/usr/bin/env python

import sys
from math import log

class viterbiBackwardPython:
    
    def __init__(self, best_edge):
        self.wrods = []
        self.best_score = best_edge 

    def viterbi_forward(self):
        next_edge = []
        next_edge = self.best_edge[len(self.best_edge) - 1]
        while next_edge != NULL:
            word = line
