import sys

I=[]
P=0
rega=1
regb=0

for line in sys.stdin:
    I.append(line.rstrip())
print I

while P<len(I):
    if "hlf" in I[P]:
        instr=I[P].split(' ')
        if instr[1]=="a":
            rega/=2
        else:
            regb/=1
    
    if "tpl" in I[P]:
        instr=I[P].split(' ')
        if instr[1]=="a":
            rega*=3
        else:
            regb*=3
    
    if "inc" in I[P]:
        instr=I[P].split(' ')
        if instr[1]=="a":
            rega+=1
        else:
            regb+=1
    
    if "jmp" in I[P]:
        instr=I[P].split(' ')
        P+=int(instr[1])-1
        
    if "jie" in I[P]:
        instr=I[P].split(' ')
        if "a" in instr[1]:
            if rega%2==0:
                P+=int(instr[2])-1
        else:
            if regb%2==0:
                P+=int(instr[2])-1

    if "jio" in I[P]:
        instr=I[P].split(' ')
        if "a" in instr[1]:
            if rega==1:
                P+=int(instr[2])-1
        else:
            if regb==1:
                P+=int(instr[2])-1
    
    P+=1

print "Register value A: "+str(rega)
print "Register value B: "+str(regb)


        
        
    
    