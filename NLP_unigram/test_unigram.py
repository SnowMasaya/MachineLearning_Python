#!/usr/bin/env python

import unittest
from file_read import readPython
from unigram_train import unigramPython
from unigram_write import writePython
from model_read import readModelPython
import commands

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'wiki-en-train.txt'
        reader = readPython(fileName)
        reader.file_Read()
        unigram = unigramPython(reader.word)
        unigram.unigram_train()
        fileName = 'unigram_model'
        writemodel = writePython(fileName, unigram.word_map)
        writemodel.file_write()
        model = readModelPython(fileName)
        model.file_read_model()
        for k,v in model.word_map.items():
            print "%s %f" % (k,v)
        
        #answer = commands.getoutput('sort -t, -k2,2 -r KEN_ALL_nkf_w.CSV')
        #join_sort_compare_data and answer are not match because sort commands is also the sorting other keys
        #self.assertEqual(join_sort_compare_data, answer)

if __name__ == '__main__':
    unittest.main()
