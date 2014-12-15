#!/usr/bin/env python

import unittest
from wc_NLP1 import wcPython

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'wc_test_data.txt'
        wc = wcPython(fileName)
        wc.file_Read()
        self.assertEqual(len(wc.filedata), 3)

if __name__ == '__main__':
    unittest.main()
