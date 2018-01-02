import sys

nhouses=700000
nelves=nhouses

houses = [0 for x in range(nhouses+1)]

for i in range(1,nelves):
    j=i
    while j <nhouses:
        houses[j]+=i*10
        if houses[j]>=29000000:
            print "Solution: " + str(j)
        j=j+i

print max(houses)
