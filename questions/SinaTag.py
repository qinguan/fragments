#! /usr/bin/env python
# -*- coding: utf-8 -*-  

#1、给定sina微博的全部用户（1亿以上）和标签（uniq的标签 
#30万左右）的关系，系统找出共有2个或以上标签的用户对，并给出这些标签是哪些。 
#input_file： 
#userid,taglist 
#output_file: 
#userid,userid,con-taglist (sizeof(con_taglist)>=2) 
#例如 
#AA，体育 新闻 清华 百年校庆 
#BB，娱乐 八卦 清华 新闻 
#CC，体育 娱乐 新闻 
#DD，八卦 新闻 娱乐 
#则输出 
#AA，BB 清华 新闻 
#AA，CC 体育 新闻 
#BB，CC 娱乐 新闻 
#BB，DD 娱乐 八卦 新闻 
#CC，DD 娱乐 新闻 
#要求时空复杂度最低。 

def split_lines(line):
    '''
    input: 
    AA,taglist
    output:
    AA,(tag1,tag2,tag3...)
    '''
    if not line:
        return
    userid,taglist = line.split(',')
    tag_set = set(taglist.split())
    return userid,tag_set

def read_context(datafile):
    '''
    read data from a given file and split the tag data.
    return [(AA,(tag1,tag2,tag3...))...]
    '''
    try:
        fp = open(datafile,'rb')
    except:
        print 'can open the %' % datafile
        return
    readlines = fp.readlines()
    res = map(split_lines,[line for line in readlines])
    fp.close()
    return list(res)

def get_common_tag_set(user_a_info,user_b_info):
    '''
    input:
    user_a_info:AA,(tag1,tag2,tag3...)
    user_b_info:BB,(tag1,tag2,tag3...)
    '''
    user_a_id = user_a_info[0]
    user_b_id = user_b_info[0]
    common_tag_set = user_a_info[1].intersection(user_b_info[1])
    return user_a_id,user_b_id,common_tag_set

def get_result(user_tag_data):
    '''
    user_tag_data: the output of read_context function
    '''
    if not user_tag_data:
        return
    res = []
    for i in range(len(user_tag_data)-1):
        for j in range(i+1,len(user_tag_data)):
            print i,j
            res.append(get_common_tag_set(user_tag_data[i],user_tag_data[j]))
    return filter(lambda x:len(x[2]) > 1 ,res)

if __name__ == '__main__':
    print get_result(read_context('test'))
