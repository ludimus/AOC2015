import sys
import random

P=[]

r1=5
r2=20

for line in sys.stdin:
    P.append(int(line))
print P

tot=0
lowest=999999999999

for e in P:
    tot+=e
third=tot/3

print "total: "+str(tot)
print "third: "+str(third)

for i in range(10000000):
    random.shuffle(P)
    for j in range(r1,r2):
        if sum(P[0:j])==third:
            for k in range(r1,r2):
                if sum(P[j:j+k])==third:
                    
                    
                    len1= len(P[0:j])
                    len2= len(P[j:j+k])
                    len3= len(P[j+k:])
                    if(len1 == 6):
                        qe=1
                        for e in P[0:j]:
                            qe*=e
                        print qe, P[0:j]
                        if lowest>qe:
                            lowest=qe
                    if(len2 == 6):
                        qe=1
                        for e in P[j:j+k]:
                            qe*=e
                        print qe, P[j:j+k]
                        if lowest>qe:
                            lowest=qe
                    if(len3 == 6):
                        qe=1
                        for e in P[j+k:]:
                            qe*=e
                        print qe, P[j+k:]
                        if lowest>qe:
                            lowest=qe
print lowest
                        
            
