import sys
import re


regex = "-?\d+"

for line in sys.stdin:
    #print line
    L=re.findall(regex,line)
    #print L
tot=0
for i in L:
    tot+=int(i)
print tot
