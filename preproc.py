#!/usr/bin/python
import sys
f = open( sys.argv[1] )

for line in f:

    line  = line[:-1] # trailing newline removal

    line = line.replace( r"\[", r"\begin{equation*}" )
    line = line.replace( r"\]", r"\end{equation*}" )
    if line.startswith('$$') :
        line = line.replace( r"$$", r"\begin{equation}",1 )
        line = line.replace( r"$$", r"\end{equation}",1 )
        
    if line.startswith('\> $$') :
        line = line.replace( r"$$", r"\begin{equation}",1 )
        line = line.replace( r"$$", r"\end{equation}",1 )

    if (line.count('.py]')) :
        line = line.replace( r'.py]', r".py`**]" )
        line = line.replace( r'[', r'[**`' )
        
    line = line.replace( r"<br>", r"\newline")
    #    line = line.replace( r"#", r"##",1 )
    while (line.count("> "))  :  line = line.replace( r"> ", r">")
    while (line.count(" <\\")) : line = line.replace( r" <\\", r"<\\")
    line = line.replace( r"1. Ordered TOC", r"")
    line = line.replace( r"{:toc}", r"")
    line = line.replace( r"quote", r"example")
    line = line.replace( r'<span style ="color:red">', r"*")
    line = line.replace( r'<span style="color:red">', r"*")
    line = line.replace( r"<span style = 'color:blue'>", r"***Antwoord:** ")
    line = line.replace( r'<span style = "color:blue">', r"***Antwoord:** ")
    line = line.replace( r'<span style = "color: blue">', r"***Antwoord:** ")
    line = line.replace( r"<span style = 'color: blue'>", r"***Antwoord:** ")
    line = line.replace( r"</span>", r"*")
    
    l = line    

    print(l)

