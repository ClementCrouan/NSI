# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:38:12 2022

@author: ccrouan
"""
class Maillon;$:
    def __init__(self, valeur = None, suivant = None):
        self.valeur = valeur
        self.suivant = suivant
    def __str__(self):
        if self.valeur is not None:
            return str(self.valeur) + '' + str(self.suivant)
        else:
            return str(None)