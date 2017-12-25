import sys

def count_vowels(l):
    nv=0;
    for c in l:
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            nv+=1
    return nv

def has_doublechar(l):
    ret=False
    for n in range(0,len(l)-1):
        if l[n]==l[n+1]:
            ret=True
    return ret

def on_blacklist(l):
    ret=False
    
    if "ab" in l:
        ret=True
    if "cd" in l:
        ret=True
    if "pq" in l:
        ret=True
    if "xy" in l:
        ret=True
    return ret    
    

n1=0

for line in sys.stdin:
    #print line
    #print count_vowels(line)
    #print has_doublechar(line)
    #print on_blacklist(line)
    if count_vowels(line)>2 and has_doublechar(line) and not on_blacklist(line):
        n1+=1;
    print n1;