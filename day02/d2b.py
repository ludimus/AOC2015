import sys


def ribbon(l,w,h):
    nlist=[0,0,0]
    nlist[0]=l
    nlist[1]=w
    nlist[2]=h       
    nlist.sort()
    return(2*nlist[0]+2*nlist[1]+l*w*h)       


           
numline=0
totribbon=0

for line in sys.stdin:
    l,w,h=line.split('x')
    totribbon+=ribbon(int(l),int(w),int(h))
    
           
print totribbon
