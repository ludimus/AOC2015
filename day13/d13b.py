import sys
import itertools

T ={}
N=['Alice','Bob','Carol','David','Eric','Frank','George','Mallory','Ludimus']
persons=9

for line in sys.stdin:
    line=line.rstrip()
    line=line.rstrip('.')
    L=line.split(' ')
    key=L[0] + L[10]
    if "gain" in L[2]:
        T[key]=int(L[3])
    else:
        T[key]=-1*int(L[3])

for i in range(8):
    key=N[i]+N[8]
    key2=N[8]+N[i]
    T[key]=0
    T[key2]=0
    


    

P=list(itertools.permutations([0, 1, 2,3,4,5,6,7,8]))
print "Number of permutations:", len(P)

maxval=0
for seating in P:
    current=0
    for seat in range(persons):
        key=N[seating[seat]]+N[seating[(seat+1)%persons]]
        current+=T[key]
        key2=N[seating[(seat+1)%persons]]+N[seating[seat]]
        current+=T[key2]
        #print key,T[key],key2,T[key2]
    #print seating, current    
    if current>maxval:
        maxval=current
print "Maximum happiness: ", maxval
        