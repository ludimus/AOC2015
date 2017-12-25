import md5

'''
vb="abcdef"
sv=609043
vbs=vb+str(sv)
print vbs
mv = md5.new()
mv.update(vbs)
print mv.hexdigest()
'''


secret="bgvyzdsv"

for sol in range(0,10000000):
    vbs=secret+str(sol)
    m = md5.new()
    m.update(vbs)
    H=m.hexdigest()
        
    #print hash[0]
    if H[0]=='0' and H[1]=='0' and H[2]=='0' and H[3]=='0' and H[4]=='0' and H[5]=='0':
        print sol
        print H