#!/bin/sh

# Merge all md files listed in book.txt
mdmerge -o DASBoek.md --leanpub book.txt

# Make soft links to figures for Latex use later
python createFigureLinks.py

# Preproces the md file.
python preproc.py DASBoek.md > DASBoek.proc.md

# Create the latex file
pandoc DASBoek.proc.md -f markdown+pipe_tables  -t latex --top-level-division=chapter --number-sections --listings -H listings.tex -s  --wrap=none  -o DASBoek.post.latex

#fixing linewraps
python midproc.py DASBoek.post.latex > DASBoek.p.latex

# Adding packages, figures search dir, title page, contents and post process formulas
python postproc.py DASBoek.p.latex > DASBoek.latex

# Finally create the pdf
pdflatex DASBoek.latex
pdflatex DASBoek.latex
open DASBoek.pdf
