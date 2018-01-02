import sys
D=[]
R=[]
U=[]
S=""

for line in sys.stdin:
    #print line
    if "=>" in line:
        line=line.rstrip()
        l=line.split(" => ")
        D.append(l[0])
        R.append(l[1])
    else:
        S=line.rstrip()

start=0
for index in range (len(D)):
    f=S.find(D[index],start)
    while (f>-1):
        s1=S[:f]
        s2=S[f+len(D[index]):]
        key=s1+R[index]+s2
        if key not in U:
            U.append(key)
        start=f+1
        f=S.find(D[index],start)
    start=0
print len(U)
        
        
        


    
    