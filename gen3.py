#for x in range(10):
  #with open("duzy.bin", "ab") as f:
    #with open("test.txt", "r") as g:
	#for x in range(10000):
	    #f.write(g.read()+str(x))
	    #print x
	    
import time
# lista
f1=time.time()
with open("duzy.bin", "r") as f:
    while True:
        line=f.readline()
        if not line:
            break
        #print (line)
f2=time.time()-f1


#def foo():
 #with open("duzy.bin", "r") as f:
    #while True:
	#yield f.readline()
	##if not line:
	    ##break
	##print line
    #g2=time.time()-g1
    ##return g2
#print f2, "\nroznica", '\n'*10
                                                            
#for x in foo():
    #print x

    
g1=time.time()    
with open("duzy.bin", "r") as f:
    while True:
        line =next(f, None)
        if line is None:
            break
        #print (line, end='')
g2=time.time()-g1
print ('\n'*10,g2-f2)

def countdown(n):
  try:
    while n>0:
        yield n
        n-=1
    print ('gotowe')
  except StopIteration:
    pass
    #print ("po mojemu")
        
n=5
s=countdown(n)
print (next(s))
print (next(s))
print (next(s))
print (next(s))
print (next(s))
print (next(s))

sequence=[3,4]
it = iter(sequence)
while True:
    try:
        value = next(it) 
    except StopIteration:
        print ('dupa')
        break
    print(value)
