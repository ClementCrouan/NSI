# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:37:56 2022

@author: ccrouan
"""

def recherche(tab, n):
    assert type(tab) == list, "erreur" 
    assert type(n) == int, "erreur"
    res = len(tab) #Initialise la variable res à la longueur de la liste tab
    for i in range(len(tab)):#Parcoure la liste
        if tab[i] == n:#Rechcerche la valeur n dans la liste tab
            res = i#Met la variable res à l'index de la liste qui correspond à n
    return res#Renvoie le résultat