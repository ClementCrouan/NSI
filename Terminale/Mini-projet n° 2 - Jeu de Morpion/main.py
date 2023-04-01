import grille as gri
import graphisme as gra
import bot

def menu():
    """
    Affiche menu, execute action demandées par le joueur
    """
    global MENU
    action = MENU.get_action_menu()
    if action == 5:#Lancer une partie
        MENU.destroy()
        res = game(gri.Morpion(), gra.Game(), 0) 
        MENU = gra.Menu(BOT)
    if action == 4:#Activer/Desactiver le bot
        MENU.destroy()
        if BOT.active:
            BOT.active = False
        else :
            BOT.active = True
        MENU = gra.Menu(BOT)
    elif action == 3:#Difficulte du bot
        MENU.destroy()
        if BOT.difficulty == 1:
            BOT.difficulty = 2
        elif BOT.difficulty == 2:
            BOT.difficulty = 3
        else:
            BOT.difficulty = 1
        MENU = gra.Menu(BOT)
    elif action == 2:#Tour du bot
        MENU.destroy()
        if BOT.NoPlayer == 1:
            BOT.NoPlayer = 2
        else:
            BOT.NoPlayer = 1
        MENU = gra.Menu(BOT)
    if action == False or action == 1:#Quitter
        MENU.destroy()
    else : 
        menu()

def game(grille, gameScreen, tour):
    """
    Déroulement d'une partie
    """
    for i in range(1,3):
        tour += 1
        exi = False
        while exi == False:
            if BOT.active and i == BOT.NoPlayer :#fais jouer le bot
                co = BOT.play(tour, grille.infosGrille)
                if grille.check_case(co):
                    pos = co
                    exi = True
            else:
                co = gameScreen.get_action_game()
                if grille.check_case(co):
                    pos = co
                    exi = True
        grille.round(i, pos)
        gameScreen.print_table_pygame(grille.infosGrille)#actualise (affiche) l'ecran
        if grille.check_win()[0] != 0:#verifie si win, sinon on rappelle la fonction game() 
            winner, pos = grille.check_win()
            gameScreen.win(winner, pos, grille.infosGrille)
            gameScreen.destroy()
            return winner
        elif tour == 9:
            gameScreen.destroy()
            return 0
    return game(grille, gameScreen, tour)

#Nomenclature :
#VARIABLEGLOBALE
#variableVariable
#fonction_fonction
#Classe
BOT = bot.Bot(2, False, 1)
MENU = gra.Menu(BOT)
menu()
