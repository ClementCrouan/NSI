print("Ex n°1 Clémentine")
print("Si vous avez fini de mettres vos notes mettez un nombre négatif qui ne sera pas compté dans les notes")
def Note():
    listeNote = []
    stop = False
    while stop == False:
        note = float(input("Note :"))
        if note >= 0:
            listeNote += [note]
        else:
            stop = True
            return(listeNote)
def Moyenne(notesTotales):
    total = 0
    moyenne = 0
    for i in range(len(notesTotales)):
        total += notesTotales[i]
    moyenne = total / len(notesTotales)
    return(f"{moyenne:5.2f}")
    

liste = []

liste = Note()
print(liste)
if len(liste) > 0:
    print("La plus petite note est un", min(liste))
    print("La plus grande note est un", max(liste))
    print("La moyenne est de", Moyenne(liste))
print("Vous n'avez entré aucune note")

  
print("Ex n°2")
import random

#Fonction lancé des dés
def DéLancé():
    #liste des résultats des lancé de dés
    résultats = []
    #10 lancés
    for loop in range(10):
        #Lancé de dé aléatoire
        dé = random.randint(1,6)
        #résultat du lancé de dé
        résultats += [dé]
    #retourne la list des réultats du lancé de dés
    return(résultats)
#nombre de 6 obtenu lors des 10 lancés
nb6 = 0
#Nombre de points d'Alice
pointA = 0
#Nombre de points de Bob
pointB = 0
#Le meileur des scores
bestPoint = 0
#Numéro de la manche
nbManche = 0

#Stop la boucle dès que quelqu'un à 10 points
while bestPoint < 10:
    #Remet à 0 au début de la manche le nombre de 6 obtenu
    nb6 = 0
    #Met à jour le numéro de la manche
    nbManche += 1
    #Lance 10 fois le dé
    sérieLancé = DéLancé()
    #Analyse les résultat des lancés de dés
    for i in range(len(sérieLancé)):
        #Vérifi s'il y a eu un 6 lors des lancés de dé
        if sérieLancé[i] == 6:
            #Ajoute 1 au nombre de 6 obtenu lors de la manche
            nb6 += 1
    #Vérifi si le nombre de 6 obtenu lors de la manche est suppérrieur ou égal
    #à 2 et vérifi si c'est la manche d'Alice ou de Bob
    if nb6 >= 2 and nbManche % 2 == 0:
        #Ajoute un point à Alice
        pointA += 1
    #Vérifi si le nombre de 6 obtenu lors de la manche est suppérrieur ou égal
    #à 2
    elif nb6 >= 2:
        #Ajoute un point à Bob
        pointB += 1
    #Condition pour connaitre qui mène
    if pointA > pointB:
        #Met à jour le nombre de point, pour savoir quand arrêter la boucle
        bestPoint = pointA
    #Condition pour connaitre qui mène
    elif pointA < pointB:
        #Met à jour le nombre de point, pour savoir quand arrêter la boucle
        bestPoint = pointB
    #Si Alice et Bob sont à égalités
    else:
        #Met à jour le nombre de point, pour savoir quand arrêter la boucle
        bestPoint = pointA
    #Vérifi si Alice à gagner
    if pointA == 10:
        #Phrase pour donner le score
        print("Alice a",pointA, "points et Bob a", pointB, "points")
        #Phrase pour dire qu'Alice à gagné
        print("Alice a gagné")
    #Vérifi si Bob à gagner
    elif pointB == 10:
        #Phrase pour donner le score
        print("Alice a",pointA, "points et Bob a", pointB, "points")
        #Phrase pour dire que Bob à gagné
        print("Bob a gagné")

print("Ex n°2")

nbImpairs = []

for i in range (1, 50, 2):
    nbImpairs += [i]
print(nbImpairs)

nbImpairs = []

for i in range (1, 50):
    if i % 2 == 1:
        nbImpairs += [i]
print(nbImpairs)


print("Ex n°3")
test = [11.367357, 30.1452365, 57.35264, 60.49235, 90.9]
print("Question n°1")
def minimum(listes):
    mini = listes[0]
    nb = 0
    for i in listes:
        nb = i
        if nb < mini:
            mini = nb
    return mini
print(minimum(test))
print("Question n°2")
def somme(listes):
    total = 0
    for i in range (len(listes)):
        total += listes[i]
    return total
print(somme(test))
print("Question n°3")
def moyenne(listes):
    total = 0
    moyenne = 0
    for i in range(len(listes)):
        total += listes[i]
    moyenne = total / len(listes)
    return(moyenne)
print(moyenne(test))
print("Ex n°4")

def ListeNb():
    nb = []
    nombre = 0
    for loop in range(1000):
        nombre = random.randint(0, 9)
        nb += [nombre]
    return(nb)

liste = ListeNb()
nb0 = 0

for i in range(len(liste)):
    if liste[i] == 0:
        nb0 += 1
print("Il y a eu", nb0, "zéros")

print("Exercice 5")
print("Question b")

def somme_ligne(carre, n):
  somme = 0
  for nombre in carre[n]:
    somme += nombre
  return somme

carre3 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
carre4 = [[4, 5, 11, 14], [15, 10, 8, 1], [6, 3, 13, 12], [9, 16, 2, 7]]
total = []

for n in range (len(carre4)):
  total += [somme_ligne(carre4,n)]
if total[0] == total[1] and total[1] == total[2] and total[2] == total[3]:
	print("C'est un carré parfait")
else:
  print("Ce n'est pas un carré parfait")

print("Question c")

def somme_colonne(carre, n, c):
    somme = carre[n][c]
    return somme

sommeColonne = 0
total = []
for n in range (len(carre4)):
    for i in range (len(carre4[n])):
        sommeColonne += somme_colonne(carre4, i, n)
    total += [sommeColonne]
    sommeColonne = 0
if total[0] == total[1] and total[1] == total[2] and total[2] == total[3]:
    print("C'est un carré parfait")
else:
    print("Ce n'est pas un carré parfait")
