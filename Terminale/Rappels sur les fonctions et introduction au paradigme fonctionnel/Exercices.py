# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:20:29 2022

@author: ccrouan
"""


#Ex bonus part 1
def premier(n):
    if type(n) == type(0) and n >= 0:
        for i in range(2, n):
            if n%i == 0:
                return False
        return True
    else:
        return False

#Ex bonus part 2
def premiers(n):
    nbPremiers = []
    if type(n) == type(0) and n >= 0:
         for i in range(2, n):
            if n%i == 0:
                return "Ce n'est pas un nombre premier"
            else:
                for j in range(2,i):
                    if i%j == 0:
                        break
                    elif j == i-1:
                        nbPremiers += [i]
                if i == 2:
                        nbPremiers += [i]
         return nbPremiers
    else:
        return "Ce n'est pas un nombre premier"
    
    
#Ex n°7

def f(nb):
    return nb**2


def applique(liste):
    listeModif = []
    for i in range (len(liste)):
        listeModif += [f(liste[i])]
    return listeModif

#Ex n°8

def calcul(op, liste):
    result = liste[0]
    for i in range (1, len(liste)):
        result = op(result, liste[i])
    return result

l=[1,2,3,4,5]

print(calcul(lambda x, y: x+y, l))
print(calcul(lambda x, y: x*y, l))
print(calcul(lambda x, y: max(x,y), l))