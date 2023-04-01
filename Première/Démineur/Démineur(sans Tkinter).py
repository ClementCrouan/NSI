import time
#Creation de infosGrille(1)
def infos_grille():
    infosGrille = {}
    infosGrille["Mine"] = [0 for loop in range(100)]
    infosGrille["AroundM"] = [0 for loop in range(100)]
    infosGrille["Flag"] = ["" for loop in range(100)]
    infosGrille["Unlock"] = ["." for loop in range(100)]
    return infosGrille

#Mines (pas de numero wtf)
from random import randint
def creation_mines(infosGrille):
    print("\nDifficulté :\nFacile - 1\nMoyen - 2\nDifficile - 3\nPersonnalisé - 4")
    a = check_entry(1,4)
    if a == 1: a = 10
    elif a == 2: a = 20
    elif a == 3: a = 30
    else:
        print("\nChoisissez le nombre de mines (entre 05 et 50).")
        a = check_entry(5,50)
    global pseudo
    pseudo = input("\nEntrer votre pseudo : ")
    i = 0
    state_of_the_shell(infosGrille, pseudo)
    while True:
        heure = time.time()
        res = user_request(infosGrille, heure)
        if res[3] =:            infosGrille = res[0]
            break
        else:
            state_of_the_shell(infosGrille, pseudo)
    v = 0
    #Trouve la position de la case vide
    for h in range(100):
        if infosGrille["Unlock"][h] == " ":
            v = h
            break
    while i < a:
        case = randint(0,99)
        if infosGrille["Mine"][case] != 1 and case != v:
            infosGrille["Mine"][case] = 1
            i += 1
            if v >= 11 and  v%10!=0 and infosGrille['Mine'][v - 11] == 1:
                infosGrille["Mine"][case] = 0
                i -= 1
            elif v >= 10 and infosGrille['Mine'][v - 10] == 1:
                infosGrille["Mine"][case] = 0
                i -= 1
            elif v >= 10 and (v+1)%10 !=0 and infosGrille['Mine'][v - 9] == 1:
                infosGrille["Mine"][case] = 0
                i -= 1
            elif v >= 1 and v%10!=0 and infosGrille['Mine'][v-1] == 1:
                infosGrille["Mine"][case] = 0
                i -= 1
            elif v<=98 and (v+1)%10 !=0 and infosGrille['Mine'][v+1] == 1:
                infosGrille["Mine"][case] = 0
                i -= 1
            elif v<= 89 and v%10 != 0 and infosGrille['Mine'][v + 9] == 1:
                infosGrille["Mine"][case] = 0
                i -= 1
            elif v<= 89 and infosGrille['Mine'][v + 10] == 1:
                infosGrille["Mine"][case] = 0
                i -= 1
            elif v<=88 and (v+1)%10 !=0 and infosGrille['Mine'][v + 11] == 1:
                infosGrille["Mine"][case] = 0
                i -= 1
    heure = time.time()
    return infosGrille, heure, pseudo

#Voisins de mines(2)
def around_m(infosGrille):
    """#calcul du nombre de mine à proximité
"""
    for i in range (100):#pour chaque case, on vérifie pour tous les voisins existants
        infosGrille['AroundM'][i] = 0#si il y a une mine
        if i >= 11 and  i%10!=0 and infosGrille['Mine'][i - 11] == 1:infosGrille['AroundM'][i] += 1
        if i >= 10 and infosGrille['Mine'][i - 10] == 1:infosGrille['AroundM'][i] += 1
        if i >= 10 and (i+1)%10 !=0 and infosGrille['Mine'][i - 9] == 1:infosGrille['AroundM'][i] += 1
        if i >= 1 and i%10!=0 and infosGrille['Mine'][i-1] == 1:infosGrille['AroundM'][i] += 1
        if i<=98 and (i+1)%10 !=0 and infosGrille['Mine'][i+1] == 1:infosGrille['AroundM'][i] += 1
        if i<= 89 and i%10 != 0 and infosGrille['Mine'][i + 9] == 1:infosGrille['AroundM'][i] += 1
        if i<= 89 and infosGrille['Mine'][i + 10] == 1:infosGrille['AroundM'][i] += 1
        if i<=88 and (i+1)%10 !=0 and infosGrille['Mine'][i + 11] == 1:infosGrille['AroundM'][i] += 1
    return infosGrille

