#!/usr/bin/env python

import unittest
from split_NLP7 import splitPython
import commands

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'KEN_ALL_nkf_w.CSV'
        split = splitPython(fileName)
        split.file_Read_split()
        counter = split.file_sort_uniq_wc()
        answer = commands.getoutput('cut -d , -f -1 KEN_ALL_nkf_w.CSV | sort | uniq | wc -l')
        self.assertEqual(counter, int(answer))

if __name__ == '__main__':
    unittest.main()
