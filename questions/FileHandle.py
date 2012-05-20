#! /usr/bin/env python
# -*- coding: utf-8 -*-  

def count_duplicate_lines(filename):
    '''
    count the duplicate lines in a given file.
    eg:
    file
    "
    abc
    hjg
    bcd
    abc
    bcd
    kkk
    "
    return [(2, 'abc'), (2, 'bcd'), (1, 'hjg'), (1, 'kkk')]
    '''
    
    fd = open(filename, 'r')
    lines = fd.readlines()
    res_line = {} # count the number of every unique line
    res_temp = [] # mark the order of lines
    for line in lines:
        item = line.strip()
        if item not in res_line:
            res_line[item] = 1
            res_temp.append(item)
        else:
            res_line[item] += 1
            
    res = []
    for i in res_temp:
        res.append((res_line[i],i))
        
    res.sort(lambda x,y: y[0]-x[0]) # sorted by frequence of line
    return res

def show_line_without_given_character(filename,character):
    '''
    print all line without character in fllename.
    eg:
    file:
    abc
    bcd
    kkk
    ne48de
    bhm48lk
    sbdhe48l
    
    output:
    abc
    bcd
    kkk
    '''
    fd = open(filename, 'r')
    lines = fd.readlines()
    for line in lines:
        if character in line:
            continue
        else:
            print line.strip()
    
def del_duplicate_line_in_file(filename):
    '''
    delete all duplicate lines in a given file.
    eg:
    file:
    abc
    hjg
    bcd
    abc
    bcd
    kkk
    ne48de
    bhm48lk
    sbdhe48l
    
    output:
    abc
    hjg
    bcd
    kkk
    ne48de
    bhm48lk
    sbdhe48l
    '''
    
    fd = open(filename,'r')
    lines = fd.readlines()
    res_line = []
    for line in lines:
        item = line.strip()
        if item not in res_line:
            res_line.append(item)
            
    return '\n'.join(res_line)

if __name__ == '__main__':
    print count_duplicate_lines('E:/python/test.txt')
    show_line_without_given_character('E:/python/test.txt','48')
    print del_duplicate_line_in_file('E:/python/test.txt')