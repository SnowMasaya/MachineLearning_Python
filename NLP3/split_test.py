#!/usr/bin/env python

import unittest
from split_NLP3 import splitPython
from wc_NLP1 import wcPython

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'KEN_ALL_2.csv'
        wc = wcPython(fileName)
        wc.file_Read()
        fileName = 'KEN_ALL_nkf_w.CSV'
        split = splitPython(fileName)
        split.file_Read_split()
        print wc.filedata
        print split.split_data
        self.assertEqual(wc.filedata, split.split_data)
        fileName = 'KEN_ALL_1.csv'
        wc = wcPython(fileName)
        wc.file_Read()
        self.assertEqual(wc.filedata, split.split_data2)

if __name__ == '__main__':
    unittest.main()
