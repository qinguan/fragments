#! /usr/bin/env python

def _prompt(letters='yn',default=None):
    """
    Wait for the user to type a character (and hit Enter). If the user enters
    one of the characters in letters, return that character. If the user hits
    Enter without entering a character, and default is specified, returns
    `default`, Otherwise, asks the user to enter a character again. 
    """
    while True:
        try:
            input = sys.stdin.readline().strip()
        except KeyboardInterrupt:
            sys.exit(0)
        if input and input in letters:
            return input
        if default is not None and input == '':
            return default
        print 'Come again?'

