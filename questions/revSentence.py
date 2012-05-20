#!/usr/bin/python

def revSentence(sentence):
    """
    the function is used to reverse the words order in one sentence.
    eg.
    this is a real world. ---> world real a is this
    """
    words = sentence.split(' ')
    words.reverse()
    newsen = " ".join([item for item in words])
    return newsen

import unittest

class revSentenceTestCase(unittest.TestCase):
    """
    test the function revSentence.
    """
     
    def setUP(self):
        pass
    def tearDown(self):
        pass

    def testRevSentence(self):
        self.assertEqual(revSentence("this is a real world"),"world real a is this")
        self.assertEqual(revSentence("coding is full of fun"),"fun of full is coding")
        
if __name__ == '__main__':
    unittest.main()
