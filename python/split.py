#!/usr/bin/env python
'''
Split

Input: string and and character to split on
Output: create list with the string split based on character submitted

'''

def split(string, char=None):
    create_list = []
    start,stop = 0,0
    if char==None:
        char = ''
    for i, letter in enumerate(string):
        if letter == char: 
            stop = i
            create_list.append(string[start:stop])
            start = i+1
        if i == (len(string)-1):
            create_list.append(string[start:len(string)])
    return create_list

print split('s p l i t', ' ')
# how to run it with no split value?
