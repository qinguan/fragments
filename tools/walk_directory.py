#! /usr/bin/env python

def walk_directory(root_directory):
    """
    Generates the absolute path of all files in root_directory`.
    """
    import os
    paths = [os.path.join(root, name)
             for root, dirs, files in os.walk(root_directory)
             for name in files]
    paths.sort()
    if paths is None:
        print 'hello'
    return paths

def test_walk_directory():
    import os
    print  walk_directory(os.getcwd()) 
#    print  walk_directory(os.path.dirname(os.getcwd()))

if __name__ == '__main__':
    test_walk_directory()
