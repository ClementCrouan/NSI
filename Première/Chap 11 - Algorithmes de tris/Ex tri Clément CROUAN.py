print("---------Ex n°1---------")
def Tri(nbCartes):
    cartes = []
    for loop in range(len(nbCartes)):
        nb = 0
        mini = nbCartes[0]
        for i in range(0, len(nbCartes)):
            if nbCartes[i] < mini:
                nb = i
                mini = nbCartes[i]
        cartes += [mini]
        del nbCartes[nb]
    return cartes

def Saisie():
    liste = []
    stop = False
    while stop == False:
        nb = input("Nombre :")
        if nb != "a":
            nb = float(nb)
            liste += [nb]
        else:
            stop = True
            return liste


print("Pour arrêter la saisie appuyer sur la touche a de votre clavier")


print(Tri(Saisie()))

print("---------Ex n°2---------")

liste=[11,16,5,9,13]

for i in range(len(liste)-1):
    mini = 1
    for j in range(i+1, len(liste)):
        if liste[j] < liste[mini]:
            mini = j
    liste[i], liste[mini] = liste[mini], liste[i]
print(liste)

liste=[11,16,5,9,13]

for i in range(len(liste)):
    x=liste[i]
    j=i
    while j>0 and liste[j-1]>x:
        liste[j]=liste[j-1]
        j-=1
        liste[j]=x
print(liste)

print("---------Ex n°3---------")

# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from random import *
import time

def insert(liste):
    for i in range(len(liste)):
        x = liste[i]
        j=i
        while j>0 and liste[j-1]>x:
            liste[j]=liste[j-1]
            j=j-1
            liste[j]=x
    return (liste)

def  select(liste):
    for i in range(len(liste)-1):
        mini=i
        for j in range(i+1,len(liste)):
            if liste[j]<liste[mini]:
                mini=j
        liste[i],liste[mini]=liste[mini],liste[i] #échange des valeurs
    return(liste)

def compare(n):
    liste=[0]*n
    for i in range(n):
        liste[i]=randint(0,n)
    e=time.perf_counter()
    liste1=select(liste)
    e1=time.perf_counter()
    e1 -= e

    e=time.perf_counter()
    liste2=insert(liste)
    e2=time.perf_counter()
    e2-=e
    return("le temps cpu selection=",e1,"le temps cpu insert=",e2)


#programme principal
m=int(input("combien de valeurs dans la liste?"))
print("pour ",m," valeurs dans la liste ",compare(m))

print("-------Ex n°1 Question 1--------")
liste = [10, 11, 20, 50, 100]
print("liste de départ:", liste)
liste += [float(input("Nouvel élément à ajouté:"))]
                

for i in range(len(liste)):
    x=liste[i]
    j=i
    while j>0 and liste[j-1]>x:
        liste[j]=liste[j-1]
        j-=1
        liste[j]=x
print(liste)

print("-------Ex n°1 Question 2--------")
liste = [100, 10, 60.5, 78, 1, 200.5, 55, 1.2]
print("liste de départ:", liste)

print(Tri(liste))
