# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:55:33 2022

@author: ccrouan
"""


class Carte: # Définition de la classe
    """Classe définissant une carte d'un jeu de 32 ou 52 cartes caractérisée par :
        — sa valeur
        — sa couleur
        — sa figure"""
    def __init__(self, valeur, couleur):
       self.valeur = valeur 
       self.couleur = couleur
       if valeur == 11:
           self.figure = "Valet"
       elif valeur == 12:
            self.figure = "Dame"
       elif valeur == 13:
            self.figure = "Roi"
       else:
            self.figure = "Aucune"
            
x = Carte(5,"carreau")
print(x.valeur)
print(x.couleur)

class Personne:
    def __init__(self, nom : str, prenom : str, age=33):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    def get_name(self):
        return self.__nom

qui = Personne("Dupont","Jean")
print(qui.get_name())
#print(qui.__nom)
qui.__nom = "Durant"
print(qui.get_name())

class Personne2:
    def __init__(self, nom : str, prenom : str, age=33):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    def __get_age(self):
        return self.__age
    def __set_age(self, age : int):
        if 100 > age > 17:
            self.__age = age
    age = property(__get_age, __set_age)

qui = Personne2("Dupont","Jean")
print(qui.age)
qui.age = 22
print(qui.age)

class Personne3:
    def __init__(self, nom : str, prenom : str, age=33):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    def __getattr__(self, name : str):
        return None
    def __get_age(self):
        return self.__age
    def __set_age(self, age : int):
        if age > 17:
            self.__age = age
    age = property(__get_age, __set_age)

qui = Personne3("Dupont","Jean")
print(qui.age)
qui.age = 22
print(qui.age)
qui.__name, qui.__age = "Albert", 10
print(qui.__name, qui.__age)
print(qui.ages)

class Personne4:
    def __init__(self, nom : str, prenom : str):
        self.__nom = nom
        self.__prenom = prenom
    def get_identity(self):
        return self.__prenom + " " + self.__nom
class AgentSpecial(Personne4):
    def __init__(self, nom : str, prenom : str, matricule : str):
        Personne4.__init__(self, nom, prenom)
        self.__matricule = matricule
    def get_matricule(self):
        return self.__matricule
    
qui = AgentSpecial("Dupont", "Jean", "007")
print("{0} : {1}".format(qui.get_identity(), qui.get_matricule()))

class Carte2:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        if valeur == 11:
            self.figure = "Valet"
        elif valeur == 12:
            self.figure = "Dame"
        elif valeur == 13:
            self.figure = "Roi"
        else:
            self.figure = "Aucune"
    def getCouleur(self):
        return self.couleur
    def getFigure(self):
        return self.figure
    def getValeur(self):
        return self.valeur
    def getAttributs(self):
        return (self.valeur, self.couleur, self.figure)
    def setFigure(self,valeur):
        if valeur == 11:
            self.figure = "Valet"
        elif valeur == 12:
            self.figure = "Dame"
        elif valeur == 13:
            self.figure = "Roi"
        else:
            self.figure = "Aucune"
    def setValeur(self,v):
        if 2<=v<=14:
            self.valeur = v
            self.setFigure(v)
            return True
        else:
            return False
    def setCouleur(self,c):
        if c in("pique","carreau","coeur","trefle"):
            self.couleur = c
            return True
        else:
            return False
        

x = Carte2(5,"carreau")
y = Carte2(14,"carreau")
print(x.getAttributs())
print(y.getAttributs())
c1 = Carte2(7, "coeur")
c1.getAttributs()
c1.setValeur(10)
c1.getAttributs()
c2 = Carte2(13, "coeur")
c2.setValeur(12)
c2.setCouleur("pique")
c2.setValeur(8)
c2.setCouleur("carreau")