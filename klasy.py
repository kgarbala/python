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

class pusta:
  pass

z = pusta()
z.imie = "Krzysztof"
z.nazwisko = "Garbala"

print z.imie