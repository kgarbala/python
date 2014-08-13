l=[x for x in range(3)]*3
print l
r=set(l)
print r
d=[]
for x in l:
    if x not in d:
        d.append(x)

print d

def mnoz(x):
    return x*2
print map(mnoz, [1,2,3,4])