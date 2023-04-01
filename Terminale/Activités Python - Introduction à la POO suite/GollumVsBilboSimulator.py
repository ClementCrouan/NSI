# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:46:07 2022

@author: ccrouan
"""
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import random

class Personnage:
    def __init__(self, nbreDeVie):
        self.vie = nbreDeVie
    def donneEtat(self):
        return self.vie
    def perdVie(self, r):
        self.vie -= 1 * r
    def boirePotion(self, r):
        self.vie += 1 * r
        
def game():
    bilbo = Personnage(20)
    gollum = Personnage(40)
    while bilbo.donneEtat() > 0 and gollum.donneEtat() > 0:
        res = int(input(f"Il vous restes {bilbo.donneEtat()} points de vie et il reste {gollum.donneEtat()} points de vie à Gollum. Quel action voulez-vous faire ? \n[1] Attaquez \n[2] Boire une potion\n"))
        if random.random()>0.5:
            r = 2
        else:
            r = 1
        if res == 1:
            gollum.perdVie(r)
        else:
            bilbo.boirePotion(r)
        if random.random()>0.5:
            bilbo.perdVie(1)
        else:
            gollum.boirePotion(1)
    if bilbo.donneEtat() <= 0 and gollum.donneEtat() > 0:
        msg = f"Gollum est vainqueur, il lui reste encore {gollum.donneEtat()} de vie points alors que vous êtes mort"
    elif gollum.donneEtat() <= 0 and bilbo.donneEtat() > 0:
        msg = f"Vous êtes vainqueur, il vous restes encore {bilbo.donneEtat()} points de vie alors que Gollum est mort"
    else:
        msg = "Egalité, vous êtes mort en même temps Gollum"
    print(msg)