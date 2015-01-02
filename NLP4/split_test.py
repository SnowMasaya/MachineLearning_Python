#!/usr/bin/env python

import unittest
from split_NLP4 import splitPython
from wc_NLP1_copy import wcPython
from split_write import writePython

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'KEN_cut.txt'
        split = splitPython(fileName)
        split.file_Read_split()
        split_data = split.split_data
        fileName = 'KEN_cut2.txt'
        split = splitPython(fileName)
        split.file_Read_split()
        split_data2 = split.split_data
        join_word = split.file_join(split_data, split_data2)
        tab_word = split.file_tab(join_word)
        #print tab_word
        fileName = 'KEN_joint_answer.txt'
        wc = wcPython(fileName)
        wc.file_Read()
        self.assertEqual(wc.filedata, tab_word)
        write = writePython("KEN_joint.txt",tab_word)
        write.file_write_split()


if __name__ == '__main__':
    unittest.main()
