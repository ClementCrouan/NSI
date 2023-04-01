# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:44:39 2022

@author: ccrouan
"""




def somme(a,b):
    if b == 0 or b < 0 or a < 0:
        return a
    else:
        return somme(a + 1, b - 1)

def factorielle(n):
    if n != 0:
        return (n * factorielle(n-1))
    elif n  == 0:
        return 1

def mystere(n):
    if n < 2:
        return str(n)
    else:
        return mystere(n // 2) + str(n%2)
    
def somme_nb(liste):
    if len(liste) != 0:
        return liste[0] + somme_nb(liste[1:])
    else:
        return 0

from turtle import*

  

"""def dessin():
    for i in range (50):
        color(couleurs[i%6])
        forward(i)
        right(59)

couleurs = ['blue','green',"yellow","orange","red","purple"]
bgcolor("black")

dessin()
exitonclick()"""

def dessin_pure(couleurs, indice):
    if indice == 0:
        return 0
    else:
        color(couleurs[(50-indice)%6])
        forward(50-indice)
        right(59)
        dessin_pure(couleurs, indice - 1)

couleurs = ['blue','green',"yellow","orange","red","purple"]
bgcolor("black")

#dessin_pure(couleurs, 50)
#exitonclick()

def koch(n,l):
    if n == 0:
        forward(l)
        print("j")
    else:
        koch(n-1,l/3)
        left(60)
        koch(n-1,l/3)
        right(120)
        koch(n-1,l/3)
        left(60)
*        koch(n-1,l/3)
        
    
def flocon(n,l):
    for i in range(3):
        koch(n,l)
        right(120)
        
koch(2, 200)
exitonclick()


def nettoie(L):
    if len(L)<= 1:
        return(L)
    if L[0]!=L[1]:
        return(L[0] +nettoie(L[1:]))
    else:
     return(nettoie(L[1:])) 