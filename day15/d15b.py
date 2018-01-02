import sys



N=[]
C=[]
D=[]
F=[]
T=[]
CA=[]


for line in sys.stdin:
    line = line.replace(",","")
    parsed = line.split(' ')
    #print parsed[2]
    C.append(int(parsed[2]))
    D.append(int(parsed[4]))
    F.append(int(parsed[6]))
    T.append(int(parsed[8]))
    CA.append(int(parsed[10]))

maxval=0
for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            if (i+j+k)<100:
                l=100-i-j-k
                cap=i*C[0]+j*C[1]+k*C[2]+l*C[3]
                if cap<0:
                    cap=0
                dur=i*D[0]+j*D[1]+k*D[2]+l*D[3]
                if dur<0:
                    dur=0
                fla=i*F[0]+j*F[1]+k*F[2]+l*F[3]
                if fla<0:
                    fla=0
                tex=i*T[0]+j*T[1]+k*T[2]+l*T[3]
                if tex<0:
                    tex=0
                cal=i*CA[0]+j*CA[1]+k*CA[2]+l*CA[3]
                cur=cap*dur*fla*tex
                if cal==500 and cur> maxval:
                    maxval=cur
print maxval        
        
    
    



