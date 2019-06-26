#!/usr/bin/env python

import unittest
import functions as api


class MyTest(unittest.TestCase):
    def test(self):
        for l in api.get_list():
            print(l.text)

if __name__ == '__main__':
    unittest.main()
