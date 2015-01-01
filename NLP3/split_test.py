#!/usr/bin/env python

import unittest
from split_NLP3 import splitPython
from wc_NLP1_copy import wcPython
from split_write import writePython

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'KEN_ALL_1.csv'
        wc = wcPython(fileName)
        wc.file_Read()
        fileName = 'KEN_ALL_nkf_w.CSV'
        split = splitPython(fileName)
        split.file_Read_split()
        self.assertEqual(wc.filedata, split.split_data)
        fileName = 'KEN_ALL_2.csv'
        wc = wcPython(fileName)
        wc.file_Read()
        self.assertEqual(wc.filedata, split.split_data2)
        write = writePython("KEN_cut.txt",split.split_data)
        write.file_write_split()
        write2 = writePython("KEN_cut2.txt",split.split_data2)
        write2.file_write_split()

if __name__ == '__main__':
    unittest.main()
