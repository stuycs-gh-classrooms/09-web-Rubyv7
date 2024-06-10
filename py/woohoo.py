#!/usr/bin/python
print('Content-type: text/html\n')

import random


def roll():
    x = random.randrange(6) + 1
    return x

print(roll())

def space():
    x = roll()
    if x == 1:
        y = "You've encountered the Ghost"
        print(monster(y))
        s = ''
        make_body(s)
    elif x == 2:
        y = "You've encountered the witch"
        print(monster(y))
        s = ''
        make_body(s)
    elif x == 3:
        y = "Some birds chrip from afar"
        print(monster(y))
        s = ''
        make_body(s)
    elif x == 4:
        y ="You've encountered a goblin"
        print(monster(y))
        s = ''
        make_body(s)
    elif x == 5:
        y = "Hint: dont..."
        print(monster(y))
        s = ''
        make_body(s)
    elif x == 6:
        y = "you've found a bag of gold!"
        print(monster(y))
        s = ''
        make_body(s)
        
def monster(y):
    title = y
    head ="""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>
    """
    head+= title + '</title></head>'
    return head

def make_body(s):
    body = '<body>' + s + '</body></html>'
    return body

print(monster)
        
