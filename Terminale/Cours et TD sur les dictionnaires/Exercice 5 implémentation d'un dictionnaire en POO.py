# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:31:24 2023

@author: ccrouan
"""

class dict1:
    def __init__(self):
        self.Liste = []
        
    def ajouter(self, liste):
        self.Liste += [liste]
        
    def supprimer(self, key):
        for i in range(len(self.Liste)):
            if self.Liste[i][0] == key:
                del self.Liste[i]

    def modifier(self, key, newValue):
        for i in range(len(self.Liste)):
            if self.Liste[i][0] == key:
                self.Liste[i][1] = newValue
    
    def rechercher(self, key):
        for i in range(len(self.Liste)):
            if self.Liste[i][0] == key:
                return self.Liste[i][1]

    def syntaxe(self):
        l = "{"
        for i in range(len(self.Liste)):
            l += self.Liste[i][0] + " : " + self.Liste[i][1]
            if i != len(self.Liste)-1:
                l += ", "
        l += "}"
        return l

        
L = dict1()
L.ajouter(["cle1","val1"])
L.ajouter(["cle2","val2"])
print(L.syntaxe())
L.modifier("cle1","Vallmodif")
L.supprimer("cle2")
print(L.syntaxe())
print(L.rechercher("cle1"))
print(L.rechercher("cle2"))
