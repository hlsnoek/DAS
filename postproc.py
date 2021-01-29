#!/usr/bin/python
import sys
f = open( sys.argv[1] )

for line in f:
    line  = line[:-1] # trailing newline removal
    if(line.count("documentclass")) :
        line = '\documentclass[11pt,twoside,a4paper,pdftex]{book}'
        line += '\\usepackage{capt-of}\n\\usepackage{xcolor}'
        line += '\n\\usepackage{tcolorbox}\n'
        line += '\\usepackage{tikz, lipsum}\n\\usepackage{fancyvrb}\n'
        line += '\\tcbuselibrary{breakable,skins}\n\\tcbset{enhanced jigsaw}'
        line += '\n\\newenvironment{example}{\\vspace{0.5cm}\\begin{tcolorbox}[breakable,title=Voorbeeld:,colframe=teal,colback=teal!5!white]}{\\end{tcolorbox}\\vspace{0.5cm}}'
        line += '\n\\newenvironment{antwoord}{\\begin{tcolorbox}[breakable, colback=grey}{\\end{tcolorbox}}'

        line += '\\setlength{\\textheight}{21.5cm}\\setlength{\\textwidth}{15.0cm}\n'
        line += '\\setlength{\\topmargin}{0.0cm}\n'
        line += '\\setlength{\\oddsidemargin}{0.0cm}\n'
        line += '\\setlength{\\evensidemargin}{0.0cm}\n'
        line += '\\renewcommand{\\appendixname}{}\n'
        line += '\\renewcommand{\\chaptername}{Hoofdstuk}\n'
        line += '\\renewcommand{\\contentsname}{Inhoud}\n'
        line += '\\renewcommand{\\partname}{Deel}\n'
        line += '\\graphicspath{{Figures/}}\n'
        
    if(line.count('begin{document}')) : 
        line = ''
        line += '\\newcommand*{\\titleGM}{\\begingroup %\n'
        line += '\\hbox{ % Horizontal box\n'
        line += '\\hspace*{0.2\\textwidth} % Whitespace to the left of the title page\n'
        line += '\\rule{1pt}{\\textheight}\n'
        line += '\\hspace*{0.05\\textwidth} % Whitespace between the vertical line and title page text\n'
        line += '\\parbox[b]{0.75\\textwidth}{'
        line += '{\\noindent\\Huge\\bfseries Data Analyse en Statistiek}\n'
        line += '{\\Large \\textsc{Hella Snoek \\& Marthe Schut}}\n'
        line += '\\vspace{0.2\\textheight}}}\\endgroup}\n'
        line += '\\begin{document}\n'
        line += '\\titleGM\n'
        line += '\\tableofcontents\\newpage\n'


    line = line.replace( r"\begin{quote}", r"\begin{example}" )
    line = line.replace( r"\end{quote}", r"\end{example}" )
    line = line.replace( r"\[", r"$" )
    line = line.replace( r"\]", r"$" )
    line = line.replace( r"♥" , r"$\heartsuit$")
    line = line.replace( r"♠" , r"$\spadesuit$")
    line = line.replace( r"♦" , r"$\diamondsuit$")
    line = line.replace( r"♣" , r"$\clubsuit$")

    if (line.startswith('\\newline')) : line = ""
    
    if (line.count('.png}')) :
        temp_line = '\\begin{figure}[h!]\n\\centering\n'
        w = '1.0'
        if (line.count('\%'))  :
            width = line[line.find('=')+3:line.find('%')-1]
            if (width == '100') : w='1.0'
            if (width == '60') : w='0.6'
            if (width == '45') : w='0.5'
            if (width == '40') : w='0.5'
            if (width == '30') : w='0.5'
            if (width == '80') : w='0.8'
        if (line.count('0px'))  :
            width = line[line.find('=')+3:line.find('px')]
            if (width == '400') : w='0.45'
        temp_line += line[0:line.find('{')]+'[width='+w+'\\textwidth]'+line[line.find('{'):line.find('}')+1]
        temp_line += '\n\\end{figure}'
        line = temp_line

    l = line
    print(l)

