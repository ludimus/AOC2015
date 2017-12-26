import sys


tot=0

for line in sys.stdin:
    line=line.rstrip();
    print line
    tot+=2;
    print "number slashes:",line.count("\\")
    tot+=line.count("\\")
    print "number of quotes:",line.count("\"")
    tot+=line.count("\"")
    print "solution:",tot
print "final solution:",tot
    
    
 