# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:55:48 2022

@author: ccrouan
"""


class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        if valeur == 11:
            self.figure = "Valet"
        elif valeur == 12:
            self.figure = "Dame"
        elif valeur == 13:
            self.figure = "Roi"
        else:
            self.figure = "Aucune"
    def getCouleur(self):
        return self.couleur
    def getFigure(self):
        return self.figure
    def getValeur(self):
        return self.valeur
    def getAttributs(self):
        return (self.valeur, self.couleur, self.figure)
    def setFigure(self,valeur):
        if valeur == 11:
            self.figure = "Valet"
        elif valeur == 12:
            self.figure = "Dame"
        elif valeur == 13:
            self.figure = "Roi"
        else:
            self.figure = "Aucune"
    def setValeur(self,v):
        if 2<=v<=14:
            self.valeur = v
            self.setFigure(v)
            return True
        else:
            return False
    def setCouleur(self,c):
        if c in("pique","carreau","coeur","trefle"):
            self.couleur = c
            return True
        else:
            return False