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
        D.append(l[1])
        R.append(l[0])
    else:
        M=line.rstrip()
       
U.append(M)
print U

cycles=20

for i in range(cycles):
    N=[]
    for e in U:
        start=0
        for index in range (len(D)):
            f=e.find(D[index],start)
            while (f>-1):
                #print " found" +str(D[index]) +"in"+ e
                s1=e[:f]
                s2=e[f+len(D[index]):]
                key=s1+R[index]+s2
                #print "s1: "+s1 + "s2:" +s2 
                if key=='e':
                    print "Jackpot after: " + str(cycles) + " cycles"
                if key not in N:
                    N.append(key)
                start=f+1
                f=e.find(D[index],start)
            start=0
    
    U=N
    print "Size of catalog:" + str(len(U))
        
        
        


    
    