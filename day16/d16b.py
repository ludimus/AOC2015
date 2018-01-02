import sys

tape={}
tape["children:"]= 3
tape["cats:"]= 7
tape["samoyeds:"]= 2
tape["pomeranians:"]= 3
tape["akitas:"]= 0
tape["vizslas:"]= 0
tape["goldfish:"]= 5
tape["trees:"]= 3
tape["cars:"]= 2
tape["perfumes:"]= 1

print tape


def check_item(item,nitems):
    ret=False
    #print item, nitems, tape[item]
    if "children" in item and nitems==tape[item]:
        ret=True
    if "samoyeds" in item and nitems==tape[item]:
        ret=True
    if "akitas" in item and nitems==tape[item]:
        ret=True
    if "vizslas" in item and nitems==tape[item]:
        ret=True
    if "cars" in item and nitems==tape[item]:
        ret=True
    if "perfumes" in item and nitems==tape[item]:
        ret=True
        
    if "cats" in item and nitems>tape[item]:
        ret=True
    if "trees" in item and nitems>tape[item]:
        ret=True
        
    if "goldfish" in item and nitems<tape[item]:
        ret=True
    if "pomeranians" in item and nitems<tape[item]:
        ret=True
        
    
    return ret



for line in sys.stdin:
    line = line.replace(",","")
    line = line.rstrip()
    parsed = line.split(' ')
    #print parsed
    item1=parsed[2]
    nitem1=int(parsed[3])
    item2=parsed[4]
    nitem2=int(parsed[5])
    item3=parsed[6]
    nitem3=int(parsed[7])

    if (check_item(item1,nitem1) and check_item(item2,nitem2) and check_item(item3,nitem3) ):
        print parsed
    
    

    
    



