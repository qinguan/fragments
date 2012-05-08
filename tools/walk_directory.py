#! /usr/bin/env python

def _walk_directory(root_directory):
    """
    Generates the paths of all that are ancestors of `root_directory`.
    """
    import os
    paths = [os.path.join(root, name)
             for root, dirs, files in os.walk(root_directory)
             for name in files]

    paths.sort()
    return paths
