# Krzysztof Garbala
# -*- coding: utf-8 -*-


class Zespolona:
    # czy tu sie komentuje
    def __init__(self, rzeczywista, urojona):
        self.r = rzeczywista
        self.i = urojona
    def name(self):
        print "test"

zesp = Zespolona(3.0, -4.5)
print zesp.r, zesp.i
zesp.name()

class Pusta:
    def pisz(self):
        print "PUSTA!"
    pass

struktura = Pusta()
struktura.imie = "Krzysztof"
struktura.nazwisko = " Garbala"
print "Klasa Pusta", len(struktura.imie), type(struktura.imie), struktura.imie + struktura.nazwisko

class Lista(Pusta):
    def __init__(self, lista):
        self.lista = lista
        self.rob1 = [x for x in lista]
        self.rob2 = self.rob1.reverse()
        self.rob3 = "".join(self.rob1)
    def wyswietl(self):
        if self.lista == "Kazik Kryminal":
            print "\n"*3, 'dziala'
        return self.rob1, self.rob3, self.lista
    def kodowanie(self):
        self.kod1 = [ord(x) for x in self.lista]
        return self.kod1

w = Lista("Krzysztof Garbala")
print w.wyswietl()
z = Lista("Kazik Kryminal")
print z.wyswietl()
print z.kodowanie()
print w.kodowanie()
print w.pisz()
print "\n"*3

class test:
	ww="test"
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def zwroc(self):
	    return self.x +self.y
	def podziel(self, z):
		return self.x + self.y * z
	def lista(self, lista1):
		return lista1.split(" ")
	def pierwiastek(self, liczba):
		from math import sqrt
		return sqrt(liczba)
		
ss=test(4, 4)
print ss.zwroc(), ss.ww, type(ss.ww)
print ss.podziel(2)
zz=test(1,1)
print zz.podziel(1)
h=zz.lista("akjsdhakjsdh ajsdhajs ajshds dd")
print zz.lista("urabure dfkjhjds dkfj"), h
print zz.pierwiastek(10)
print zz.zwroc()
import visual