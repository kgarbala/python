# Krzysztof Garbala
# -*- coding: utf-8 -*-
lista1=[x for x in range(5)]
lista2=[x*3 for x in range(5)]
print (len(lista1))
print (ord('a'))
slownik1={chr(97+x): x**3 for x in range(5)}
slownik2={chr(97+x)+chr(98+x): [x**3,x*2] for x in range(5)}
print (slownik1, slownik2, "slownik2['cd']",slownik2['cd'])
print (slownik1['a'], 'str',str(slownik1))
slownik1.clear()
print (slownik1, type(slownik1))
slownik3=slownik2.copy()

slownik3['nowa_wartosc'], slownik3['NOWA_WARTOSC']=50, 999
print (slownik3, len(slownik3))
del slownik3['de']
print (slownik3, len(slownik3), '\n'*3)
lis=[]
for key in slownik3:
  lis.append(key), 
  lis.append(slownik3[key])
  print (lis)
print (lis[2])

print (slownik3.keys())          # [klucze]

print (3*'\n',slownik3.items())   #[(klucz),(wartosc)]

print (3*'\n',slownik3.values())  # [wartosc] 
  
  
import collections
kolejka1=collections.deque(maxlen=3)
kolejka1.append("jeden")
kolejka1.append("dwa")
kolejka1.append("trzy")
kolejka1.append("zero")
print (kolejka1)