import sys

size=100
lines_read=0

M={}
N={}

def print_matrix():
    for v in range(size):
        l=""
        for h in range(size):
            key=str(v)+"_"+str(h)
            l+=M[key]
        print l

def get_neighbors(v,h):
    ret =0;
    if (v-1)>=0 and (h-1)>=0 and M[str(v-1)+"_"+str(h-1)]=="#":
        ret+=1
    if (v-1)>=0 and M[str(v-1)+"_"+str(h)]=="#":
        ret+=1
    if (v-1)>=0 and (h+1)<size and M[str(v-1)+"_"+str(h+1)]=="#":
        ret+=1
    if (h-1)>=0 and M[str(v)+"_"+str(h-1)]=="#":
        ret+=1
    if (h+1)<size and M[str(v)+"_"+str(h+1)]=="#":
        ret+=1
    if (v+1)<size and (h-1)>=0 and M[str(v+1)+"_"+str(h-1)]=="#":
        ret+=1
    if (v+1)<size and M[str(v+1)+"_"+str(h)]=="#":
        ret+=1
    if (v+1)<size and (h+1)<size and M[str(v+1)+"_"+str(h+1)]=="#":
        ret+=1
    return ret



for line in sys.stdin:
    if lines_read<size:
        L=list(line.rstrip())
        h=0
        for e in L:
            key=str(lines_read)+"_"+str(h)
            M[key]=e
            h+=1
        lines_read+=1

M["0_0"]="#"
M["0_99"]="#"
M["99_0"]="#"
M["99_99"]="#"


cycles=100

for c in range(cycles):
    for v in range(size):
        for h in range(size):
            numon=get_neighbors(v,h)
            key=str(v)+"_"+str(h)
            if (numon<2) and M[key]=="#":
                N[key]="."
            if (numon>3) and M[key]=="#":
                N[key]="."
            if (numon==2) and M[key]=="#":
                N[key]="#"
            if (numon==3) and M[key]=="#":
                N[key]="#"
            if (numon==3) and M[key]==".":
                N[key]="#"
            if (numon<>3) and M[key]==".":
                N[key]="." 
    
    for v in range(size):
        for h in range(size):
            key=str(v)+"_"+str(h)
            M[key]=N[key]
    
    M["0_0"]="#"
    M["0_99"]="#"
    M["99_0"]="#"
    M["99_99"]="#"

    #print "------------------------------"
    #print_matrix()

total=0
for v in range(size):
    for h in range(size):
        key=str(v)+"_"+str(h)
        if M[key]=="#":
            total+=1
print total            