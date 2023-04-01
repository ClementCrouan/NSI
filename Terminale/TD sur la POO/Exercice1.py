# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:12:19 2022

@author: ccrouan
"""
from math import sqrt

class Carre():
    def __init__(self, c):
        self.cote = c
    def perimetre(self):
        return 4 * self.cote
    def aire(self):
        return self.cote ** 2
        
class Triangle():
    def __init__(self, c1, c2, c3):
        self.cote1 = c1
        self.cote2 = c2
        self.cote3 = c3
    def perimetre(self):
        return ((self.cote1 + self.cote2 + self.cote3)/2)
    def aire(self):
        p = self.perimetre()
        a = sqrt(p * (p-self.cote1) * (p-self.cote2) * (p-self.cote3))
        return a
    def rect(self):
        h = max(self.cote1, self.cote2, self.cote3)
        if h == self.cote1:
            a = self.cote2
            o = self.cote3
        elif h == self.cote2:
            a = self.cote1
            o = self.cote3
        else:
            a = self.cote1
            o = self.cote2
        if h**2 == a**2 + o**2:
            return True
        else:
            return False


carre = Carre(5)
print(carre.perimetre())
print(carre.aire())
triangle = Triangle(5.4, 9, 7.2)
print(triangle.rect())
print(triangle.aire())
