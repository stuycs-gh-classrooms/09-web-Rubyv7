#!/usr/bin/python
print('Content-type: text/html\n')

import random
import cgitb #
cgitb.enable()
import cgi
data = cgi.FieldStorage()

w = open("witchandthebeast.txt", encoding="utf-8")
w = w.read()
gh = open("Ghosts.txt", encoding="utf-8")
gh = gh.read()
gob =  open("Goblin.txt", encoding="utf-8")
gob = gob.read()

html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <link href="woo.css" rel="stylesheet">
    """
        


def make_body(s, mon):
    s = s.replace('.', ' .')
    s = s.split()
    info = s.index(mon)
    found = s[info:info+100]
    period = found.index('.')
    period2 = s[info+period +1:info+100]
    period3 = period2.index('.')
    b = ' '.join(s[info: period3 + period + info + 1]) + '.'
    body = '<p>'+ b 
    return body

w = make_body(w, 'Witches')
gh = make_body(gh, 'Ghost')
gob = make_body(gob, 'Goblins')



def space():
    x = random.randrange(6) + 1
    if x == 1:
        y = "You've encountered a ghost."
        text = '<h1>' + y + '</h1></head>' +'\n' + '<body>' + gh + '</body>' + '</p>' + '<p>' + str('<select name="name"> <option value="v0">Run away</option> <option value="v1">Fight</option> <option value="v2">Hide</option></select>') +'<form action="woohoo.py" method="GET">'  + '<img src="https://i.icanvas.com/BFD635?d=2&sh=v&p=1&bg=g">' + '\n' '\n' + '<p>' + '<input type="submit" name="submit"/>' + '</p>'
    elif x == 2:
        y = "You've encountered a witch!"
        text = '<h1>' + y + '</h1></head>' +'\n' + '<body>' + w + '</body>' + '</p>' + '<p>' + str('<select name="name"> <option value="v0">Run away</option> <option value="v1">Fight</option> <option value="v2">Hide</option></select>')+ '<form action="woohoo.py" method="GET">'  + '<img src="https://the-public-domain-review.imgix.net/essays/woodcuts-and-witches/34427876715_0e59110873_b.jpg?fit=max&w=1200&h=850">' + '\n' + '<p>' + '<input type="submit" name="submit"/>' + '</p>' 
    elif x == 3:
        y = "Some birds chrip from afar."
        text = '<h1>' + y + '</h1></head>' +'\n' + '<body>' + 'They soar through the forest, chirping and singing. They cause you no harm and you can continue on your adventure.'  + '</p>' + '<form action="woo.py" method="GET">' + '<img src="https://cosmosmagazine.com/wp-content/uploads/2020/02/190122-bird-full.jpg">'  + '</body>' + '\n' + '<p>' + '\n' + '<p>' + '<input type="submit" name="submit" value="Roll again!">' 
    elif x == 4:
        y ="You've encountered a goblin."
        text = '<h1>' + y + '</h1></head>' +'\n' + '<body>' + gob + '</body>' + '</p>' + '<p>' + str('<select name="name"> <option value="v0">Run away</option> <option value="v1">Fight</option> <option value="v2">Hide</option></select>') + '<form action="woohoo.py" method="GET">'  + '<img src="https://runic.com/artwork/goblin-hunting-party-large.jpg">' + '<form action="woo.py" method="GET">' '\n' + '<p>' + '<input type="submit" name="submit"/>' + '</p>'
    elif x == 5:
        y = "You hear some branches breaking."
        text = '<h1>' + y + '</h1></head>' +'\n' + '<body>' +'It was just a cute fox with a bird in its mouth. It ignored you and you can continue.' + '<form action="woo.py" method="GET">' + '<img src="https://images.fineartamerica.com/images-medium-large-5/fox-in-a-forest-daniel-eskridge.jpg">' + '</body>' + '\n' + '<p>' + '<input type="submit" name="submit" value="Roll again!">' + '</p>'
    elif x == 6:
        y = "You've found a bag of gold!"
        text = '<h1>' + y + '</h1></head>' +'\n' + '<body>' + 'Nice find! Now continue on your journey.'  + '<form action="woo.py" method="GET">' + '<img src="https://img.freepik.com/premium-photo/bag-gold-coins-with-number-3-it_81048-6884.jpg">' + '</body>' + '\n' + '<p>' +'<input type="submit" name="submit" value="Roll again!">' + '</p>'
    return text 
 
text = space()

html += "\n"
html += text
html += ""
html += '</form>'
html += '</html>'
print(html)
# 
# 
