import sys


def get_dist(timeslot,speed, speed_time, rest_time):
    dest=0
    cycles=(timeslot)/(speed_time +rest_time)
    dest+=(speed*speed_time*cycles)
    leftover=timeslot%(speed_time+rest_time)
    if leftover<=speed_time:
        dest+=(speed*leftover)
    else:
        dest+=(speed*speed_time)
    return dest

N=[]
S=[]
ST=[]
RT=[]
i=0

for line in sys.stdin:
    parsed = line.split(' ')
    #print parsed
    N.append(parsed[0])
    S.append(int(parsed[3]))
    ST.append(int(parsed[6]))
    RT.append(int(parsed[13]))
    

T=[0,0,0,0,0,0,0,0,0]
cur=[0,0,0,0,0,0,0,0,0]

cycles=2503

for i in range(cycles):
    for j in range(len(N)):
        cur[j]=get_dist((i+1),S[j],ST[j],RT[j])
    for j in range(len(N)):
        if cur[j]==max(cur):
            T[j]+=1
    print cur
print T    


