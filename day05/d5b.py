import sys

def has_double_ss(l):
    ret=False
    for c in range(0,len(l)-4):
        ss=l[c]+l[c+1]
        if l.find(ss, c+2, len(l))>0:
            ret=True
    return ret

def has_skipchar(l):
    ret=False
    for n in range(0,len(l)-2):
        if l[n]==l[n+2]:
            ret=True
    return ret


n1=0

for line in sys.stdin:
    #print line
    #print has_double_ss(line)
    #print has_skipchar(line)
    #print on_blacklist(line)
    if has_double_ss(line) and has_skipchar(line):
        n1+=1;
    print n1;