#!/usr/bin/env python

import unittest
from file_read import readPython
from unigram_train import unigramPython
from unigram_write import writePython
from file_read_feature import readFeaturePython
from online_learning import onlineLearningPython
from predict_one import predictOnePython
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
        fileName = '03-train-input.txt'
        cfeature = readFeaturePython(fileName)
        cfeature.feature_Read()

        print {k:v for k,v in cfeature.feature.items()}
        online = onlineLearningPython(cfeature.feature, unigram.word_map, "UNI:")
        online.online_learning()
        print {k:v for k,v in online.phi.items()}

        predict = predictOnePython("03-train.txt", online.weight, online.phi, "UNI:")
        predict.predict()
        
        #model = readModelPython(fileName)
        #model.file_read_model()
        #print {k:v for k,v in unigram.word_map.items()}
        #fileName = '01-test-input.txt'
        #self.assertEqual(join_sort_compare_data, answer)

if __name__ == '__main__':
    unittest.main()
