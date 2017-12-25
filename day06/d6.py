import sys

table= [ [ 0 for i in range(1000) ] for j in range(1000) ]    


def turn_on(l):
    c1,c2,c3,c4,c5=l.split(' ')
    x1,y1=c3.split(',')
    x2,y2=c5.split(',')
#   print (int(x1),int(y1),int(x2),int(y2))
    for x in range(int(x1),int(x2)+1):
        for y in range (int(y1),int(y2)+1):
            table[x][y]=1

def turn_off(l):
    c1,c2,c3,c4,c5=l.split(' ')
    x1,y1=c3.split(',')
    x2,y2=c5.split(',')
#   print (int(x1),int(y1),int(x2),int(y2))
    for x in range(int(x1),int(x2)+1):
        for y in range (int(y1),int(y2)+1):
            table[x][y]=0

def toggle(l):
    c1,c2,c3,c4=l.split(' ')
    x1,y1=c2.split(',')
    x2,y2=c4.split(',')
#   print (int(x1),int(y1),int(x2),int(y2))
    for x in range(int(x1),int(x2)+1):
        for y in range (int(y1),int(y2)+1):
            if table[x][y]==0:
                table[x][y]=1
            else:
                table[x][y]=0
                
for a in range(0,10):
    print a

for line in sys.stdin:
#    print line
    
    if "turn on" in line:
        turn_on(line)
    if "turn off" in line:
        turn_off(line)
    if "toggle" in line:
        toggle(line)    

ons=0
for x in range(0,1000):
    for y in range(0,1000):
        if table[x][y]==1:
            ons+=1
print ons            