#!/usr/bin/python
import sys
f = open( sys.argv[1] )


inExEnv = False

for line in f:
    line  = line[:-1] # trailing newline removal
    line = line.replace("{part}{I\\hspace {1em}}","{part}{MODULE I\\hspace {1em}}")
    line = line.replace("{part}{II\\hspace {1em}}","{part}{MODULE II\\hspace {1em}}")
    line = line.replace("{part}{III\\hspace {1em}}","{part}{MODULE III\\hspace {1em}}")
    line = line.replace("{part}{IV\\hspace {1em}}","{part}{MODULE IV\\hspace {1em}}")
    if (line.count('{Appendices}')) : line = '' 
    l = line
    print(l)
