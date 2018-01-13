import sys


def get_element(r,c):
    col_start=((c+1)*c)/2
    element=col_start
    for i in range (2,r+1):
        element+=c
        c+=1
    return element
    
print get_element(5,6)

print get_element(3010,3019)

base=20151125
for i in range(get_element(3010,3019)-1):
    
    base=(base*252533)%33554393

print base
    

