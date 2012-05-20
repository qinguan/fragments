#! /usr/bin/env python
# -*- coding: utf-8 -*-  

def permutation_enumerator(items, n=None):
    '''
    generate all permutation of given items.
    '''
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[:i] + items[i+1:]
            for p in permutation_enumerator(rest, n-1):
                yield v + p
                

def combination_enumerator(items, n=None):
    '''
    generate all combination if given items.
    '''
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[i+1:]
            for c in combination_enumerator(rest, n-1):
                yield v + c

def test():
    enum1 = permutation_enumerator([1,2,3],2)
    for i in enum1:
        print i

    print '************************'
    enum2 = combination_enumerator([4,5,6],2)
    for j in enum2:
        print j

if __name__ == '__main__':
    test()

