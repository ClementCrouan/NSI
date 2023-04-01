# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:07:36 2022

@author: ccrouan
"""


def augmente(prix,pourcentage):
    pourcentage = 1 + pourcentage / 100
    prix *= pourcentage
    return prix
    
def reduction(prix, pourcentage):
    pourcentage = 1 - pourcentage / 100
    prix *= pourcentage
    return prix
    
    