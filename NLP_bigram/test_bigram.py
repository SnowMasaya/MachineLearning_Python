#!/usr/bin/env python

import unittest
from file_read import readPython
from bigram_train import bigramPython
from bigram_write import writePython
from model_read import readModelPython
from evaluate_model import evaluateModelPython
import commands

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = '02-train-input.txt'
        reader = readPython(fileName)
        reader.file_Read()
        bigram = bigramPython(reader.word)
        bigram.bigram_train()
        print {k:v for k,v in bigram.word_map.items()}
        print {k:v for k,v in bigram.lambda_word_map.items()}
        fileName = 'bigram_model'
        writemodel = writePython(fileName, bigram.word_map)
        writemodel.file_write()
        model = readModelPython(fileName)
        model.file_read_model()
        fileName = '02-train-input.txt'
        test = evaluateModelPython(fileName, model.word_map, bigram.lambda_word_map)
        test.evaluate_model()
        print "entropy = "  + str(test.H / test.total_word_number )
        
        #answer = commands.getoutput('sort -t, -k2,2 -r KEN_ALL_nkf_w.CSV')
        #join_sort_compare_data and answer are not match because sort commands is also the sorting other keys
        #self.assertEqual(join_sort_compare_data, answer)

if __name__ == '__main__':
    unittest.main()
