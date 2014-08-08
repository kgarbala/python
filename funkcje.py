# Krzysztof Garbala
# -*- coding: utf-8 -*-
# python3


def wyswietl(*arg):
	print (arg)
	print (arg[3])
	print (sum(arg))


def wyswietl(a,*kwarg):
	print (a,kwarg)
	print (kwarg[3])
	print (sum(kwarg))

	
def recv(maxsize, *, block):
	'Przyjmuje komunikat'
	pass

recv(1024, block=True)
	
f = wyswietl(3,4,5,19, 20)


def minimum(*values, clip=None):
	z=max(values)
	m= min(values)
	if clip is not None:
		print (clip, 'aasda')
		m= clip if clip > m else m
	return m, z


print (minimum(12, 23, -9, 23,43534, 213,-1, clip=-12))
print ("Sprawdznie")
