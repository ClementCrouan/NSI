# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:21:54 2022

@author: ccrouan
"""


class Reservoir:
    def __init__(self, couleur):
        self.couleur = couleur
    def getCouleur(self):
        return self.couleur
    def setCouleur(self, couleur):
        self.couleur = couleur