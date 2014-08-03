# krotki, zbiory (sets)
slowo1="Krzysztof Garbala"
lista1=list(slowo1)
print lista1

krotka1=[x for x in slowo1]
krotka1=tuple(krotka1)  # tworzenie krotki z listy
l=[x for x in krotka1]
print "Krotka1",krotka1, 'l:',l

empty={x for x in range(10)}
sin='hello',

print sin, empty
for x in (1, 2, 3): print x

zbior1=set(krotka1)
print zbior1

unique=[x for x in zbior1]
unique[2]=22
print sorted(unique), '\n'*3, unique[2]
print sorted(krotka1), type(krotka1)
zbior1.add(30)
print zbior1