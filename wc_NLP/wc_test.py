#!/usr/bin/env python

import unittest
from wc_NLP1 import wcPython

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = '../KEN_ALL.CSV'
        wc = wcPython(fileName)
        wc.file_Read()
        self.assertEqual(len(wc.filedata), 123721)

if __name__ == '__main__':
    unittest.main()
