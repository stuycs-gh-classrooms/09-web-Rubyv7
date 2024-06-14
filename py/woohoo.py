#!/usr/bin/python
print('Content-type: text/html\n')

import random
import cgitb #
cgitb.enable()
import cgi
data = cgi.FieldStorage()

html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <link href="woo.css" rel="stylesheet">
    """
def ifin():
    x = random.randrange(6) + 1
    f = ''
    if x <= 2:
        f = '<h1> You died, would you like to try again? </h1> </head <\n>' + '<p>' + '<form action="woo.py" method="GET">' + '<input type="submit" name="submit" value="Try again!">' +'</p>'
    elif x <= 5:
        f = '<h1> You successfully survived, keep moving through the forest! </h1> </head <\n>' + '<form action="woo.py" method="GET">' + '<input type="submit" name="submit" value="Roll again!">'
    if x == 6:
        f ='<h1>You have won!</h1> </head> <\n>' + '<body> Would you like to play again?<form action="woo.py" method="GET">' + '<input type="submit" name="submit" value="Play again!">' +'</p>'
    return f
 

html +=  ifin()
html += '</form>'
html += '</html>'
print(html)
