# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:35:12 2022

@author: ccrouan
"""


from Reservoir import *

class Stylo:
    def __init__(self, couleur):
        self.reservoir = Reservoir(couleur)
    def getCouleur(self):
        return self.reservoir.getCouleur()
    def setCouleur(self, couleur):
        self.reservoir.setCouleur(couleur)