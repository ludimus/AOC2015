import itertools
L=[20,15,10,5,5]
L=[43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38]

solution=0
for i in range(1,5):
    for c in itertools.combinations(L,i):
        if sum(c)==150:
            solution+=1
print solution