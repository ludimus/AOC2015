import sys
D=[]
R=[]
L=[]
S=""

for line in sys.stdin:
    #print line
    if "=>" in line:
        line=line.rstrip()
        l=line.split(" => ")
        R.append(l[0])
        D.append(l[1])
        L.append(len(l[1]))
    else:
        S=line.rstrip()
       

print(R)
print(D)
print(L)
print(S)


# strategy replacing back the longest matches, input table sorted on len
for i in range(1000):
    replaced=False
    for index in range (len(D)):
        if not replaced:
            f=S.find(D[index],0)
            if (f>-1):
                print ("\nfound " +str(D[index]) +" in "+ S)
                s1=S[:f]
                s2=S[f+len(D[index]):]
                S=s1+R[index]+s2
                print("newstring :" + S + " in " + str(i+1) + " steps")
                replaced=True
            
                           
    
        
        


    
    