#Debogage(3)
def debogage(infosGrille):
    """#debogage des mines
"""
    print("\n     ", end = " ")#print du tableau
    for i in range(10):
        print(i, end = "  ")
    print()
    print("  ", end = " ")
    for loop in range(34):
        print("-",end="")
    print()
    x = 0
    for ordonnee in range(10):
        print(x, end = "  ")
        x += 1
        print("|", end=" ")
        for abscisse in range(10):
            i = ordonnee*10+abscisse
            if infosGrille['Mine'][i] == 1: print(" +", end = " ")
            elif infosGrille['AroundM'][i] == 0 : print("  ", end = " ")
            else : print("",infosGrille["AroundM"][i], end = " ")
        print(" |")
    print("  ", end = " ")
    for loop in range(34):
        print("-",end="")

#Etat de cases(4)
def state_of_the_shell(infosGrille, pseudo):
    print("\n", pseudo, ":")
    print()
    print("     ", end = " ")
    for i in range(10):
        print(i, end = "  ")
    print()
    print("  ", end = " ")
    for loop in range(34):
        print("-",end="")
    print()
    x = 0
    for ordonnee in range(10):
        print(x, end = "  ")
        x += 1
        print("|", end=" ")
        for abscisse in range(10):
            i = ordonnee*10+abscisse
            if infosGrille['Unlock'][i] == " " and infosGrille['Flag'][i] == "#": infosGrille['Flag'][i] = ""
            if infosGrille['Unlock'][i] == "." and infosGrille['Flag'][i] != "#": print("",infosGrille['Unlock'][i], end = " ")
            elif infosGrille['Flag'][i] == "#": print("",infosGrille['Flag'][i], end = " ")
            else:
                #dévoilement des cases
                if infosGrille['Mine'][i] != 1 and infosGrille["AroundM"][i] != 0: print("",infosGrille['AroundM'][i], end = " ")
                elif infosGrille['Mine'][i] != 1 and infosGrille['AroundM'][i] == 0: print("",infosGrille['Unlock'][i], end = " ")
                elif infosGrille['Unlock'][i] == "+": print("",infosGrille['Unlock'][i], end = " ")
        print(" |")
    print("  ", end = " ")
    for loop in range(34):
        print("-",end="")
    print()

#Demande Utilisateur(5)
def user_request(infosGrille, debut):
    res = False
    info = ""
    print("\nMiner - 1\nPoser/Enlever un drapeau - 2")
    action = check_entry(1,2)
    print("Quel case choisissez-vous ? d'abord la ligne puis la colonne (ex: 02). ")
    while True:
        case = check_entry(0,99)
        if infosGrille['Unlock'][case] == ".": 
            if time.time() - debut >= 600000000:
                 res = True
                 info = "Vous avez mis trop de temps, les bombes se sont activé"
                 break

            elif action == 1:
                if infosGrille['Flag'][case] != "#":
                    infosGrille['Unlock'][case] = " "
                    if infosGrille["Mine"][case] == 1:
                        res = True
                        info = "Vous avez miné une bombe et ça à activé les autres"
                    break
                else: print("Vous avez posé un drapeau sur cette case, vous ne pouvez pas la miner.")     
            elif action == 2 :
                if infosGrille['Flag'][case] == "":
                    infosGrille['Flag'][case] = "#"
                    break
                else :
                    infosGrille['Flag'][case] = ""
                    break
        else : print("Cette case à déjà été minée.")
    return infosGrille, res, info, action

