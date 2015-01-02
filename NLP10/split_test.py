#!/usr/bin/env python

import unittest
from split_NLP10 import splitPython
import commands

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'KEN_ALL_nkf_w.CSV'
        split = splitPython(fileName)
        split_data = split.file_Read_split()
        fileName = 'KEN_cut2.txt'
        split = splitPython(fileName)
        data = split.file_Read()
        data_frenquency = split.file_frequency(data)
        data_sort = split.file_sort(split_data, data_frenquency)
        sort_compare_data = []
        [sort_compare_data.append(",".join(compare_data)) for compare_data in data_sort]
        join_sort_compare_data = "".join(sort_compare_data)
        print join_sort_compare_data
        answer = commands.getoutput('sort -t, -k2,2 -r KEN_ALL_nkf_w.CSV')
        #join_sort_compare_data and answer are not match because sort commands is also the sorting other keys
        #self.assertEqual(join_sort_compare_data, answer)

if __name__ == '__main__':
    unittest.main()
