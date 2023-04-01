# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:21:40 2022

@author: ccrouan
"""


import vente as vente

def vendeur(prix, pourcentage, indice):
    if indice >= 0:
        print(vente.augmente(prix, pourcentage))
    else:
        print(vente.reduction(prix, pourcentage))