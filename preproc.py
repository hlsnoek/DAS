#!/usr/bin/python
import sys
f = open( sys.argv[1] )

inExEnv = False

for line in f:
    if (line.startswith('>')) : inExEnv = True
    else : inExEnv = False

    line  = line[:-1] # trailing newline removal
    line = line.replace( r"\displaystyle" , r"")
    line = line.replace( r"\[", r"\begin{equation*}" )
    line = line.replace( r"\]", r"\end{equation*}" )
    line = line.replace( r"<br>", r'\newline')

    if line.startswith('> $$') :
        line = line.replace( r"$$", r" \begin{equation*}",1 )
        line = line.replace( r"$$", r"\end{equation*}",1 )

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


    
    if line.startswith('$$') :
        line = line.replace( r"$$", r"\begin{equation}",1 )
        line = line.replace( r"$$", r"\end{equation}",1 )
        

    if (line.count('.py]')) :
        line = line.replace( r'.py]', r".py`**]" )
        line = line.replace( r'[', r'[**`' )
        


    if (line.count('.png)')) :
        title = line[line.rfind('[')+1:line.find(']')]
        name = line[line.rfind('(')+1:line.find('.png')]
        if (inExEnv) : line += '\n\\captionof{figure}{'+title+'}'
        else : line += '\n\\caption{'+title+'}'
        line += '\n\\label{fig:'+name+'}'
        if(inExEnv) : line += '\\vspace{0.2cm}'
        
    #    line = line.replace( r"#", r"##",1 )

    if (line.count('<!--FIG')) :
        line = line.replace( r'<!--FIG ', r' ')
        line = line.replace( r'-->', r' ')

    if (line.count('<!--REF')) :
        line = line.replace( r'<!--REF', r'')
        line = line.replace( r'-->', r' ')

    if (line.count('<!--COMMENT')) :
        line = line.replace( r'<!--COMMENT', r'')
        line = line.replace( r'-->', r' ')

    if (line.count('<!--APP')) :
        line = line.replace( r'<!--APP', r'')
        line = line.replace( r'-->', r' ')


    l = line    

    print(l)

