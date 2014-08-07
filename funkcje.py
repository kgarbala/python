

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
	m= min(values)
	if clip is not None:
		print (clip, 'aasda')
		m= clip if clip > m else m
	return m


print (minimum(12, 23, -9, 23,43534, 213,-1))