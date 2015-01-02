#!/usr/bin/env python

import unittest
from split_NLP9 import splitPython
import commands
import itertools

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'KEN_ALL_nkf_w.CSV'
        split = splitPython(fileName)
        split.file_Read_split()
        sort_data = split.file_sort_column2_column1()
        sort_compare_data = []
        [sort_compare_data.append(",".join(compare_data)) for compare_data in sort_data]
        join_sort_compare_data = "".join(sort_compare_data)
        print join_sort_compare_data
        answer = commands.getoutput('sort -t, -k2,2 -k1,1 -r KEN_ALL_nkf_w.CSV')
        #print answer
        #self.assertEqual(join_sort_compare_data, answer)

if __name__ == '__main__':
    unittest.main()
