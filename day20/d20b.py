import sys

nhouses=800000
nelves=nhouses

houses = [0 for x in range(nhouses+1)]

for i in range(1,nelves):
    j=i
    p=0
    while j <nhouses and p<50:
        houses[j]+=i*11
        if houses[j]>=29000000:
            print "Solution: " + str(j)
        j=j+i
        p+=1

print max(houses)
