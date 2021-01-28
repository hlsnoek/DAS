#!/bin/sh
mdmerge -o DASBoek.md --leanpub book.txt
python preproc.py DASBoek.md > DASBoek.proc.md
pandoc DASBoek.proc.md -f markdown+pipe_tables  -t latex --top-level-division=chapter --number-sections --listings -H listings.tex -s -o DASBoek.post.latex
python postproc.py DASBoek.post.latex > DASBoek.latex
pdflatex DASBoek.latex
open DASBoek.pdf
