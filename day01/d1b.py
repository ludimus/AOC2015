import sys

floor=0
numchar=1

for line in sys.stdin:
    #print line
    for c in line:
        if(c=='('):
            floor+=1
        if(c==')'):
            floor-=1
        if(floor==-1):
            print(numchar)
        numchar+=1    
