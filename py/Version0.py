#!/usr/bin/python
print('Content-type: text/html\n')

import random
import cgitb #
cgitb.enable()


import cgi

def space():
    x = random.randrange(6) + 1
    if x == 1:
        y = "You've encountered the Ghost"
        text = monster(y, '')
        s = ''
        make_body(s)
    elif x == 2:
        y = "You've encountered the witch"
        text = monster(y, '')
        s = ''
        make_body(s)
    elif x == 3:
        y = "Some birds chrip from afar"
        text = monster(y, '')
        s = ''
        make_body(s)
    elif x == 4:
        y ="You've encountered a goblin"
        text = monster(y, '')
        s = ''
        make_body(s)
    elif x == 5:
        y = "Hint: dont..."
        text = monster(y, '')
        s = ''
        make_body(s)
    elif x == 6:
        y = "you've found a bag of gold!"
        text = monster(y, '')
        s = ''
        make_body(s)
        
def monster(title, body):
    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    """
    html+= '<title>' + title + '</title></head>'
    html+= '<body>' + body + '</body>'
    html+= '</body></html>'
    return html


def make_body(s, mon):
    s = s.split()
    info = s.find(mon)
    body = '<body>' + s + '</body></html>'
    return body

def make_form(path):
    html = """
    <form action="dynaform.py" method="GET">
    Pick a name! <input type="text" name="name" value="...">
    <br>
    """
    radio = ''
  
    for option in path:
        iput = '<div>'
        iput+= '<input type="radio" name="bgcolor" value="' + option + '">'
        iput+= option + '</div>'
        radio+= iput
    
    html+= radio
    html+= '<input type="submit" value="Submit!">'
    return html



data = cgi.FieldStorage()
