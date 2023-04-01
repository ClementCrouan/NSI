print("Exercice n°1")

#Le jeu mystere
from random import randint

def mystere (entier):
    secret = randint(1, 6)
    reponse = entier == secret #reponse est de type : bool
    return (entier, secret, reponse) #Type retourne par
        #La fonction mystere : tuple
nombre = int(input("Donnez un entier entre 1 et 6 :"))
tuple_reponse = mystere (nombre)
if tuple_reponse[2] == True:
    print("Vous avez gagné 6 euros")
else:
    print(nombre, "est différent de", tuple_reponse[1])
    print("vous avez perdu 1 euro")


print("Exercice n°2")

def reduction(prix, taux):
    economie = prix * (taux / 100)
    prix_reduit = prix - economie
    return((prix_reduit, economie))

prixBase = float(input("prix de l'article :"))
tauxRed = float(input("réduction (en %):"))
total = reduction(prixBase, tauxRed)


print("Après reduction, vous devez payer :", total[0], "euros")
print("Vous avez economise :", total[1], "euros")
