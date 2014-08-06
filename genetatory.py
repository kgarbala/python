# Krzysztof Garbala
# -*- coding: utf-8 -*-

# napisac co se robia generatory

def gen(x):
  for x in range(x,10):
    print x
    yield x
    
def gen1(x):
  for x in range(x,10):
    print x
  return x
    
z=1
gen(z)
print next(gen(z)),next(gen(z)) 
print '\n'*3    

print gen1(1)

print 2*'\n',"xxxxxxxxxx"
def frange(start, stop, inc):
  while start<stop:
    yield start
    start+=inc
  
for n in frange(0,10,1):
  print n
s1 = [n for n in frange(0,20,2)]
s2 = [n for n in frange(0,10, 1)]
print s1, s2, len(s1)==len(s2)
dic={n1: n2 for n1, n2 in zip(s1, s2)}
print dic




print "Urabura"
  