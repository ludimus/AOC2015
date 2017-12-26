import sys


tot=0

for line in sys.stdin:
    line=line.rstrip();
    line=line[:-1]
    print line
    tot+=2;
    print "number of double slashes:",line.count("\\\\")
    tot+=line.count("\\\\")
    line=line.replace("\\\\","")
    print "number of slashes quotes:",line.count("\\\"")
    tot+=line.count("\\\"")
    line=line.replace("\\\"","")
    print "number of hex notations :",line.count("\\x")
    tot+=line.count("\\x")*3
    print "solution:",tot
print "solution:",tot
    
    
 