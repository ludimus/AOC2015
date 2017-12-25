import sys

floor=0

for line in sys.stdin:
    #print line
    for c in line:
        if(c=='('):
            floor+=1
        if(c==')'):
            floor-=1
print floor