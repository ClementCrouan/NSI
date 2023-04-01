def menu():
    """création du menu"""
    global times
    if infosGrille != []:
        infosGrille["StateG"][0] = "Menu"
    else:
       times = 120
    for i in window.winfo_children():
        i.destroy()
    #345D7E : bleu - gris
    #FF5000 : orange
    pseudoBox1 = Frame(window,bg = "#FF5000")#affichage du pseudo
    Label(window, text = "Démineur", font=("Courrier",30), bg = "#345D7E" ,fg="white").pack(side = TOP, fill = X, ipady = 30)
    Label(pseudoBox1, text="Pseudo : ", font=("Roboto",17), bg = "#FF5000",fg="white").pack(pady = 5, side = LEFT)
    Label(pseudoBox1, text=pseudo, font=("Roboto",17), bg = "#FF5000",fg="white").pack(pady = 5, side = RIGHT)
    pseudoBox1.pack(side = TOP)
    global saisie
    global stateTimer
    pseudoBox2 = Frame(window,bg = "#FF5000")#boite de texte pour écrire un nouveau pseudo
    saisie = Entry(pseudoBox2, font=("Courrier",12),width = 10, bg = "white",fg="#345D7E")
    saisie.pack(side = LEFT)
    Button(pseudoBox2, image = checkBoxOnIcon, command = lambda : ["""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")""", Name(True)]).pack(padx = 3)
    pseudoBox2.pack(side = TOP)
    stateTimerBox = Frame(window, bg="#FF5000")#bouton permettant de désactiver/réactiver le temps limité
    Label(stateTimerBox, text="Timer :", font=("Roboto",15), bg = "#FF5000",fg="white").pack(side = LEFT)
    Button(stateTimerBox, image = stateTimer, command = lambda : ["""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")""", change_state(stateTimer)]).pack(side = RIGHT, padx = 3)
    stateTimerBox.pack()
    menu_deroulant()#affichage du menu deroulant et du tableau de score
    ranking(3, 50, 25)

