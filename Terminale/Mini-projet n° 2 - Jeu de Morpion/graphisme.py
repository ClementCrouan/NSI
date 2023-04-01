import pygame

class Game:
    def __init__(self, size = (900,900)):
        """
        Crée affichage d'une partie
        """
        pygame.init()
        self.screen = pygame.display.set_mode(size)#creation de la fenetre
        pygame.display.set_caption('Morpion')
        self.croix = pygame.image.load("croix.png")
        self.croixVerte = pygame.image.load("croix_verte.png")
        self.rond = pygame.image.load("rond.png")
        self.rondVert = pygame.image.load("rond_vert.png")
        self.screen.fill('white')
        for i in range(1,3):#quadriage du morpion
            pygame.draw.line(self.screen, "black", (0,i*300),(900,i*300), 5)
            pygame.draw.line(self.screen, "black", (i*300,0),(i*300,900), 5)
        

    def get_action_game(self):
        """
        Obtiens action executee par le joueur (click sur case)
        """
        pygame.display.flip()
        run = True
        while run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN :
                    if pygame.mouse.get_pressed() == (1,0,0):
                        pos = pygame.mouse.get_pos()
                        a = pos[1]//300#convertie coordonnees du click en numero de case
                        b = pos[0]//300
                        return (a,b)

    def print_table_pygame(self, l):
        """
        Affiche les pions sur le morpion 
        """
        for i in range(3):
            for j in range(3):
                if l[i][j] == 1:
                    self.screen.blit(self.croix, (j*300+100,i*300+100))
                elif l[i][j] == 2:
                    self.screen.blit(self.rond, (j*300+100,i*300+100))
        pygame.display.flip()

    def destroy(self):
        """
        Détruit la fenetre
        """
        run = True
        while run :
            for event in pygame.event.get():
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    run = False
        pygame.quit()

    def win(self, win, pos, l):
        for i in range(3):
            for j in range(3):
                for x in range(3):
                    if i == pos[x][0] and j == pos[x][1] and win == 2:
                        self.screen.blit(self.rondVert, (j*300+100,i*300+100))
                    elif i == pos[x][0] and j == pos[x][1] and win == 1:
                        self.screen.blit(self.croixVerte, (j*300+100,i*300+100))
        pygame.display.flip()


class Menu:
    def __init__(self, bot, size = (800,600)):
        """
        Crée affichage du menu
        """
        pygame.init()
        self.screen = pygame.display.set_mode(size)#cree la fenetre
        pygame.display.set_caption('Morpion')
        self.screen.fill('white')
        textButtons = ["Quitter","Tour du bot","...","...","Lancer une partie"]#texte a afficher sur les boutons
        if bot.active :
            textButtons[3] = "Bot : activé"
        else :
            textButtons[3] = "Bot : désactivé"
        if bot.difficulty == 1:
            textButtons[2] = "Bot : clément"
        elif bot.difficulty == 2:
            textButtons[2] = "Bot : difficile"
        else :
            textButtons[2] = "Bot : impossible"
        if bot.NoPlayer == 1:
            textButtons[1] = "Bot : Joueur 1"
        else :
            textButtons[1] = "Bot : Joueur 2"
        font = pygame.font.SysFont("arial", 20)
        for i in range(1,6):#affichage des boutons
            text = font.render(textButtons[i-1], True, 'black')
            self.screen.blit(text, (50,585-i*45))
            pygame.draw.rect(self.screen, "black", (50,585-i*45, 250,35), 3)
        
    def get_action_menu(self):
        """
        Obtiens action executee par le joueur (click sur bouton)
        """
        pygame.display.flip()
        run = True
        while run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN :
                        pos = pygame.mouse.get_pos()
                        run = False
                        return self.check_action(pos)
                        
    
    def check_action(self, pos):
        """
        Verifie que le joueur a clique sur un bouton
        """
        for i in range (1,6):
            if 50 < pos[0] < 200 and 585-i*45 < pos[1] < 615-i*45:
                return i
        return self.get_action_menu()

    def destroy(self):
        """
        Detruit la fenetre
        """
        pygame.quit()
