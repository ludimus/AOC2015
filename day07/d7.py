import sys
import time


C={}

def compute(wire):
    
    #time.sleep(1)
    if wire.isdigit():
        ret=int(wire)
    else:
        expr=C.get(wire,"0")
        print "Computing wire:", wire
        
        if expr.isdigit():
            ret=int(expr)
        else:
            exprl=expr.split(' ')
            nexpr=len(exprl)
            print "number arguments in expr:" ,expr,":", nexpr
        
            if nexpr==1:
                ret=compute(expr)
            
            if "NOT" in expr:
                n,v=expr.split(" ")
                ret = ~compute(v) & 0xffff
        
            if "OR" in expr:
                n1,v,n2 =expr.split(" ")
                ret = (compute(n1) | compute(n2) )& 0xffff
            
            if "AND" in expr:
                n1,v,n2 =expr.split(" ")
                ret = (compute(n1) & compute(n2) )& 0xffff
                
            if "LSHIFT" in expr:
                n1,v,n2 =expr.split(" ")
                ret = (compute(n1) << compute(n2) )& 0xffff
            
            if "RSHIFT" in expr:
                n1,v,n2 =expr.split(" ")
                ret = (compute(n1) >> compute(n2) )& 0xffff
        
        C[wire]=str(ret)        
    return ret
    


for line in sys.stdin:
    line=line.rstrip()
    expr, wire = line.split('->')
    wire=wire.lstrip()
    expr=expr.lstrip()
    expr=expr.rstrip()
    C[wire.lstrip()]=expr
#print C
print compute('a')
'''
    print "----------------x--------------"
    print compute('x')
    print "----------------y--------------"
    print compute('y')
    print "----------------i--------------"
    print compute('i')
    print "----------------h--------------"
    print compute('h')
    print "----------------j--------------"
    print compute('j')
    print "----------------e--------------"
    print compute('e')
    print "----------------d--------------"
    print compute('d')
    print "----------------f--------------"
    print compute('f')
    print "----------------g--------------"
    print compute('g')
'''