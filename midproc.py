#!/usr/bin/python
import sys
f = open( sys.argv[1] )

for line in f:
    line  = line[:-1] # trailing newline removal
    l = ''
    temp_line = line
    while (temp_line.count('} ')) :
        l += temp_line[0:temp_line.find('} ')+1]+'\n'
        temp_line = temp_line[temp_line.find('} ')+2:]
    l += temp_line
    line = l
    l = ''
    temp_line = line
    while (temp_line.count('\\newline ')) :  
        l += temp_line[0:temp_line.find('newline ')+7]
        l += '\n'
        temp_line = temp_line[temp_line.find('newline ')+8:]
        
    l += temp_line
    line = l
        
    print(line)
