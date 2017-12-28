import sys
import random


N={}
nn=8
curin=nn-1
curnode=-1
nextnode=curnode+1;
while (curin>0):
    curnode+=1
    nextnode=curnode+1
    for l in range(curin):
        line = sys.stdin.readline()
        a1,a2,a3,a4,a5=line.split(' ')
        key=str(curnode) + '_'+str(nextnode)
        N[key]=int(a5)
        key=str(nextnode) + '_'+str(curnode)
        N[key]=int(a5)
        nextnode+=1
    curin-=1    
print N

#generate random routes
longest=0
for r in range(1000000):
    route = [x for x in range(nn)]
    random.shuffle(route)
    curroute=0
    for n in range(nn-1):
        key=str(route[n])+'_'+str(route[n+1])
        curroute+=int(N.get(key))
    #print route, curroute
    if curroute>longest:
        longest=curroute
        print route, curroute

print "solution:", longest
        