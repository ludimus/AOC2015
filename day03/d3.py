import sys

H={}


def addhouse(x,y):
    key=str(x)+"_"+str(y)
    if key in H:
        H[key]+=1
    else:
        H[key]=1
        
x=0
y=0

for line in sys.stdin:
    print line
    addhouse(x,y)
    for c in line:
        if(c=='>'):
            x+=1;
        if(c=='<'):
            x-=1;
        if(c=='^'):
            y+=1;
        if(c=='v'):
            y-=1;
        addhouse(x,y)
        
print H
print len(H)