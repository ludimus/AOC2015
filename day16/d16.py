import sys

tape=""
tape +="children: 3"
tape +="cats: 7"
tape +="samoyeds: 2"
tape +="pomeranians: 3"
tape +="akitas: 0"
tape +="vizslas: 0"
tape +="goldfish: 5"
tape +="trees: 3"
tape +="cars: 2"
tape +="perfumes: 1"

print tape

for line in sys.stdin:
    line = line.replace(",","")
    line = line.rstrip()
    parsed = line.split(' ')
    #print parsed
    item1=parsed[2]+" " + parsed[3]
    item2=parsed[4]+" " + parsed[5]
    item3=parsed[6]+" " + parsed[7]
    #print item1, item2, item3
    if (item1 in tape) and (item2 in tape) and (item3 in tape):
        print parsed[0], parsed[1]
    
    

    
    



