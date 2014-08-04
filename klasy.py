# Krzysztof Garbala
# -*- coding: utf-8 -*-

class Zespolona:
  def __init__(self, rzeczywista, urojona):
    self.r = rzeczywista
    self.i = urojona
  def name(self):
    print "test"

x = Zespolona(3.0,-4.5)
print x.r, x.i
x.name()

class Pusta:
  def pisz(self):
      print "PUSTA!"
  pass
  

z = Pusta()
z.imie = "Krzysztof"
z.nazwisko = "Garbala"

print z.imie

class Lista(Pusta):
  def __init__(self, lista):
    self.lista = lista
    self.rob1 = [x for x in lista]
    self.rob2 = self.rob1.reverse()
    self.rob3 = "".join(self.rob1)
  def wyswietl(self):
    if self.lista=="Kazik Kryminal": 
      print "\n"*3, 'dziala'
    return self.rob1, self.rob3, self.lista
  def kodowanie(self):
    self.kod1 = [ord(x) for x in self.lista] 
    return self.kod1,
w=Lista("Krzysztof Garbala")
print w.wyswietl()

z=Lista("Kazik Kryminal")
print z.wyswietl()
print z.kodowanie()

print w.kodowanie()
print w.pisz()