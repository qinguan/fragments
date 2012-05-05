#! /usr/bin/python

def fibonacci():
    a, b = 0, 1
    while True:
        yield a 
        a, b = b, a+b
fib = fibonacci()
print [fib.next() for i in range(10)]