#Fin de la partie(6)
def game_over(infosGrille):
    for i in range(100):
        if infosGrille['Mine'][i] == 1:
            infosGrille['Unlock'][i] = "+" 
        if infosGrille["Flag"][i] == "#": infosGrille["Flag"][i] = ""
    return infosGrille

#Victoire(7)
def victor(infosGrille):
    isVictor = True
    for i in range(100):
        if infosGrille["Mine"][i] == 0 and (infosGrille["Flag"][i] == "#" or infosGrille["Unlock"][i] == "."):
            isVictor = False
            break
    return isVictor

#Devoilement auto des cases(8)
def empty_propagation(infosGrille):
    empty = True
    while empty:
        empty = False
        for i in range(100):
            if infosGrille["AroundM"][i] == 0 and infosGrille["Unlock"][i] == " ":
                if i >= 11 and  i%10 !=0 :
                    if infosGrille["AroundM"][i-11] == 0 and infosGrille["Unlock"][i-11] == "." : empty = True
                    infosGrille["Unlock"][i-11] = " "
                if i >= 10 :
                    if infosGrille["AroundM"][i-10] == 0 and infosGrille["Unlock"][i-10] == "." : empty = True
                    infosGrille["Unlock"][i-10] = " "
                if i >= 10 and (i+1)%10 !=0 :
                    if infosGrille["AroundM"][i-9] == 0 and infosGrille["Unlock"][i-9] == "." : empty = True
                    infosGrille["Unlock"][i-9] = " "
                if i >= 1 and i%10!=0 :
                    if infosGrille["AroundM"][i-1] == 0 and infosGrille["Unlock"][i-1] == "." : empty = True
                    infosGrille["Unlock"][i-1] = " "
                if i<=98 and (i+1)%10 !=0 :
                    if infosGrille["AroundM"][i+1] == 0 and infosGrille["Unlock"][i+1] == "." : empty = True
                    infosGrille["Unlock"][i+1] = " "
                if i<= 89 and i%10 != 0 :
                    if infosGrille["AroundM"][i+9] == 0 and infosGrille["Unlock"][i+9] == "." : empty = True
                    infosGrille["Unlock"][i+9] = " "
                if i<= 89 :
                    if infosGrille["AroundM"][i+10] == 0 and infosGrille["Unlock"][i+10] == "." : empty = True
                    infosGrille["Unlock"][i+10] = " "
                if i<=88 and (i+1)%10 !=0 :
                    if infosGrille["AroundM"][i+11] == 0 and infosGrille["Unlock"][i+11] == "." : empty = True
                    infosGrille["Unlock"][i+11] = " "
    return infosGrille

#Déroulement d’une partie
def game():
    global check
    infosGrille = infos_grille()
    infosGrille, start, pseudo = creation_mines(infosGrille)
    infosGrille = around_m(infosGrille)
    infosGrille = empty_propagation(infosGrille)
    state_of_the_shell(infosGrille, pseudo)
    while True:
        res = user_request(infosGrille, start)
        infosGrille = res[0]
        loseeerrr = res[1]
        if loseeerrr:
            check = 0
            infosGrille = game_over(infosGrille)
            state_of_the_shell(infosGrille, pseudo)
            print("\nGAME OVER")
            print(res[2])
            all_game_save()
            break
        if victor(infosGrille):
            check = 1
            debogage(infosGrille)
            print("\nVICTORY")
            all_game_save()
            break
        infosGrille = empty_propagation(infosGrille)
        state_of_the_shell(infosGrille, pseudo)
        


