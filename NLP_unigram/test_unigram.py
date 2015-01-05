#!/usr/bin/env python

import unittest
from file_read import readPython
from unigram_train import unigramPython
from unigram_write import writePython
from model_read import readModelPython
from evaluate_model import evaluateModelPython
import commands

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = '01-train-input.txt'
        reader = readPython(fileName)
        reader.file_Read()
        unigram = unigramPython(reader.word, reader.total_word)
        unigram.unigram_train()
        fileName = 'unigram_model'
        writemodel = writePython(fileName, unigram.word_map)
        writemodel.file_write()
        model = readModelPython(fileName)
        model.file_read_model()
        #print {k:v for k,v in unigram.word_map.items()}
        fileName = '01-test-input.txt'
        test = evaluateModelPython(fileName, model.word_map)
        test.evaluate_model()
        print "entropy = "  + str(test.H / test.total_word_number )
        print "coverage = "  + str( 1.0 * (test.total_word_number - test.unknown_word_number) / test.total_word_number) 
        
        #answer = commands.getoutput('sort -t, -k2,2 -r KEN_ALL_nkf_w.CSV')
        #join_sort_compare_data and answer are not match because sort commands is also the sorting other keys
        #self.assertEqual(join_sort_compare_data, answer)

if __name__ == '__main__':
    unittest.main()
