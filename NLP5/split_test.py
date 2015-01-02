#!/usr/bin/env python

import unittest
from split_NLP5 import splitPython
from wc_NLP1_copy import wcPython
import commands

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'KEN_joint.txt'
        split = splitPython(fileName)
        split.file_Read_split()
        head_data = split.file_head(split.split_data,10)
        head_data_join = "\n".join(head_data)
        head_answer = commands.getoutput('head -n 10 KEN_joint_answer.txt')
        self.assertEqual(head_data_join,head_answer)


if __name__ == '__main__':
    unittest.main()
