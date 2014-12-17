#!/usr/bin/env python

import unittest
from commama_NLP2 import tabPython
from wc_NLP1 import wcPython

class TestSeaquenceFunction(unittest.TestCase):
    def testWc(self):
        fileName = 'KEN_ALL.CSV'
        wc = wcPython(fileName)
        wc.file_Read()
        fileName = '../KEN_ALL_nkf_w.CSV'
        tab = tabPython(fileName)
        tab.file_Read()
        self.assertEqual(wc.filedata, tab.filedata)

if __name__ == '__main__':
    unittest.main()
