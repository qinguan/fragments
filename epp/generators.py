#! /usr/bin/env python

def fibonacci():
    a, b = 0, 1
    while True:
        yield a 
        a, b = b, a+b
fib = fibonacci()
print [fib.next() for i in range(10)]

#********************************************#
import multitask

def coroutine_1():
    """
    .
    """
    for i in range(3):
        print 'c1'
        yield

def coroutine_2():
    """
    .
    """
    for i in range(3):
        print 'c2'
        yield i

multitask.add(coroutine_1())
multitask.add(coroutine_2())
multitask.run()

#********************************************#
#from __future__ import with_statement
