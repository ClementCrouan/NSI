# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:48:35 2022

@author: ccrouan
"""


import jeudecarte

jeu = jeudecarte.JeuDeCartes(32)
lepaquet = jeu.getPaquet()
for i in range(len(lepaquet)):
    print(lepaquet[i].getValeur(), lepaquet[i].getCouleur(),lepaquet[i].getFigure())
jeu.melanger()
for i in range (len(lepaquet)):
    print(lepaquet[i].getValeur(), lepaquet[i].getCouleur(), lepaquet[i].getFigure())
    