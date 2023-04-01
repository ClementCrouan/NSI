# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:20:00 2023

@author: ccrouan
"""

def list_to_dico(liste):
    dico = {}
    for i in range(0,len(liste)-1, 2):
            dico[liste[i]] = liste[i+1]
    return dico

L = ['France','Paris','Royaune-Uni','Londres','Allemagne', 'Berlin']
print(list_to_dico(L))