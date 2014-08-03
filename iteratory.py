# Krzysztof Garbala
# -*- coding: utf-8 -*-

def iterator(start, stop, inc):
  while start<stop:
    start+=inc
    print start
  return start
z=iterator(1,10,0.25)