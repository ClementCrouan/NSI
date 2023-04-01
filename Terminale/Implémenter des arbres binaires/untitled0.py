# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:54:17 2023

@author: ccrouan
"""


class ArbreBinaire:
    def __init__(self, val=None):
        self.valeur=val
        self.enfant_gauche=None
        self.enfant_droit=None
    def insert_gauche(self,valeur):
        if self.enfant_gauche==None:
            self.enfant_gauche=ArbreBinaire(valeur)
        else:
            arbre_gauche=ArbreBinaire(valeur)
            arbre_gauche.enfant_gauche=self.enfant_gauche
            self.enfant_gauche=arbre_gauche
    def insert_droit(self,valeur):
        if self.enfant_droit==None:
            self.enfant_droit=ArbreBinaire(valeur)
        else:
            arbre_droit=ArbreBinaire(valeur)
            arbre_droit.enfant_droit=self.enfant_droit
            self.enfant_droit=arbre_droit
    def get_valeur(self):
        return self.valeur
    def get_droit(self):
        return self.enfant_droit
    def get_gauche(self):
        return self.enfant_gauche
    def __str__(self):
        return f'({self.valeur},{self.enfant_gauche},{self.enfant_droit})' 

racine=ArbreBinaire("A")
racine.insert_gauche("B")
racine.insert_droit("F")

node_B=racine.get_gauche()
node_B.insert_gauche("C")
node_B.insert_droit("D")

node_C=node_B.get_gauche()
node_C.insert_gauche("E")

node_F=racine.get_droit()
node_F.insert_gauche("G")
node_F.insert_droit("H")

node_H=node_F.get_droit()
node_H.insert_gauche("J")

node_G=node_F.get_droit()
node_G.insert_droit("I")
print(racine)