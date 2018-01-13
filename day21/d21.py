p_hp=8
p_dam=5
p_arm=5

b_hp=12
b_dam=7
b_arm=2

maxcycle=10000

def play_game(ph,pd,pa,bh,bd,ba):
    winner=""    
    for i in range(maxcycle):
        if (i%2==0):
            bh-=max(pd-ba,0)
            #print "Boss: ", bh
            if (bh<=0):
                winner="Player"
                break
        else:
            ph-=max(bd-pa,0)
            #print "Player: ", ph
            if (ph<=0):
                winner="Boss"
                break
    return winner

#print "Boss: ", b_hp
#print "Hero: ", p_hp
#teat game
#print play_game(p_hp,p_dam,p_arm,b_hp,b_dam,b_arm) + " wins!"                


#real game
WC=[8,10,25,40,74]
WD=[4,5,6,7,8]
AC=[0,13,31,53,75,102]
AA=[0,1,2,3,4,5]
RC=[0,0,25,50,100,20,40,80]
RD=[0,0,1,2,3,0,0,0]
RA=[0,0,0,0,0,1,2,3]

gold=1000
for r1 in range(len(RC)):
    for r2 in range(len(RC)):
        if(r1<>r2):
            for a in range(len(AC)):
                for w in range(len(WC)):
                    gold_spent=WC[w]+AC[a]+RC[r1]+RC[r2]
                    if "Player" in play_game(100,WD[w]+RD[r1]+RD[r2],AA[a]+RA[r1]+RA[r2],100,8,2):
                        if gold_spent<gold:
                            gold=gold_spent
                            print gold_spent, str(w),str(a),str(r1),str(r2)
                

