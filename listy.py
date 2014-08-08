### -*- coding: utf-8 -*-
slowo1= "Krzysztof Garbala"
slowo2="urabura,urabura,kys,kazio;kryminal            df"
print "slowo1", slowo1
print "slowo2", slowo2
# string na liste:
lista=list(slowo1)
print "lista: "; print  lista
lista.reverse()
print "lista odwrocona: "; print lista
lista2="".join(lista)
print "slowo odwrocone: "; print lista2

import re
# slowo rozdzielone:
_lista1=re.split(r"[;,\s]\s*", slowo2)
print "slowo rozdzielone", _lista1

_lista2=",".join(_lista1)
print _lista2
# znaki w ASCI:

# for letter in range(ord('a'), ord('{')):
	# print chr(letter)
print '''
                          ALFABET 
'''
lis1=[chr(x) for x in range(ord('a'), ord('{'))]
print 2*'\n',"lis1: ",lis1

print  "alfabet", ''.join(lis1)
print sorted(''.join(lis1))
lis1.reverse()
lis1.sort(reverse=True)
print lis1

print '''     
                           RANDOM                 '''

#from random import randint
#from random import *
import time as Ty
import random
import time
jedna=random.randint(0, 6)
print jedna
jedna2=random.randrange(0,6)
print jedna2
jedna_lis=random.choice(lis1)
print jedna_lis
random.shuffle(lis1)
print lis1

for i in range(1,11):
 k=1
 print i,":\r\r"
 while True:
	znak=random.choice(lis1)
	if znak=="a":
		print "znaleziono k=", k
		
		break
	elif k>=10:
		print "przekroczono k=", k
		break
	k+=1
	
print '$$$$$$$$$$$$$'

w="Urabura grzyb ść"
w1=list(w)
k=0
for i in w1:
  if i=="ś":
    w1.pop(k)
  k+=1
print w1 
print "".join(w1)

print Ty.time()

def test(lista):
  k=0
  for l in lista:
    k+=1
    print l+ str(k)

map(test, lista2)



print ("========------========")
S=[[x for x in range(1,4)]*3]*3
print S, len(S), len(S[0])
i=0
s1,s2,s3=S
print s1,"s2=",s2,s3
k=[]
for x in S:
	
	for z in x:
		
		print z,
		i+=1
		s("%d") %(i)
		
		
	
