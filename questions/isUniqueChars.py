#! /usr/bin/python

def isUniqueChar(in_str):
    """
    implement an algorithm to determain if a string has all unique characters.
    """
    exist_str=[]
    for i in xrange(len(in_str)):
        if(in_str[i] not in exist_str):
            exist_str.append(in_str[i])
        else:
            return False
    return True

import unittest
class isUniqueCharTestCase(unittest.TestCase):
    def testIsUniqueChar(self):
        self.assertEqual(isUniqueChar("aba"),False)
        self.assertEqual(isUniqueChar("abc"),True)
        self.assertEqual(isUniqueChar(""),True)
        self.assertEqual(isUniqueChar("aaaaa"),False)
if __name__ == "__main__":
    unittest.main()
