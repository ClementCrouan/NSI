# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:57:23 2022

@author: ccrouan
"""


class Piece:
    def __init__(self, surface, nom):
        self.nom = nom
        self.surface = surface
    def getSurface(self):
        return self.surface
    def getNom(self):
        return self.nom
    def setSurface(self, s):
        self.surface = s
class Appartement:
    def __init__(self, nom):
        self.listeDePieces = []
        self.nom = nom
    def getNom(self):
        return self.nom
    def ajouter(self, piece):
        self.listeDePieces.append(piece)
    def nbPieces(self):
        return(len(self.listeDePieces))
    def SurfaceTotale(self):
        total = 0
        for i in self.listeDePieces:
            total += i.getSurface()
        return total

salle1 = Piece(20,"chambre1")
salle2 = Piece(15, "chambre2")
salle3 = Piece(25, "séjour")
salle4 = Piece(10, "séjour")
salle5 = Piece(12, "cuisine")

appart = Appartement("appart205")
appart.ajouter(salle1)
appart.ajouter(salle2)
appart.ajouter(salle3)
appart.ajouter(salle4)
appart.ajouter(salle5)
print(appart.SurfaceTotale())
for i in range (appart.nbPieces()):
    print(appart.listeDePieces[i].getNom())
    print(appart.listeDePieces[i].getSurface())
    
    