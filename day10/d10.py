task = "3113322113"
 
 
for i in range(50):
    p=0
    newtask=""
    while p<len(task):
        count=0
        while(((p+count)<len(task)) and task[p+count]==task[p]):
            count+=1
        newtask+=str(count)+task[p]
        p+=count
    print len(newtask) 
    task=newtask 