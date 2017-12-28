# Hello World program in Python
   
A = list("abcdefghijklmnopqrstuvwxyz")
 
 
pw=list("cqjxjnds")
pw=list("cqjxxyzz")
 
def rotate(c):
    i= A.index(pw[c])
    i = (i+1 )%26
    pw[c]=A[i]
    if i==0 and c>0:
        rotate(c-1)
 
def check_iol():
    ret=True
    if ret and 'i' in pw:
        ret=False
    if ret and 'o'in pw:
        ret=False
    if ret and 'l' in pw:
        ret=False
   
    return ret
 
def check_abc():
    ret=False
    s=0
    e=3
    pws=''.join(pw[0:8])
    for i in range(24):
        abc=''.join(A[s:e])
        #print abc
        if ret==False and abc in pws:
            ret=True
        s+=1
        e+=1
    #print ret
    return ret
       
def check_doubles():
    numfind=0
    ret=False
    pws=''.join(pw[0:8])
    for i in range(26):
        double=A[i]+A[i]
        #print double
        if numfind<2 and double in pws:
            numfind+=1
            
    if numfind>1:
        ret=True
    return ret    
    
 
       
pwok=False
while(pwok==False):
    pwok=True
    rotate(7)
    if(pwok):
        pwok=check_iol()
    if(pwok):
        pwok=check_abc()
    if(pwok):
        pwok=check_doubles()
print pw