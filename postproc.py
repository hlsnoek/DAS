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

        line += '\\setlength{\\textheight}{21.5cm}\\setlength{\\textwidth}{15.0cm}\n'
        line += '\\setlength{\\topmargin}{0.0cm}\n'
        line += '\\setlength{\\oddsidemargin}{0.0cm}\n'
        line += '\\setlength{\\evensidemargin}{0.0cm}\n'
        line += '\\renewcommand{\\appendixname}{}\n'
        line += '\\renewcommand{\\chaptername}{Module}\n'
        line += '\\renewcommand{\\contentsname}{Inhoud}\n'

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



    line = line.replace( r"\[", r"$" )
    line = line.replace( r"\]", r"$" )



    if(line.count("Ordered TOC")) :  line = ''
    line = line.replace( r"quote", r"example")
    l = line
    print(l)

