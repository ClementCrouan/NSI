from math import *
rayon = float(input("Le rayon du cercle est de :"))
perimetre = 0
aire = 0
q1 = input("Voulez-vous obtenir le périmètre ?")
q2 = ""
if q1 == "oui":
    perimetre = 2 * rayon
    print(perimetre)
q2 = input("Voulez-vous obtenir l'aire ?")
if q2 == "oui":
    aire = pi * rayon**2
    print(aire)
