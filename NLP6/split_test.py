#!/usr/bin/env python

import unittest
from split_NLP6 import splitPython
from wc_NLP1_copy import wcPython
import commands

TAIL_VALUE = 10

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'KEN_joint.txt'
        split = splitPython(fileName)
        split.file_Read_split()
        tail_data = split.file_tail(split.split_data,TAIL_VALUE)
        tail_data_join = "\n".join(tail_data)
        tail_answer = commands.getoutput('tail -n %d KEN_joint.txt' % TAIL_VALUE)
        self.assertEqual(tail_data_join,tail_answer)


if __name__ == '__main__':
    unittest.main()
