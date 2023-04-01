# Rendu de monnaie d'Alice
#  coding: utf-8

def somme(liste):
    """ Fonction qui retourne la somme de tous les éléments de la liste"""
    resultat=0
    for element in liste:
        resultat+= element
    return resultat

def monnaie_brute(rendre):
    """Fonction qui donne les différentes façons de donner rendre euros
       avec un nombre minimum de pièces de 3 valeurs différentes,
       4, 3 et 1"""

    minimum = rendre
    # minimum représente le nombre minimum de pieces à rendre
    listePieces = [] # liste des solutions possibles (optimales ou non)

    for i in range(rendre+1): # i est le nombre de pièces de 4 utilisées
        for j in range(rendre+1): # j est le nombre de pièces de 3 utilisées
            for k in range(rendre+1): # k est le nombre de pièces de 1 utilisées
                nombrePieces = i + j + k
                if i*4 + j*3 + k*1 == rendre and nombrePieces <= minimum:
                    minimum = nombrePieces
                    listePieces.append([i,j,k])

    solution = [] # liste des solutions optimales

    for possibilite in listePieces:
        if somme(possibilite) == mini:
            solution.append(possibilite)

    return [solution,minimum]


#Programme principal
rendre = int(input("somme à rendre: "))
reponse=monnaie_brute(rendre)[0]
mini=monnaie_brute(rendre)[1]
print("On peut rendre",rendre,"avec",mini,"pieces" )
for element in reponse:
  print(element[0],"pieces de 4, et ", element[1],"pieces de 3, et ", element[2],"pieces de 1")

  def monnaieGlouton(somme):
  pieces = [4, 3, 1]
  arendre = somme
  liste=[]
  for piece in pieces:
    while arendre >= piece:
      liste += [piece]
      arendre -= piece
  return liste

somme = int(input("somme à rendre: "))
print(monnaieGlouton(somme))
