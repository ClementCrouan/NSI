# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:41:04 2022

@author: ccrouan
"""


import Carte
import random

class JeuDeCartes:
    def CreerPaquet(self):
        monpaquet = []
        if self.nombreCarte == 32:
            num_debut = 7
        else:
            num_debut = 2
        for coul in ["carreau","coeur", "trèfle", "pique"]:
            for i in range(num_debut, 15):
                monpaquet.append(Carte.Carte(i, coul))
        return monpaquet
    def __init__ (self, nombreCarte):
        self.nombreCarte = nombreCarte
        self.paquetCarte = self.CreerPaquet()
    def getNombreCartes(self):
        return(self.nombreCarte)
    def getPaquet(self):
        return(self.paquetCarte)
    def melanger(self):
        random.shuffle(self.paquetCarte)
    