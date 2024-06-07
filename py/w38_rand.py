#!/usr/bin/python
print('Content-type: text/html\n')

import random

space = 0

def roll():
    x = random.randrange(6) + 1
    return x

print(roll())

def spacer():
    space = space + roll()
    return space
print(space)