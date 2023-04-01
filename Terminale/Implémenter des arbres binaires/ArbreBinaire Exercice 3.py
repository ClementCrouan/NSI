class ArbreBinaire:
    def __init__(self, val=None):
        self.valeur=val
        self.enfant_gauche=None
        self.enfant_droit=None
    def insert_gauche(self,valeur):
        if self.enfant_gauche==None:
            self.enfant_gauche=ArbreBinaire(valeur)
        else:
            arbre_gauche=ArbreBinaire(valeur)
            arbre_gauche.enfant_gauche=self.enfant_gauche
            self.enfant_gauche=arbre_gauche
    def insert_droit(self,valeur):
        if self.enfant_droit==None:
            self.enfant_droit=ArbreBinaire(valeur)
        else:
            arbre_droit=ArbreBinaire(valeur)
            arbre_droit.enfant_droit=self.enfant_droit
            self.enfant_droit=arbre_droit
    def get_valeur(self):
        return self.valeur
    def get_droit(self):
        return self.enfant_droit
    def get_gauche(self):
        return self.enfant_gauche
    def __str__(self):
        return f'({self.valeur},{self.enfant_gauche},{self.enfant_droit})' 

def parcours_prefixe(arbre):
    if arbre != None:
        print(arbre.valeur)
        parcours_prefixe(arbre.gauche)
        parcours_prefixe(arbre.droit)
        
def parcours_infixe(arbre):
    if arbre != None:
        parcours_infixe(arbre.gauche)
        print(arbre.valeur)
        parcours_infixe(arbre.droit)
        
def parcours_suffixe(arbre):
    if arbre != None:
        parcours_prefixe(arbre.gauche)
        parcours_prefixe(arbre.droit)
        print(arbre.valeur)

racine=ArbreBinaire(15)
racine.insert_gauche(6)
racine.insert_droit(18)

node_18=racine.get_gauche()
node_18.insert_gauche(17)
node_18.insert_droit(20)

node_6=racine.get_gauche()
node_6.insert_gauche(3)
node_6.insert_droit(7)

node_3=node_6.get_droit()
node_3.insert_gauche(2)
node_3.insert_droit(4)

node_7=node_6.get_droit()
node_7.insert_droit(13)

node_13=node_7.get_droit()
node_13.insert_droit(9)
print(racine)
print(parcours_prefixe(racine))
print(parcours_suffixe(racine))
print(parcours_infixe(racine))