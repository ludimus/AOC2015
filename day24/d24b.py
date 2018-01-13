import sys
import random

P=[]
opt=4

r1=4
r2=20

for line in sys.stdin:
    P.append(int(line))
print P

tot=0
lowest=999999999999

for e in P:
    tot+=e
fourth=tot/4

print "total: "+str(tot)
print "fourth: "+str(fourth)

for i in range(10000000):
    random.shuffle(P)
    for j in range(r1,r2):
        if sum(P[0:j])==fourth:
            for k in range(r1,r2):
                if sum(P[j:j+k])==fourth:
                    for l in range(r1,r2):
                        if sum(P[j+k:j+k+l])==fourth:
                            len1= len(P[0:j])
                            len2= len(P[j:j+k])
                            len3= len(P[j+k:j+k+l])
                            len4= len(P[j+k+l:])
                            
                            if(len1 == opt):
                                qe=1
                                for e in P[0:j]:
                                    qe*=e
                                print qe, P[0:j]
                                if lowest>qe:
                                    lowest=qe
                            
                            if(len2 == opt):
                                qe=1
                                for e in P[j:j+k]:
                                    qe*=e
                                print qe, P[j:j+k]
                                if lowest>qe:
                                    lowest=qe
                    
                            if(len3 == opt):
                                qe=1
                                for e in P[j+k:j+k+l]:
                                    qe*=e
                                print qe, P[j+k:j+k+l]
                                if lowest>qe:
                                    lowest=qe
                            
                            if(len4 == opt):
                                qe=1
                                for e in P[j+k+l:]:
                                    qe*=e
                                print qe, P[j+k+l:]
                                if lowest>qe:
                                    lowest=qe        
                                    
print lowest
                        
            
