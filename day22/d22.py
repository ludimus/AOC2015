import random

Spells = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
Cost=[53,73,113,173,229]

Shield_T=0
Poison_T=0
Recharge_T=0

Hero_hitpoints=10
Hero_mana=250
Hero_armor=0
Hero_mana_spent=0

Boss_hitpoints=13
Boss_damage=8



def pick_spell():
    
    global Shield_T
    global Poison_T
    global Recharge_T
    
    global Boss_hitpoints
    global Hero_hitpoints
    global Hero_mana
    global Hero_mana_spent
    
    picked_spell=False
    
    #create list of possible spells
    S=[]
    if Cost[0]<=Hero_mana:
        S.append(0)
    if Cost[1]<=Hero_mana:
        S.append(1)
    if Cost[2]<=Hero_mana and Shield_T==0:
        S.append(2)
    if Cost[3]<=Hero_mana and Poison_T==0:
        S.append(3)
    if Cost[4]<=Hero_mana and Recharge_T==0:
        S.append(4) 
    
    if len(S)>0:    
        # randomly pick spell from S
        rspell=random.choice(S)
        print "Player casts "+Spells[rspell]+"("+str(Cost[rspell])+")."
        Hero_mana-=Cost[rspell]
        Hero_mana_spent+=Cost[rspell]
    
        if rspell==0:
            Boss_hitpoints-=4
            print "Player casts Magic Missile, dealing 4 damage."
        if rspell==1:
            Boss_hitpoints-=2
            Hero_hitpoints+=2
            print "Player casts drain dealing 2 damage, healing 2 hitpoints"
        if rspell==2:
            Shield_T=6
        if rspell==3:
            Poison_T=6
        if rspell==4:
            Recharge_T=5
        picked_spell=True
        
    return picked_spell

def Check_timers():
    global Shield_T
    global Poison_T
    global Recharge_T
    
    global Hero_armor
    global Boss_hitpoints
    global Hero_mana
    
    if Shield_T>0:
        Hero_armor=7
        Shield_T-=1
        print "Shields timer is now "+str(Shield_T)
        if Shield_T==0:
            print "Shield wears off, decreasing armor by 7."
            Hero_armor=0
    if Poison_T>0:
        Boss_hitpoints-=3
        Poison_T-=1
        print "Poison deals 3 damage; its timer is now "+str(Poison_T)
    if Recharge_T>0:
        Hero_mana+=101
        Recharge_T-=1
        print "Recharge provides 101 mana 3; its timer is now "+str(Recharge_T)
        
        
    


def print_report(who):
    print ""
    if (who%2)==0:
        print "-- Player turn --"
    else:
        print "-- Boss turn --"
    print "- Player has "+str(Hero_hitpoints)+" hit points, "+str(Hero_armor)+" armor, "+ str(Hero_mana)+" mana" 
    print "- Boss has "+str(Boss_hitpoints)+" hit points"


def play_game():
    
    winner=""
    global Hero_hitpoints
    turn=0
    while (Hero_hitpoints>0 and Boss_hitpoints>0):
        print_report(turn)
        if(turn%2==0):
            Hero_hitpoints-=1
            Check_timers()
            if (Hero_hitpoints>0 and Boss_hitpoints>0):
                if not pick_spell():
                    print "No more mana Boss wins"
                    Hero_hitpoints=0
        else:
            Check_timers()
            if (Hero_hitpoints>0 and Boss_hitpoints>0):
                print "Boss attacks for "+str(Boss_damage)+" damage"
                Hero_hitpoints-=max(Boss_damage-Hero_armor,0)
        turn+=1
    
    if (Hero_hitpoints>0):
        winner="Player"
    else:
        winner="Boss"
    return winner

#======================================================================
# Main loop
#======================================================================
least_mana=99999

for i in range (100000):
    
    Shield_T=0
    Poison_T=0
    Recharge_T=0

    Hero_hitpoints=50
    Hero_mana=500
    Hero_armor=0
    Hero_mana_spent=0

    Boss_hitpoints=58
    Boss_damage=9
    print "---------------Start new Game-----------------"    
    winner=play_game()
    print "----------------End of Game-------------------" + winner
    if "Player" in winner:
        print winner +" wins the game =========================================#" + str(Hero_mana_spent)
        if(Hero_mana_spent<least_mana):
            least_mana=Hero_mana_spent
    
print " End simulation,best result: "+str(least_mana)