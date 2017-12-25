import sys

H={}


def addhouse(x,y):
    key=str(x)+"_"+str(y)
    if key in H:
        H[key]+=1
    else:
        H[key]=1
        
xr=0
yr=0
xs=0
ys=0
numc=0;

for line in sys.stdin:
    print line
    addhouse(0,0)
    for c in line:
        if ((numc%2)==0):
            if(c=='>'):
                xs+=1;
            if(c=='<'):
                xs-=1;
            if(c=='^'):
                ys+=1;
            if(c=='v'):
                ys-=1;
            addhouse(xs,ys)
        else:
            if(c=='>'):
                xr+=1;
            if(c=='<'):
                xr-=1;
            if(c=='^'):
                yr+=1;
            if(c=='v'):
                yr-=1;
            addhouse(xr,yr)
        numc+=1
        
print len(H)