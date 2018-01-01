import sys

#f=2503
f=1000

for line in sys.stdin:
    parsed = line.split(' ')
    #print parsed
    name=parsed[0]
    speed=int(parsed[3])
    speed_time=int(parsed[6])
    rest_time=int(parsed[13])
    dest=0
    cycles=(f)/(speed_time +rest_time)
    dest+=(speed*speed_time*cycles)
    leftover=f%(speed_time+rest_time)
    if leftover<=speed_time:
        dest+=(speed*leftover)
    else:
        dest+=(speed*speed_time)
    print name, " traveled ", dest
