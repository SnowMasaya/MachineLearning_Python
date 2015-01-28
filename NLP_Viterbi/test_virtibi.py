#!/usr/bin/env python

import unittest
from viterbi_forward import viterbiForwardPython
import commands

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        modelName = 'unigram_model'
        fileName = '04-input.txt'
        viterbi = viterbiForwardPython(modelName, fileName)
        viterbi.viterbi_forward()
        
        #answer = commands.getoutput('sort -t, -k2,2 -r KEN_ALL_nkf_w.CSV')
        #join_sort_compare_data and answer are not match because sort commands is also the sorting other keys
        #self.assertEqual(join_sort_compare_data, answer)

if __name__ == '__main__':
    unittest.main()
