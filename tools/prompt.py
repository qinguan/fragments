#! /usr/bin/env python

"""
a useful function for prompt.
"""

def _prompt(letters='yn', default=None):

    r"""
    Wait for the user to type a character (and hit Enter). If the user enters
    one of the characters in letters, return that character. If the user hits
    Enter without entering a character, and default is specified, returns
    `default`, Otherwise, asks the user to enter a character again. 
    """

    import sys
    while True:
        try:
            inputstr = sys.stdin.readline().strip()
        except KeyboardInterrupt:
            sys.exit(0)
        if inputstr and inputstr in letters:
            return inputstr
        if default is not None and inputstr == '':
            return default
        print 'Come again?'