def menu_deroulant():
    """affichage du menu déroulant
        (a placer dans chaque fenetre du menu)"""
    buttonBox = Frame(window,bg = "#FF5000")
    Button(buttonBox, image = playIcon, width = 50, height = 50, command = lambda: [difficulty.restart_after_menu(), """"playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = RIGHT)
    Button(buttonBox, image = homeIcon, width = 50, height = 50, command = lambda:[menu(),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = RIGHT,  ipadx = 0, ipady = 0)
    Button(buttonBox, image = statsIcon, width = 50, height = 50, command = lambda:[statistiquesA(),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = RIGHT)
    Button(buttonBox, image = missionIcon, width = 50, height = 50, command = lambda:[mission.print_mission(),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = RIGHT)
    Button(buttonBox, image = parametersIcon, width = 50, height = 50, command = lambda:[credit(),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = RIGHT)
    Button(buttonBox, image = leftIcon, width = 50, height = 50, command = lambda:[window.destroy(), """playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = RIGHT)
    buttonBox.pack(side = BOTTOM)

class Mission:
    """creation/verification/affichage/remplacement des défis"""
    def __init__(self):
        """creation de 3 défis si aucun n'est enregistré"""
        open("Mission.csv","a").close()
        if os.path.getsize("Mission.csv") == 0:
            with open("Mission.csv","a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                for i in range(3) :
                    writer.writerow(Mission.generation_missions())
        self.stateButton = [checkBoxOffIcon,checkBoxOffIcon,checkBoxOffIcon]#variables verifiants l'état des quêtes (accomplies ou non)
        self.games = [0,0,0]#et le nombres de parties réussies pour chaque défi

    def print_mission(self):
        """affichage des missions"""
        for i in window.winfo_children() : i.destroy()
        menu_deroulant()#affichage du menu déroulant
        bigMissionBox  = Frame(window,bg="#FF5000")
        with open("Mission.csv","r") as csvfile:
            missions = csv.reader(csvfile)
            i=0
            for row in missions:#Pour chaque ligne de Mission.csv (pour chaque défi), on écrit un "texte a trou"
                littleMissionBox = Frame(bigMissionBox, bg= "#FF5000")#en remplacant les trous par les infos de la mission(nb de parties, difficultée)
                if row[1] == "None": sentence = "Réussissez " + str(row[0]) + " partie(s) en mode " + row[2] + " : " + str(self.games[i]) + "/" + row[0]
                else : sentence = "Réussissez " + str(row[0]) + " partie(s) en moins de " + row[1] + " en mode " + row[2] + " : " + str(self.games[i]) + "/" + row[0]
                Label(littleMissionBox, text = sentence, font=("Roboto",15), bg = "#FF5000",fg="white").pack(side = LEFT)
                if i == 0:#on place a coté de chaque ligne(défi) un bouton pour la remplacer si le défi est réussi
                    Button(littleMissionBox, image = self.stateButton[0], command = lambda : mission.replace_mission(0)).pack(side = RIGHT)
                elif i == 1:
                    Button(littleMissionBox, image = self.stateButton[1], command = lambda : mission.replace_mission(1)).pack(side = RIGHT)
                else :
                    Button(littleMissionBox, image = self.stateButton[2], command = lambda : mission.replace_mission(2)).pack(side = RIGHT)
                littleMissionBox.pack()
                i+=1
            bigMissionBox.pack(expand = True)

    def generation_missions():
        """generation aleatoire d'une mission"""
        choice = randint(0,2)#on choisi un entier au hasard pour déterminer la difficultée de la mission
        difficulty = ["Facile", "Moyen", "Difficile"]
        for i in range(3):
            if i == choice :
                difficultyMission = difficulty[i]
                break
        numberMission = randint(1,3)#autre entier au hasard pour le nombre de parties a accomplir
        choice = randint(1,2)#autre entier pour savoir si il y a un temps limite ou non
        if choice == 1:
            if difficultyMission == "Facile": timeMission = "00:45"
            elif difficultyMission == "Moyen": timeMission = "01:30"
            elif difficultyMission == "Difficile": timeMission = "02:15"
        else :
            timeMission = "None"
        return [numberMission,timeMission,difficultyMission]#on retourne les infos sous forme de liste pour etre enregistre dans le fichier csv

    def replace_mission(self, numMission):
        """remplace le défi selectionne"""
        if self.stateButton[numMission] == checkBoxOnIcon:#on verifie que le defi soit accompli
            self.stateButton[numMission] = checkBoxOffIcon#on marque le nouveau defi comme non accompli
            with open("Mission.csv","r") as csvfile:#on copie le contenu du fichier sur une liste de listes
                reader = csv.reader(csvfile)
                missions = []
                for row in reader:
                    missions.append(row)
            with open("Mission.csv","w", newline = "") as csvfile:#on remplace le contenu du fichier par les anciennes missions et une nouvelle,
                writer = csv.writer(csvfile)#generee aleatoirement
                for i in range(3):
                    if i == numMission :
                        writer.writerow(Mission.generation_missions())
                        self.games[i] = 0
                    else : writer.writerow(missions[i])
            mission.print_mission()#on reaffiche la page pour que le nouveau defi s affiche
        
    def check_mission(self):
        """verifie l avancement des defis"""
        with open("Mission.csv","r") as csvfile:#on copie le contenu du fichier sur une liste de listes
            reader = csv.reader(csvfile)
            missions = []
            for row in reader:
                 missions.append(row)
        for i in range(3):#pour chacun des defis, si les conditions sont respectees,
            if missions[i][2] == difficulty.difficultyChoosen:
                achievement = False
                if missions[i][1] != "None":         
                    if stateTimer == checkBoxOnIcon: timeTaken =  times - (60*int(tempsAffichage[0:2]) + int(tempsAffichage[3:5]))
                    else : timeTaken = 60*int(tempsAffichage[0:2]) + int(tempsAffichage[3:5])#calcul du temps utilisé et du temps autorisé
                    timeAllow = 60*int(missions[i][1][0:2]) + int(missions[i][1][3:5])
                    print(timeAllow)
                    if timeTaken <= timeAllow: 
                        achievement = True
                else: achievement = True
                if achievement:
                    self.games[i] += 1#on augmente le nombre de parti realisees de 1
                    if self.games[i] == int(missions[i][0]):#si celui ci est egale aux nombre de parties a realisees on marque le defi comme accompli
                        self.stateButton[i] = checkBoxOnIcon
                 
def rule():
    """Onglet qui affiche les regles"""
    for i in window.winfo_children():
        i.destroy()
    ruleText = Label(window, text="\nChaque case de la grille peut soit cacher une mine, soit être vide. \nLe but du jeu est de découvrir toutes les cases vides sans faire exploser les mines,\n\
c'est-à-dire sans miner les cases qui les dissimulent. \nLorsque vous minez une case vide comportant au moins une mine dans l'une de ses cases voisines,\n\
un chiffre apparaît, indiquant ce nombre de mines.", font=("Roboto",15), bg = "#FF5000",fg="white")
    menu_deroulant()
    parametersBox = Frame(window, bg ="#FF5000")
    Button(parametersBox, text="Crédits", font=("Roboto",15), bg = "white",fg="#345D7E", command= lambda:[credit(),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = LEFT, padx = 5, pady = 10)
    Button(parametersBox, text="Règles", state = DISABLED, font=("Roboto",15), bg = "white",fg="#345D7E").pack(side = RIGHT, padx = 5, pady = 10)
    parametersBox.pack(side = TOP)
    ruleText.pack(expand = TRUE, fill = BOTH)

def credit():
    """Onglet qui affiche les credits"""
    for i in window.winfo_children():
        i.destroy()
    creditText = Label(window, text="\nGAME DESIGN : François\nPROGRAMMATION : François\nGRAPHISMES : François\nSCENARIO : François\nMUSIQUE : François\nLEVEL DESIGN : François\n\
FINANCEMENT : François\nTEST & DEBUG : François\nDANS LE ROLE DE FRANCOIS : Auxence\nFIGURANTS/STAGIAIRES : Clément & Martin", bg = "#FF5000",fg="white", font=("Roboto",15))
    menu_deroulant()
    parametersBox = Frame(window, bg ="#FF5000")
    Button(parametersBox, text="Règles", font=("Roboto",15), bg = "white",fg="#345D7E", command= lambda:[rule(),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = RIGHT, padx = 5, pady = 10)
    Button(parametersBox, text="Crédits", state = DISABLED, font=("Roboto",15), bg = "white",fg="#345D7E").pack(side = LEFT, padx = 5, pady = 10)
    parametersBox.pack(side = TOP)
    creditText.pack(expand = TRUE, fill = BOTH)


def infos_grille():
    """creation du dico de listes contenant les infos de la grille"""
    global infosGrille
    infosGrille = {}
    infosGrille["Mine"] = [0 for loop in range(100)]
    infosGrille["AroundM"] = [0 for loop in range(100)]
    infosGrille["Flag"] = ["" for loop in range(100)]
    infosGrille["Unlock"] = ["." for loop in range(100)]
    infosGrille["StateG"] = ["StartGame","info"]

def start_game(a):
    """appelle les fonctions de début de partie en fonction du nombre de mines choisies"""
    for i in window.winfo_children():
       i.destroy()
    infos_grille()#cree infos grille
    global nbMine
    global can
    global heure
    heure = time.time()
    nbMine = a
    can = Canvas(window, width = 600, height = 600, bg = '#333338')#cree la grille
    can.pack(side = LEFT, padx = 60, pady = 60)
    grille()#affiche la grille
    difficulty.choose_difficulty()#affiche les boutons sur le cote comme celui pour changer la difficulte
    clic()#commence a detecter les clics de l'utilisateurs

def affichage():
    """affiche la grille, la defaite ou la victoire si necaissaire apres chaque action"""
    if infosGrille["StateG"][0] == "Loose" or victor():#on verifie si on a gagne ou perdu pour mettre fin a la partie
        endgame()
    else:
        empty_propagation()#sinon on active la propagation des cases vides et on affiche la grille 
        grille()

def Name(player):
    """enregistre le pseudo choisi, le defini a 'Joueur 1' si necaissaire"""
    #player = True : l'utilisateur vient d'ecrire un nouveau pseudo
    #player = False : l'utilisateur vient de lancer une partie mais n'a peut etre pas de pseudo
    global saisie
    global times
    global pseudo
    if pseudo == "": pseudo = "Joueur 1"#si aucun pseudo n a ete choisie, il est defini a joueur 1
    if player :#si l'utilisateur a juste ecrit un nouveau pseudo, on l enregistre et on le ramene sur le menu
        pseudo = saisie.get()
        menu()
    else :#si il a lance une partie, bah on la lance
        start_game(20)
        times = 120

class Difficulty:
    """affichage des boutons sur les cotes(dont celui pour changer de diffficultee)
        relance les parties dans la difficultee choisie"""
    def __init__(self):
        """creation de difficultyChoosen"""
        self.difficultyChoosen = "Moyen"#lorsqu on lance le jeu la difficultée est moyen
        self.difficulty = StringVar(window)
        self.difficulty.set(self.difficultyChoosen)
        self.chooseBox = Frame(window, bg = "#FF5000")
        
    def restart_after_menu(self):
        """verifie si la difficultee est celle de base"""
        if self.difficultyChoosen == "Moyen" or self.difficultyChoosen == "Personnalisé":
            self.difficultyChoosen = "Moyen"
            Name(False)#quand le joueur lance une partie depuis le menu, on verifie qu'il
        else :#n'ai pas deja choisi de difficulte
            self.restart()
        
    def choose_difficulty(self):
        """affichage des boutons sur le cote durant une partie"""
        self.chooseBox = Frame(window, bg = "#FF5000")
        choix = ["Facile", "Moyen", "Difficile",  "Personnalisé"]
        Label(self.chooseBox, text=pseudo, font=("Roboto",15), bg = "#FF5000",fg="white").pack(pady = 10, ipadx = 20)
        global stateTimer
        global chronoText
        Button(bd = 0, image = pauseIcon, width = 27, height = 33, command = lambda: [pause(), """"playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = TOP, pady = 60)
        infosGrille["StateG"][0] = "StartGame"
        if stateTimer == checkBoxOnIcon:#creation de chronoText
            secondes = times % 60
            minutes = times // 60
            affichage = "%02d:%02d" % (minutes, secondes)
            chronoText = Label(self.chooseBox, text = affichage, font=("Roboto",15), relief = RIDGE, bd = 2)
        else:
            chronoText = Label(self.chooseBox, text = "00:00", font=("Roboto",15), relief = RIDGE, bd = 2)
        chronoText.pack()
        opt = OptionMenu(self.chooseBox, self.difficulty, *choix)#creation dun menu deroulant pour le choix des difficultes
        opt.config(font=("Roboto",15), bg = "white",fg="#345D7E")
        opt.pack(pady = 10, ipadx = 20)
        Button(self.chooseBox, text="Retour au menu", font=("Roboto",15), bg = "white",fg="#345D7E", command= lambda:[menu(),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(pady = 10)
        self.chooseBox.pack(side = BOTTOM, pady = 60, ipadx = 30)
        self.difficulty.trace("w", self.callback)#appelle callback des qu une difficultee est choisie


    def callback(*args):
        """lit la difficulte choisi dans le menu deroulant"""
        infosGrille["StateG"][0] = "Menu"
        difficulty.difficultyChoosen = format(difficulty.difficulty.get())
        difficulty.difficulty.set(difficulty.difficultyChoosen)
        difficulty.restart()#on recommence une partie dans la bonne difficultee

    def restart(self):
        """permet de relancer une partie avec la difficulte choisie precedamment"""
        global times
        if self.difficultyChoosen == "Facile":
            start_game(10)
            times = 60
        elif self.difficultyChoosen == "Moyen":
            start_game(20)
            times = 120
        elif self.difficultyChoosen == "Personnalisé":#affichage d une boite de texte qui demande le nombre de mines
            for i in window.winfo_children(): i.destroy()
            difficulty.choose_difficulty()
            infosGrille["StateG"][0] = "Menu"
            personelizeBox = Frame(window, bg = "#FF5000")
            Label(personelizeBox,  text= "Nombre de mines (de 5 à 50):", font=("Roboto",15), bg = "#FF5000",fg="white").pack(side = TOP)
            nbMine = Entry(personelizeBox)
            nbMine.pack(side = LEFT)
            Button(personelizeBox, image = checkBoxOnIcon, command = lambda : [difficulty.personalize_mine(nbMine, personelizeBox),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = RIGHT, pady = 10)
            personelizeBox.pack(side = BOTTOM)
        else :
            start_game(30)
            times = 180
            
    def personalize_mine(self, nbMine, personelizeBox):#verification du nombre entré pour la personnalisation des mines
        global times
        nb = nbMine.get()
        if nb.isdigit():
            nb = int(nb)
            if nb < 51 and nb > 4:
                for i in personelizeBox.winfo_children():
                    i.destroy()
                personelizeBox.destroy()
                start_game(nb)#si le nombre est correct on lance la partie
                times = nb * 6


def grille():
    """affichage de la grille"""
    can.delete(ALL)#on supprime tous les elementes presents(pour les remplacer t as capte)
    for y in range(10):#dessin de la grille
        for x in range(10):
            can.create_line(x * 60, 0, x * 60, 600, fill = "black")
            can.create_line(0, y *60, 600, y * 60, fill = "black")
    for y in range(10):
        for x in range(10):#pour chaque case on dessine l'item correspondant avec les bonnes coordonnees
            i = y*10+x
            if infosGrille['Unlock'][i] == " " and infosGrille['Flag'][i] == "#": infosGrille['Flag'][i] = ""
            if infosGrille['Unlock'][i] == "." and infosGrille['Flag'][i] != "#":
                grass(can,x*60,y*60)
            elif infosGrille['Flag'][i] == "#":
                flag(can, x*60, y*60)
            else:
                if infosGrille['Mine'][i] != 1 and infosGrille["AroundM"][i] != 0:
                    Number(infosGrille["AroundM"][i], can, x*60, y*60)
                elif infosGrille['Unlock'][i] == "+":
                    bombe(can, x*60, y*60)

def Number(n, can, x, y):
    """affichage du nombre de mines a proximite sur la case"""
    if n == 1 :#on regarde le numero a afficher pour le mettre dans une couleur specifique
        can.create_text((x+30,y+30), text = 1, fill = "white", font =("Roboto",15))
    elif n == 2 :
        can.create_text((x+30,y+30), text = 2, fill = "yellow", font =("Roboto",15))
    elif n == 3:
        can.create_text((x+30,y+30), text = 3, fill = "#FF7400", font =("Roboto",15))
    elif n == 4 :
        can.create_text((x+30,y+30), text = 4, fill = "#FF0000", font =("Roboto",15))
    elif n == 5:
        can.create_text((x+30,y+30), text = 5, fill = "#8A1185", font =("Roboto",15))
    else: can.create_text((x+30,y+30), text = n, fill = "#000000", font =("Roboto",15))

def grass(can,x,y):
    """affichage de l herbe sur la case"""
    can.create_rectangle((x,y), (x+60, y+60), fill = "#2DC512")

def cach(can,x,y):
    """affichage du cache sur la grille"""
    can.create_rectangle((x,y), (x+60, y+60), fill = "#2DC999", width = 1079, tag = "cache")

def flag(can,x ,y):
    """affichage du drapeau sur la case"""
    can.create_rectangle((x,y), (x+60, y+60), fill = "#2DC512")
    can.create_rectangle((x+19.375, y+5), (x+21.875, y+55),fill="black",)
    can.create_rectangle((x+21.875, y+5), (x+28.125, y+23.75),fill="blue")
    can.create_rectangle((x+28.125, y+5), (x+34.375, y+23.75),fill="white")
    can.create_rectangle((x+34.375, y+5), (x+40.625, y+23.75), fill="red")
    can.create_rectangle((x+19.375, y+8), (x+21.875, y+9.125), fill="blue",width=3,outline="blue")
    can.create_rectangle((x+19.375, y+18.75), (x+21.875, y+19.625), fill="blue",width=3,outline="blue")

def bombe(can, x, y):
    """affichage de la mine sur la case"""
    can.create_oval(x+7.5, y+10, x+52.5,y+55, fill ="black")
    can.create_rectangle((x+25, y+5), (x+35, y+30),fill="black")
    can.create_line((x+30,y+2.5),(x+30,y+30),fill="black")

def clic():
    """détecte les clics gauche/droit de la souris"""
    can.bind("<Button-1>", dif_user_request)
    can.bind("<Button-3>", user_request_flag)

def dif_user_request(e):
    """cherche quel case doit être creusée"""
    if infosGrille["StateG"][0] == "StartGame" or infosGrille["StateG"][0] == "Game":
        x = (e.x)//60
        y = (e.y)//60
        i = y*10+x
        if infosGrille['Unlock'][i] == ".":
           user_request_mine(e)
        elif infosGrille['Unlock'][i] == " " :
           quick_mine(e)

def user_request_flag(e):
    """pose un drapeau sur la case selectionnee"""
    x = (e.x)//60#calcul du numero de la case en fonction des coordonnees
    y = (e.y)//60
    i = y*10+x
    if infosGrille["Unlock"][i] == "." :
        if infosGrille["Flag"][i] != "#": infosGrille["Flag"][i] = "#"
        else : infosGrille["Flag"][i] = ""
        """playsound("Lantern Minecraft Sound Effects HD.mp3")"""
    affichage()

def user_request_mine(e):
    """creuse la case selectionnee"""
    x = (e.x)//60#calcul du numero de la case en fonction des coordonnees
    y = (e.y)//60
    i = y*10+x
    if infosGrille["Unlock"][i] == "." and infosGrille["Flag"][i] != "#":
        infosGrille["Unlock"][i] = " "
        """playsound("Minecraft Dirt Sound Effect.mp3")"""
        loose(e,0)#verifie si l'utilisateur a perdu
    if infosGrille["StateG"][0] == "StartGame" :#si on est au debut de la partie,
        infosGrille["StateG"][0] = "Game"#lance la creation des mines et le chronometre
        creation_mines(i)
        arround_m()
        global pauses
        pauses = 0
        updateTime()
    affichage()#pour la propagation des cases vides et afficher la grille

def loose(e,z):
    """verifie si l'utilisateur a miné une bombe"""
    x = (e.x)//60
    y = (e.y)//60
    i = y*10+x
    if infosGrille["Mine"][i+z] == 1:
          infosGrille["StateG"][0] = "Loose"
          infosGrille["StateG"][1] = "Game Over !\nVous avez miné une bombe."
          """playsound("Minecraft TNT Explosion - Sound Effect (HD).mp3")"""

def quick_mine(e):
    """dévoile toutes les cases autour de la case minée si celle si a déja été minée et si ses mines avoisinantes ont étées marquées"""
    count = nbDrapeau(e) #calcule le nombre de drapeau autour de la case choisi
    x = (e.x)//60
    y = (e.y)//60
    i = y*10+x#calcul du numero de la case choisie
    if infosGrille['AroundM'][i] == count:#si il y a autant de drapeaux a cotes que de mines a cotes
        if i >= 11 and  i%10!=0 :#pour chaque case voisine,
           if infosGrille["Flag"][i-11] != "#":#cherche si il y a un drapeau sur cette case
              infosGrille["Unlock"][i-11] = " "#dévoile la case
              loose(e,-11)#verifie si on a perdu
        if i >= 10 :
           if infosGrille["Flag"][i-10] != "#":
              infosGrille["Unlock"][i-10] = " "
              loose(e,-10)
        if i >= 10 and (i+1)%10 !=0:
           if infosGrille["Flag"][i-9] != "#":
              infosGrille["Unlock"][i-9] = " "
              loose(e,-9)
        if i >= 1 and i%10!=0 :
           if infosGrille["Flag"][i-1] != "#":
              infosGrille["Unlock"][i-1] = " "
              loose(e,-1)
        if i<=98 and (i+1)%10 !=0 :
           if infosGrille["Flag"][i+1] != "#":
              infosGrille["Unlock"][i+1] = " "
              loose(e,1)
        if i<= 89 and i%10 != 0 :
           if infosGrille["Flag"][i+9] != "#":
              infosGrille["Unlock"][i+9] = " "
              loose(e,9)
        if i<= 89 :
           if infosGrille["Flag"][i+10] != "#":
              infosGrille["Unlock"][i+10] = " "
              loose(e,10)
        if i<=88 and (i+1)%10 !=0 :
           if infosGrille["Flag"][i+11] != "#":
              infosGrille["Unlock"][i+11] = " "
              loose(e,11)
        """playsound("Minecraft Dirt Sound Effect.mp3")"""
    affichage()

def nbDrapeau(e):
    """cherche le nombre de drapeau autour de la case"""
    x = (e.x)//60
    y = (e.y)//60
    a = y*10+x #calcul du numero de la case
    count = 0#variable compteur du nombre de drapeau
    if  a>= 11 and  a%10!=0 and infosGrille['Flag'][a - 11] == "#":#cherche si il y a un drapeau sur la case choisi
        count += 1
    if a >= 10 and infosGrille['Flag'][a - 10] == "#":
        count += 1
    if a >= 10 and (a+1)%10 !=0 and infosGrille['Flag'][a - 9] == "#":
        count += 1
    if a >= 1 and a%10!=0 and infosGrille['Flag'][a-1] == "#":
        count += 1
    if a<=98 and (a+1)%10 !=0 and infosGrille['Flag'][a+1] == "#":
        count += 1
    if a<= 89 and a%10 != 0 and infosGrille['Flag'][a + 9] == "#":
        count += 1
    if a<= 89 and infosGrille['Flag'][a + 10] == "#":
        count += 1
    if a<=88 and (a+1)%10 !=0 and infosGrille['Flag'][a + 11] == "#":
        count += 1
    return count

def creation_mines(v):
    """cree le nombre de mines choisis a des cases aleatoires et a une case d'ecart de la case creusée
    v = case déja creusée"""
    i = 0
    while i < nbMine:
        case = randint(0,99)
        if infosGrille["Mine"][case] != 1 and case != v:#si il n'y a pas de mine sur la case choisie et qu'elle n'est pas creusée, 
            infosGrille["Mine"][case] = 1#on met une mine et on augmente le compteur de un
            i += 1
            if v >= 11 and  v%10!=0 and infosGrille['Mine'][v - 11] == 1:#on vérifie que la case choisie n'est pas un voisin de v, 
                infosGrille["Mine"][case] = 0#sinon on supprime la mine et on rebaisse le compteur
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
    global heure
    heure = time.time()

def arround_m():
    """calcul du nombre de mine à proximité"""
    for i in range (100):#pour chaque case, on vérifie pour tous les voisins existants si il y a une mine
        if i >= 11 and  i%10!=0 and infosGrille['Mine'][i - 11] == 1:infosGrille['AroundM'][i] += 1
        if i >= 10 and infosGrille['Mine'][i - 10] == 1:infosGrille['AroundM'][i] += 1
        if i >= 10 and (i+1)%10 !=0 and infosGrille['Mine'][i - 9] == 1:infosGrille['AroundM'][i] += 1
        if i >= 1 and i%10!=0 and infosGrille['Mine'][i-1] == 1:infosGrille['AroundM'][i] += 1
        if i<=98 and (i+1)%10 !=0 and infosGrille['Mine'][i+1] == 1:infosGrille['AroundM'][i] += 1
        if i<= 89 and i%10 != 0 and infosGrille['Mine'][i + 9] == 1:infosGrille['AroundM'][i] += 1
        if i<= 89 and infosGrille['Mine'][i + 10] == 1:infosGrille['AroundM'][i] += 1
        if i<=88 and (i+1)%10 !=0 and infosGrille['Mine'][i + 11] == 1:infosGrille['AroundM'][i] += 1

def debogage():
    """debogage pour la fin de partie"""
    if infosGrille["StateG"][0] == "Loose":#si on a perdu, on affiche les mines(ambiance triste)
        for i in range(100):
            if infosGrille["Flag"][i] == "#" : infosGrille["Flag"][i] = ""
            if infosGrille['Mine'][i] == 1: infosGrille['Unlock'][i] = "+"
            if infosGrille["Unlock"][i] == ".": infosGrille["Unlock"][i] = " "
    else:
        for i in range(100):#si on a gagne, on remplace les mines par de l'herbe(ambiance joyeuse)
            if infosGrille["Flag"][i] == "#" : infosGrille["Flag"][i] = ""
            if infosGrille['Mine'][i] == 1: infosGrille['Unlock'][i] = "."

def victor():
    """vérifie si on a gagne"""
    isVictor = True
    for i in range(100):
        if infosGrille["Mine"][i] == 0 and infosGrille["Unlock"][i] == ".":
            isVictor = False
            break
    if isVictor: infosGrille["StateG"][0] = "Victory"
    return isVictor

def empty_propagation():
    """propagation des cases vides"""
    empty = True
    while empty:
        empty = False
        for i in range(100):
            if infosGrille["AroundM"][i] == 0 and infosGrille["Unlock"][i] == " ":#on cherche une case creusé et sans mine avoisinante
                if i >= 11 and  i%10 !=0 :#on creuse ses voisins, si l'un d'eux n'a pas de mines avoisinantes, empty = True, donc la boucle recommence
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

def pause():
    global can
    global pauses
    global heure
    if infosGrille["StateG"][0] != "Pause" and infosGrille["StateG"][0] == "Game":
        infosGrille["StateG"][0] = "Pause"
        pauses = time.time()#heure du début de la pause
        cach(can, 0, 0)
    elif infosGrille["StateG"][0] == "Pause":
        infosGrille["StateG"][0] = "Game"
        can.delete("cache")
        heure += time.time() - pauses#calcul le temps de la pause et l'ajoute à l'heure du début de la partie 
        updateTime()
        
def endgame():
    """affiche le necessaire en fin de partie"""
    for i in window.winfo_children():
        if i != can :i.destroy()
    debogage()#creuse les dernieres cases pour afficher la reponse
    grille()#affiche les reponses
    box = Frame(bg = "#FF5000")#frame contenant les infos/boutons de fin de partie
    Label(box, text = pseudo, font=("Roboto",15), bg = "#FF5000",fg="white").pack(ipadx = 50, pady = 10)
    Label(box, text = tempsAffichage, font=("Roboto",15), bd = 2, relief = RIDGE).pack()
    if infosGrille["StateG"][0] == "Loose" :
        engameText = Label(box, text = infosGrille["StateG"][1], font=("Roboto",15), bg = "#FF5000",fg="white" )
        v1 = Volcano(can, 325, 100, ["red", "black", "grey"])#animation volcan pour défaite
        objects = [v1]

        window.after(500, simulate, can, objects)
    else:
        engameText = Label(box, text = "Victory !", font=("Roboto",15), bg = "#FF5000",fg="white" )
       
        ro = Rocket(can, 250, 550, "red")#animation feu d'artifice pour victoire
        ro1 = Rocket(can, 150, 600, "purple")
        ro2 = Rocket(can, 50, 525, "green")
        ro3 = Rocket(can, 350, 500, "yellow")
        ro4 = Rocket(can, 450, 625, "cyan")
        ro5 = Rocket(can, 550, 650)
        objects = [ro, ro1, ro2, ro3, ro4, ro5]
        window.after(500, simulate, can, objects)
        """playsound("Minecraft Fireworks Sound Effects HD.mp3")"""
        mission.check_mission()#verifie si on a avance dans les missions en reussissant cette partie
    engameText.pack(ipadx = 50, pady =10)
    Button(box, text = "Rejouer", font=("Roboto",15), bg = "white",fg="#345D7E", command = lambda:[difficulty.restart(), """playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(ipadx = 20, pady =10)
    Button(box, text = "Retour au menu", font=("Roboto",15), bg = "white",fg="#345D7E", command = lambda:[menu(), """playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(ipadx = 20, pady =10)
    box.pack(side = BOTTOM, pady = 60)
    ranking_save()#sauvegardes
    last_game_save()

class Particle:
    """Generic class for particles.

    Particles can be emitted by Fireworks objects. They are displayed for a
    specified lifespan and then removed from the canvas.
    
    """

    def __init__(self, cv=None, color='white', x=0., y=0.,
                 vx=0., vy=0., lifespan=5.):
        """Init Particle objects.

        """
        self.cv = cv
        self.cid = None
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.color = color
        self.age, self.lifespan = 0, lifespan

    def update(self, dt):
        global can
        """Update position and velocity after dt seconds have passed.

        """
        self.age += dt
        if self.alive():
            self.vy += GRAVITY * dt
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.cv.move(self.cid, self.vx * dt, self.vy * dt)
        elif self.cid is not None:
            can.delete(self.cid)
            self.cid = None

    def alive(self):
        """Check if particle is still within its lifespan."""
        return self.age <= self.lifespan


class SquareParticle(Particle):
    """A Particle with a quadratic shape"""
    def __init__(self, x=0., y=0., size=2., **kwargs):
        super().__init__(x=x, y=y, **kwargs)
        self.cid = self.cv.create_polygon(
            x - size, y - size, x + size, y - size,
            x + size, y + size, x - size, y + size,
            fill=self.color)


class TriangleParticle(Particle):
    """A Particle with a triangular shape"""
    def __init__(self, x=0., y=0., size=2., **kwargs):
        super().__init__(x=x, y=y, **kwargs)
        self.cid = self.cv.create_polygon(
            x - size, y - size, x + size,
            y - size, x, y + size,
            fill=self.color)


class CircularParticle(Particle):
    """A Particle with a circular shape."""
    def __init__(self, x=0., y=0., size=2., **kwargs):
        super().__init__(x=x, y=y, **kwargs)
        self.cid = self.cv.create_oval(
            x - size, y - size, x + size,
            y + size, fill=self.color)


class Fireworks:
    """Generic class for fireworks.

    The main "behavior" of a fireworks is specified via its update method.
    E.g., new particles can be emitted and added to the particle list. The
    Fireworks base class automatically updates all particles from the particle
    list in its update method.

    """

    def __init__(self, cv=None):
        """Init Fireworks objects.

        """
        self.cv = cv
        self.age = 0
        self.particles = []

    def update(self, dt):
        """Update the fireworks' particles and remove dead ones.

        """
        self.age += dt
        for p in self.particles:
                 p.update(dt)
        for i in range(len(self.particles) - 1, -1, -1):
            if not self.particles[i].alive():
                del self.particles[i]


class Volcano(Fireworks):
    """A volcano that continuously emits colored particles."""

    def __init__(self, cv, x, pps, colors):
        """Init Volcano objects.

        """
        super().__init__(cv)
        self.cid = cv.create_polygon(x - 12, 530,  # size and color are fixed
                                     x + 12, 530,  # (can be parametrized)
                                     x, 500,
                                     fill="orange")
        self.x = x
        self.pps = pps
        self.colors = colors
        self._tospawn = 0

    def update(self, dt):
        """Continuously emits new random particles and updates them.

        """
        super().update(dt)
        self._tospawn += self.pps * dt
        color = self.colors[int(self.age / 3) % len(self.colors)]
        for i in range(int(self._tospawn)):
            ptype = choice(
            [SquareParticle, TriangleParticle, CircularParticle])
            angle = uniform(-0.25, 0.25)
            speed = -uniform(80.0, 120.0)
            vx = sin(angle) * speed
            vy = cos(angle) * speed
            self.particles.append(
                ptype(cv=self.cv, x=self.x, y=500, color=color, vx=vx, vy=vy))
        self._tospawn -= int(self._tospawn)


class Rocket(Particle, Fireworks):
    def __init__(self, cv, x=0., y=0., color="blue",size=2., **kwargs):
        super().__init__(cv, x=x, y=y, **kwargs)
        self.cid = self.cv.create_oval( x - size, y - size, x + size, y + size, fill=self.color)
        self.x = x
        self.pps = 100
        self.colors = [color]
        self._tospawn = 0
        self.particles = []

    def update(self, dt):
        global can
        self.age += dt
        if self.alive():
            self.vy += -GRAVITY * dt
            self.x += self.vx * dt
            self.y += self.vy * dt
            can.move(self.cid, self.vx * dt, self.vy * dt)
        elif self.cid is not None:
            can.delete(self.cid)
            self.cid = None
        if self.cid is None:
             Fireworks.update(self, dt)
             color = self.colors[int(self.age / 3) % len(self.colors)]
             self._tospawn += self.pps * dt
             for i in range(int(self._tospawn)):
              ptype = choice([CircularParticle])
              angle = uniform(-100, 100)
              speed = -uniform(80, 120.0)
              vx = sin(angle) * speed
              vy = cos(angle) * speed
              self.particles.append(ptype(cv=can, x=self.x, y=self.y, color=color, vx=vx, vy=vy))
              self._tospawn -= self.pps * dt

def simulate(cv, objects):
    global running
    """Fireworks simulation loop.

    """
    t = time.time()
    while running:
        time.sleep(0.01)
        tnew = time.time()
        t, dt = tnew, tnew - t
        for o in objects:
            o.update(dt)
        cv.update()


def close(*ignore):
    """Stops simulation loop and closes the window."""
    global running
    running = False
    root.destroy()


def last_game_save():
    """Sauvegarde des statistiques de la dernière partie"""
    with open('LastGameSave.txt',"w") as txtfile :#statistique enregistrées dans un fichier .txt (plus facile a lire)
        contenu = pseudo + "\n"
        if infosGrille["StateG"][0] == "Victory" : contenu = contenu + "Victoire\n"
        else : contenu = contenu + "Défaite\n"
        contenu = contenu + "Difficulté : "+ difficulty.difficultyChoosen
        if stateTimer == checkBoxOnIcon: contenu = contenu + "\nTemps restant : "
        else : contenu = contenu + "\nTemps utilisé : "
        contenu = contenu + str(tempsAffichage)    
        txtfile.write(contenu)
  
def ranking_save():
    """Sauvegarde des Statistique de toutes les parties"""
    open('Ranking.csv',"a").close()
    with open('Ranking.csv', 'r') as csvfile :
        reader = csv.reader(csvfile)
        stats = []
        save = True
        index = 0
        for row in reader:#on copie le fichier sur une liste(stats)
            stats.append(row)
            if row[0] == pseudo:#si un score a deja ete enregistre pour le pseudo utilise,
                if infosGrille["StateG"][0] == "Victory":#on augmente le score de l'ancien pseudo et
                    x = int(stats[index][1]) + 1#save  = False (plus besoin d'enregistrer)
                    stats[index][1] = x
                else :
                    x = int(stats[index][2]) + 1
                    stats[index][2] = x
                save = False
            index += 1
        if save:#si la partie n'a pas etee enregistree, on cree une nouvelle ligne avec la victoire/defaite sur le nouveau pseudo
            if infosGrille["StateG"][0] == "Victory": stats.append([pseudo, 1, 0])
            else: stats.append([pseudo, 0, 1])
    with open("Ranking.csv", "w", newline = "") as csvfile :#on recopie la liste(stats) sur le fichier
        writer = csv.writer(csvfile)
        for i in range(len(stats)):
            writer.writerow(stats[i])

def ranking(maxi, lenght, h):
    """affichage du tableau de scores en fonction de sa taille"""
    open('Ranking.csv',"a").close()
    lignes  = 0
    with open("Ranking.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        stats = []
        for i in reader :#on copie le fichier sur une liste(stats)
            stats.append(i)
            lignes += 1
    newStats = []
    for i in range(len(stats)):#on classe les joueurs en fonction de leur nombre de victoire
        x = 0#sur une nouvelle liste(newStats)
        maxiVic = int(stats[x][1])
        maxiDef = int(stats[x][2])
        maxiIndex = x
        for j in range(1,len(stats)):
            if int(stats[j][1]) > maxiVic:
                maxiVic = int(stats[j][1])
                maxiDef = int(stats[j][2])
                maxiIndex = j
            elif int(stats[j][1]) == maxiVic:#si deux joueurs ont autant de victoires, on prend celui avec le moins de défaites
                if int(stats[j][2]) < maxiDef:
                    maxiVic = int(stats[j][1])
                    maxiDef = int(stats[j][2])
                    maxiIndex = j
        newStats.append(stats[maxiIndex])
        del stats[maxiIndex]
    if lignes > maxi : lignes = maxi
    scores = Canvas(window, width = lenght*6, height = h+lignes*h, bg= "#345D7E")#canvas contenant le tableau de scores
    scores.pack()
    for i in range(3):#on dessine les lignes et titres du tableau
        scores.create_line(i*(lenght*2), h+lignes*h, i*(lenght*2), 0, fill = "white")
    scores.create_text((lenght,h/2), text = "Pseudo", fill = "white", font =("Roboto",15))
    scores.create_text((lenght*3,h/2), text = "Victoires", fill = "white", font =("Roboto",15))
    scores.create_text((lenght*5,h/2), text = "Défaites", fill = "white", font =("Roboto",15))
    scores.create_line(0, h, 600, h, fill = "white")
    for i in range(lignes):#on affiche les informations dans le tableau
        if i > maxi-1 : break#autant que la variable maxi en demande (variable parametre de la fonction)
        scores.create_text((lenght,h/2+h*(i+1)), text = newStats[i][0], fill = "white", font =("Roboto",15))
        scores.create_text((lenght*3,h/2+h*(i+1)), text = newStats[i][1], fill = "white", font =("Roboto",15))
        scores.create_text((lenght*5,h/2+h*(i+1)), text = newStats[i][2], fill = "white", font =("Roboto",15))
        
def statistiquesA():
    """Affichage du tableau de scores"""
    for i in window.winfo_children():
        i.destroy()
    statsBox = Frame(window, bg ="#FF5000")#boutons pour naviguer entre les 2 pages de stats
    actualButton = Button(statsBox, text="Toutes les parties", font=("Roboto",15), bg = "white",fg="#345D7E")
    actualButton["state"] = DISABLED
    actualButton.pack(side = LEFT, padx = 5, pady = 10)
    Button(statsBox, text="Dernières parties", font=("Roboto",15), bg = "white",fg="#345D7E", command= lambda:[statistiquesB(),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = RIGHT, padx = 5, pady = 10)
    statsBox.pack(side = TOP)
    ranking(10, 100, 50)#affichage du tableau de scores avec la taille adaptee
    menu_deroulant()#affichage du menu déroulant
    
def statistiquesB():
    """Affichage des statistiques de la dèrnière parties"""
    open('LastGameSave.txt','a').close()
    obFichier=open('LastGameSave.txt','r')
    contenuFichier=obFichier.read()
    for i in window.winfo_children():
        i.destroy()
    statsBox = Frame(window, bg ="#FF5000")#boutons pour naviguer entre les 2 pages de stats
    Button(statsBox, text="Toutes les parties", font=("Roboto",15), bg = "white",fg="#345D7E", command= lambda:[statistiquesA(),"""playsound("Button-Plate Click (Minecraft Sound) - Sound Effect for editing.mp3")"""]).pack(side = LEFT, padx = 5, pady = 10)
    actualButton = Button(statsBox, text="Dernières parties", font=("Roboto",15), bg = "white",fg="#345D7E")
    actualButton["state"] = DISABLED
    actualButton.pack(side = RIGHT, padx = 5, pady = 10)
    statsBox.pack(side = TOP)
    texte = Label(window, text= contenuFichier, font=("Roboto",15), bg = "#FF5000",fg="white")#on print la contenu de LastGameSave (deja mis en page car .txt)
    Scrollbar(texte).pack(side = RIGHT, fill = Y)#barre de scroll inutile mais c drole
    menu_deroulant()#affichage du menu déroulant
    texte.pack(expand = TRUE, fill = BOTH)  


def updateTime():
    """calcul le temps ecoule"""
    global tempsAffichage
    global chronoText
    if stateTimer == checkBoxOnIcon:#calcul des minutes et secondes pour un temps limite
        minutesAffichage = (times - round(time.time() - heure)) // 60
        secondesAffichage = (times - round(time.time() - heure)) % 60
    else:#calcul des minutes et secondes pour un chronometre
        minutesAffichage = round(time.time() - heure) // 60
        secondesAffichage = round(time.time() - heure) % 60
    tempsAffichage = ("%02d:%02d" % (minutesAffichage, secondesAffichage))
    if stateTimer == checkBoxOnIcon and minutesAffichage == 0 and secondesAffichage <= 10:#si il ne reste plus que 10s, le chrono clignote rouge/noire
        if secondesAffichage % 2 == 0: chronoText.config(text = tempsAffichage,fg="#CC0505")
        else: chronoText.config(text = tempsAffichage, fg="black")
    elif infosGrille["StateG"][0] == "Game" :#changement du texte de chronoText
        chronoText.config(text = tempsAffichage)
    elif infosGrille["StateG"][0] == "Menu"  : chronoText.destroy()#si le joueur retourne sur le menu on detruit le chrono
    if time.time() - heure > times and stateTimer == checkBoxOnIcon:#si il n'y a plus de temps la partie est perdue
        infosGrille["StateG"][0] = "Loose"
        infosGrille["StateG"][1] = "Game Over !\nTemps écoulé."
        """playsound("Minecraft TNT Explosion - Sound Effect (HD).mp3")"""
        endgame()#affichage de fin de partie
    elif infosGrille["StateG"][0] == "Game":
        window.after(1000, updateTime)#fonction rappelée chaque seconde

def change_state(state):
    """change l'état du bouton pour choisir entre temps limité ou non"""
    global stateTimer
    if state == checkBoxOnIcon:
        stateTimer = checkBoxOffIcon
    else:
        stateTimer = checkBoxOnIcon
    menu()

from random import randint#tout les import (on a une armee la)
import time
from random import choice, uniform, randint
from math import sin, cos, radians
from sys import modules
from timeit import default_timer
import os
#from playsound import playsound
from tkinter import *
import csv
#Regles de nommage :
#variable : maVariable
#fonction : ma_fonction(maVariable)
#class : Class
#constante : CONSTANTE
window = Tk()
x = 10
GRAVITY = 30  # you can play around with this if you want
start = default_timer()
window.title("Démineur")#configuration de la fenetre
window.geometry("1080x720")
window.minsize(480,360)
window.config(background='#FF5000')
infosGrille = []
pseudo = "Joueur 1"
homeIcon = PhotoImage(file = r"home.png")
statsIcon = PhotoImage(file = r"stats.png")
checkBoxOnIcon = PhotoImage(file = r"checkboxon.png")
checkBoxOffIcon = PhotoImage(file = r"checkboxoff.png")
leftIcon = PhotoImage(file = r"leftgame.png")
playIcon = PhotoImage(file = r"play.png")
pauseIcon = PhotoImage(file = r"pause.png")
missionIcon = PhotoImage(file = r"mission.png")
parametersIcon = PhotoImage(file = r"parameters.png")
stateTimer = checkBoxOnIcon
mission = Mission()
difficulty = Difficulty()
running = True
menu()#appelle le menu
window.mainloop()
