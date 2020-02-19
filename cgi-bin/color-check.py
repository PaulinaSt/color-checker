#!/usr/bin/env python3
import cgi
import os
path = "/Users/Paulina/foundations/color-checker/cgi-bin/colors.txt"

form = cgi.FieldStorage()
color = form.getvalue('color')
#color="blue"
#colors = ["blue", "green", "red"]

yescolor = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
  </head>  
  <body>
    <h1>Hello !</h1>
    <p>Congrats, {color} is a color.</p>
    <svg width="400" height="110">
    <rect width="300" height="100" style="fill:{color};stroke-width:3;stroke:rgb(0,0,0)" />
</svg>
  </body>
</html>
""".format(color=color)

nocolor = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
  </head>  
  <body>
    <h1>Hello !</h1>
    <p>Oh no, {color} is not a color.</p>
  </body>
</html>
""".format(color=color)

f=open(path,"r")
fi= f.read()
if color in fi:
  print (yescolor)
else:
  print(nocolor)

"""
if color in colors:
  print (yescolor)
else:
  print (nocolor)
"""