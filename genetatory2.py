def info():
	yield "Co"
	yield "to"
	yield "jest"
	yield "?"
	
print " ".join(info()), next(info()), next(info())
print "Urabura"
print "Urabura"
g=lambda x, y: x+y*2
print g(8, 1),
z=lambda x, y: x+y

print z(2,4)
mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
mult4 = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 3 == 0]
print mult3, mult4, sum(range(8,10))

print [x for x in range(10)]
