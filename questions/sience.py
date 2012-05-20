#! /usr/bin/env python
# -*- coding: utf-8 -*-  


# 1. Calculate angle of 2 hands of a clock given time.
def calculate_angle(timestr):
    hour,minute = timestr.split(':')
    angle = abs(int(minute) * 6 - (int(hour)%12) * 30 - int(minute)/60.0 * 30)
    if angle > 180:
        return angle - 180
    else:
        return angle
    
def test_calculate_angle():
    assert calculate_angle("15:00") == 90
    assert calculate_angle("24:00") == 0
    assert calculate_angle("12:00") == 0
    assert calculate_angle("9:00") == 90
    assert calculate_angle("2:15") == 22.5


# 2.Given two sorted integer arrays, write an algorithm to get back the intersection.
def get_intersection_1(a,b):
    #print list(set(a).symmetric_difference(set(b)))
    return list(set(a).intersection(set(b)))
def get_intersection_2(a,b):
    return [var for var in a if var in b]

def get_intersection_3(a,b):
    #print list((set(a) | set(b)) - (set(a) & set(b)))
    return list(set(a) & set(b))

def test_get_intersection():
    assert get_intersection_1([1,2,3],[2,3,4]) == [2,3]
    assert get_intersection_2([1,2,3],[2,3,4]) == [2,3]
    assert get_intersection_3([1,2,3],[2,3,4]) == [2,3]

# 3. Array of 100 integers from 1 to 100, shuffled. One integer is taken out, find that integer.
def find_missing_integer(arr_max):
    import random
    import copy
    arr_max = [var for var in range(1,arr_max)]
    arr_ori = copy.deepcopy(arr_max)
    
    random.shuffle(arr_max)
    print arr_max.pop()
    
    return list(set(arr_max).symmetric_difference(set(arr_ori)))[0]
    
    
def test_find_missing_integer():
    print find_missing_integer(101)
    
# 3.1. Array of 100 integers from 1 to 100, shuffled. two integer is taken out,find them out.
def find_missing_integer_2(arr_max):
    import random
    import copy
    arr_max = [var for var in range(1,arr_max)]
    arr_ori = copy.deepcopy(arr_max)
    random.shuffle(arr_max)
    return arr_max.pop(),arr_max.pop(),list(set(arr_max).symmetric_difference(set(arr_ori)))
   
def test_find_missing_integer_2():
    res = find_missing_integer_2(101)
    assert set([res[0],res[1]]) == set(res[2]) # res[2]: the missing integers


# 4. Find n-th largest item in an incoming array.
def find_nth_item_in_array(arr,n):
    arr.sort(lambda x,y: len(y)-len(x))
    return arr[n-1]

def find_nth_item_in_array_2(arr,n,flag = 0): # 0 represent integer array, 1 represent string array
    if flag:
        arr.sort(lambda x,y: len(y)-len(x))
    else:
        arr.sort(lambda x,y: y - x)
    return arr[n-1]
    
def test_find_nth_item_in_array():
    assert find_nth_item_in_array(['abs','de','dede'],2) == 'abs'
    assert find_nth_item_in_array(['abs','de','bhebdha','dede'],3) == 'abs'
    

# 5. Write a function to determine if a string (consisting only of parenthesis) is balanced.
def is_string_balanced(string):
    left = 0
    right = 0
    for var in string:
        if var == '(':
            left = left + 1
        elif var == ')':
            right = right + 1
            
        if(right > left):
            return False
    if(left != right):
        return False
    return True

def test_is_string_balanced():
    assert is_string_balanced('(((())') == False
    assert is_string_balanced('((()))') == True
    assert is_string_balanced(')((') == False


# 6. Given a matrix with 1′s and 0′s, find the number of groups of 1′s.  A group is defined by horiz/vertically adjacent 1′s.
    

# 7. RLE(Run Length Encoding)
#import pdb
#pdb.set_trace()
def encode_with_RLE(input_string):
    lastchar = ''
    count = 1
    newstr = []
    for curchar in input_string:
        if curchar == lastchar and lastchar:
            count = count + 1
        elif curchar != lastchar and lastchar:
            newstr.append((lastchar,count))
            count = 1
            lastchar = curchar
        elif curchar != lastchar:
            lastchar = curchar
    newstr.append((lastchar,count))
    return newstr

def encode_with_RLE_2(input_string):
    if not input_string:
        return None
    lastchar = input_string[0]
    count = 1 
    newstr = []
    for curchar in input_string[1:]:
        if curchar == lastchar:
            count = count + 1
        elif curchar != lastchar:
            newstr.append((lastchar,count))
            count = 1
            lastchar = curchar
    newstr.append((lastchar,count))
    return newstr

def test_encode_with_RLE():
    assert encode_with_RLE_2('aabb    fff   fss') == [('a', 2), ('b', 2), (' ', 4), ('f', 3), (' ', 3), ('f', 1), ('s', 2)]
    assert encode_with_RLE_2('aabbffffss') == [('a', 2), ('b', 2), ('f', 4), ('s', 2)]
    assert encode_with_RLE_2('') == None


# 8. del the duplicate item
def del_duplicate_item(arr): #mess order
    arr2  = list(set(arr))
    arr2.sort()
    return arr2

def del_duplicate_item_2(arr): # origin order
    arr2 = []
    [arr2.append(var) for var in arr if not var in arr2]
    return arr2

def test_del_duplicate_item():
    assert del_duplicate_item([1,2,3,4,3,2,5,8,7]) == [1,2,3,4,5,7,8]
    assert del_duplicate_item(['a','b','z','y','d','b','a']) == ['a','b','d','y','z']
    assert del_duplicate_item_2([1,2,3,4,3,2,5,8,7]) == [1,2,3,4,5,8,7]
    assert del_duplicate_item_2(['a','b','y','d','b','a']) == ['a','b','y','d']



# 9. given two list, exchange the item ,make the diff minimun
def balanced_list(a,b):
    if type(a) == list:
        a.sort()
    else:
        raise "error"
    if type(b) == list:
        b.sort()
    else:
        raise "error"
    import copy
    min_diff = abs(sum(a))+abs(sum(b))
    balanced_a = copy.deepcopy(a)
    balanced_b = copy.deepcopy(b)

    for item in b:
        flag = 0
        temp_b = item
        for var in a:
            cur_diff = abs(sum(a) + item - var - (sum(b)-item + var))
            temp_a = var
            if cur_diff < min_diff and flag == 0: 
                flag = 1
                min_diff = cur_diff
                balanced_a.remove(var)
                balanced_a.append(item)
                balanced_b.remove(item)
                balanced_b.append(var)
            elif cur_diff < min_diff and flag == 1:
                min_diff = cur_diff
                balanced_a.append(temp_a)
                balanced_a.remove(var)
                
    print balanced_a
    print balanced_b
    
def test_balanced_list():

    balanced_list([1,3,4,100],[2,5,6,50])
    
    
# 10. You are given a set of numbers 0 - n. Given a k, print all subsets of size k.
def combination_enumerator(items, n=None):
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
                
def print_all_n_subset(n,k):
    enums = combination_enumerator([i for i in range(n)],k)
    for i in enums:
        print i
    
if __name__ == "__main__":
    #test_calculate_angle()
    #test_get_intersection()
    #test_find_missing_integer()
    #test_find_nth_item_in_array()
    #test_is_string_balanced()
    #test_encode_with_RLE()
    #test_del_duplicate_item()
    test_balanced_list()
