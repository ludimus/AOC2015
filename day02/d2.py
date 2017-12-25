import sys


def wrap(l,w,h):
    return((l*w*2) + (w*h*2) + (l*h*2))

def extra_wrap(l,w,h):
    nlist=[0,0,0]
    nlist[0]=l
    nlist[1]=w
    nlist[2]=h       
    nlist.sort()
    return(nlist[0]*nlist[1])       


           
numline=0
totwrap=0

for line in sys.stdin:
    l,w,h=line.split('x')
    totwrap+=wrap(int(l),int(w),int(h))
    totwrap+=extra_wrap(int(l),int(w),int(h))

           
print totwrap