#Vérification des demandes utilisateurs
def check_entry(mini, maxi):
    while True:
        if maxi > 9:
            nb = input("Entrez un nombre : ")
            if len(nb) == 2:
                if nb.isnumeric():
                    nb = int(nb)
                    if nb >= mini and nb <= maxi :
                        return nb
                        break
                    else: print("Le nombre n'est pas dans l'intervalle.")
                else : print("Entrez des chiffres.")
            else : print("Entrez un nombre de deux chiffres.")
        elif maxi <= 9:
            nb = input("Entrez un chiffre : ")
            if len(nb) == 1:
                if nb.isnumeric():
                    nb = int(nb)
                    if nb >= mini and nb <= maxi :
                        return nb
                        break
                    else: print("Le chiffre n'est pas dans l'intervalle.")
                else : print("Entrez un chiffre.")
            else : print("Entrez un seul chiffre.")


#Sauvegarde des Statistique de toutes les parties
def all_game_save():
    global check
    global pseudo
    obFichier = open('AllGameSave.txt',"a")
    obFichier.close()
    obFichier = open('AllGameSave.txt', 'r')
    stats = obFichier.read()
    obFichier.close()
    if stats == "":
        stats = " "
    nb = 0
    csvpseudo = ""
    stats2 = ""
    vict = 0
    defe = 0
    save = True
    for i in stats:
        if i == ":":
            nb = 1
        if nb == 0:
            csvpseudo = csvpseudo + i
        if nb == 2 and i.isdigit():
            defe = int(i)
            nb =3
        if nb == 1 and i.isdigit():
            vict = int(i)
            nb = 2
        if nb == 4: nb =0
        if nb == 3 and i == "s":
            if pseudo == csvpseudo:
                if check == 1 : vict +=1
                else : defe += 1
                save = False
            stats2 = stats2 + csvpseudo + ": " + str(vict) + " victoires / " + str(defe) + " défaites\n"
            vict = 0
            defe = 0
            nb = 4
            csvpseudo = ""
    if save :
        if check == 1: stats2 = stats2 + pseudo + ": 1 victoires / 0 défaites\n"
        elif check == 0 : stats2 = stats2 + pseudo + ": 0 victoires / 1 défaites\n"
    obFichier = open('AllGameSave.txt', 'a')
    obFichier.truncate(0)
    obFichier.write(stats2)
    obFichier.close()
    


#Affichage des statistiques de toutes les parties
def statistiquesA():
    open('AllGameSave.txt','a').close()
    obFichier=open('AllGameSave.txt','r')
    contenuFichier=obFichier.read()
    while True:
        print(contenuFichier)
        obFichier.close()
        print("\nRetour au menu- 1")
        var = check_entry(1, 1)
        if var == 1: break

            
#Menu
def regle():
    while True:
        print("\nChaque case de la grille peut soit cacher une mine, soit être vide. \nLe but du jeu est de découvrir toutes les cases vides sans faire exploser les mines,\n\
c'est-à-dire sans miner les cases qui les dissimulent. \nLorsque vous minez une case vide2 comportant au moins une mine dans l'une de ses cases voisines,\n\
un chiffre apparaît, indiquant ce nombre de mines.")
        print("\nRetour au menu- 1")
        var = check_entry(1, 1)
        if var == 1: break
def credit():
    while True:
        print("\nGAME DESIGN : François\nPROGRAMMATION : François\nGRAPHISMES : François\nSCENARIO : François\nMUSIQUE : François\nLEVEL DESIGN : François\n\
FINANCEMENT : François\nTEST & DEBUG : François\nDANS LE ROLE DE FRANCOIS : Auxence\nFIGURANTS/STAGIAIRES : Clément & Martin")
        print("\nRetour au menu- 1")
        var = check_entry(1, 1)
        if var == 1: break

while True:
    print("\nLancer une partie - 1\nStatistique - 2\nRègles du jeu3\nCrédits - 4\nQuitter - 5")
    action = check_entry(1,5)
    if action == 1:
        while True:
            game()
            print("\nRejouer - 1\nRetour au menu - 2 ")
            replay = check_entry(1,2)
            if replay == 2 : break
    elif action == 2:statistiquesA()
    elif action == 3: regle()
    elif action == 4: credit()
    else: break
