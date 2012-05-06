#! /usr/bin/python

"""
 An example writing code according Pylint.
"""

def is_unique_char(in_str):
    """
    implement an algorithm to determain if a string has all unique characters.
    """
    exist_str = []
    for i in xrange(len(in_str)):
        if(in_str[i] not in exist_str):
            exist_str.append(in_str[i])
        else:
            return False
    return True

import unittest
class IsUniqueCharTestCase(unittest.TestCase):
    """
    unit test class.
    """
    def test_is_unique_char(self):
        """
        test the function is_unique_char.
        """
        self.assertEqual(is_unique_char("aba"), False)
        self.assertEqual(is_unique_char("abc"), True)
        self.assertEqual(is_unique_char(""), True)
        self.assertEqual(is_unique_char("aaaaa"), False)

if __name__ == "__main__":
    unittest.main()
