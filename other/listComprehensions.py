#! /usr/bin/python

seq = ["one","two","three"]

#method 1
for i,elem in enumerate(seq):
    seq[i] = '%d: %s' %(i,seq[i])

#method 2
def treatment(pos,elem):
    return '%d: %s' % (pos,elem)

[treatment(i,el) for i,el in enumerate(seq)]
