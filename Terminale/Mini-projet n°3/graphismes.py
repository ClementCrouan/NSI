import tkinter as t
import pygame as p  
from win32api import GetSystemMetrics

class Tkinter:

    def __init__(self) -> None:
        self.window = t.Tk()
        self.window.title("Le jeu de la vie")
        self.window.config(bg = "#23272a")
        screenRes = [GetSystemMetrics(0) - 20,GetSystemMetrics(1) - 20]
        self.window.geometry(str(screenRes[0]) + "x" + str(screenRes[1]))#87CEEB  <- cyan
        self.window.minsize(screenRes[0],screenRes[1])
        self.nothing = False
        self.option1 = False
        self.option2 = False
        self.option3 = False
    

    def menu(self):
        textButtons = ["Quitter", "Lancer une partie", "Boutique", "Changer de moteur graphique (jeu plus beau)"]
        self.buttons(textButtons)
    def choose_character(self):
        textButtons = ["Retour au menu", "Chimiste", "Nerd", "Commercial"]
        self.buttons(textButtons)
    def shop(self, rewards):
        textButtons = ["Retour au menu", "Flashbacks : "+ str(rewards.flashbacks), "Boussoles : " + str(rewards.boussoles), None]
        self.buttons(textButtons)
    def game(self, q, r1, r2, res, hint):
        textButtons = ["Retour au menu", r1, r2]
        textLabels = [q, None]
        if res is not None:    
            if res :
                textLabels[1] = "Victoire !"
            elif not res:
                textLabels[1] = "Défaite :("
        if hint > 0: 
            textButtons.append("Utiliser un flashback ("+str(hint)+" restants)")
        else: 
            textButtons.append("Plus de flashbacks")
        self.buttons(textButtons, textLabels)
    def warning(self):
        textLabels = ["Attention !!! Passer à l'interface graphique pygame améliorera votre expérience de jeux, mais nécessite l'installation préalable du module python.\nAssurez vous que cela soit fait avant de continuer, sinon votre jeux va planter.", None]
        textButtons = ["Retour au menu", None, None, "Continuer à vos risques et périls"]
        self.buttons(textButtons, textLabels)

    def buttons(self, textButtons, textLabels = [None, None]):
        bottom = t.Frame(self.window, bg = "#23272a")
        if textLabels[0] is not None :
            t.Label(bottom, text = textLabels[0], font= 18, width = 720, height = 10, bg = "#23272a", fg= "#FFFFFF").pack(pady = 4)
        if textButtons[1] is not None:
            t.Button(bottom, text = textButtons[1], font= 18, width = 40, bg = "#36393f", fg= "#FFFFFF", command = self.return_option1).pack(pady = 4)
        if textButtons[2] is not None:
            t.Button(bottom, text = textButtons[2], font= 18, width = 40, bg = "#36393f", fg= "#FFFFFF", command = self.return_option2).pack(pady = 4)
        if textLabels[1] is not None:
            t.Label(bottom, text = textLabels[1], font= 18, width = 720, bg = "#23272a", fg= "#FFFFFF").pack(pady = 4)
        if textButtons[3] is not None:
            t.Button(bottom, text = textButtons[3], font= 18, width = 40, bg = "#36393f", fg= "#FFFFFF", command = self.return_option3).pack(pady = 4)
        if textButtons[0] is not None:
            t.Button(bottom, text = textButtons[0], font= 18, width = 40, bg = "#36393f", fg= "#FFFFFF", command = self.return_nothing).pack(pady = 4)
        bottom.pack(side = "bottom", padx = 8, pady= 8)
        self.window.mainloop()


    def return_nothing(self):
        self.nothing = True 
        self.quit()
    def return_option1(self):
        self.option1 = True
        self.quit()
    def return_option2(self):
        self.option2 = True
        self.quit()
    def return_option3(self):
        self.option3 = True
        self.quit()


    def reset(self):
        self.nothing = False
        self.option1 = False
        self.option2 = False
        self.option3 = False
    def quit(self):
        self.window.destroy()

class Pygame:
    def __init__(self) -> None:
        p.init()
        self.window = p.display.set_mode((1280,720))
        p.display.set_caption('Morpion')
        self.window.fill(256)
        self.nothing = False
        self.option1 = False
        self.option2 = False
        self.option3 = False


    def menu(self):
        textButtons = ["Quitter","Changer de moteur graphique", "Boutique","Lancer une partie"]
        self.buttons(textButtons)
        option = self.click(len(textButtons))
        self.option(option)
    def choose_character(self):
        textButtons = ["Retour au menu","Commercial","Nerd","Chimiste"]
        self.buttons(textButtons)
        option = self.click(len(textButtons))
        self.option(option)
    def shop(self, rewards):
        textButtons = ["Retour au menu", "Boussoles : " + str(rewards.boussoles),"Flashbacks : " + str(rewards.flashbacks)]
        self.buttons(textButtons)
        option = self.click(len(textButtons))
        self.option(option)
    def game(self, q, r1, r2, res, hint):
        textButtons = ["Retour au menu","Utiliser un flashback ("+str(hint)+" restants)"]
        if r1 is not None:
            textButtons.append(r1)
        if r2 is not None:
            textButtons.append(r2)
        textLabels = [q]
        if res is not None:  
            if res :
                textLabels.append("Victoire !")
            elif not res:
                textLabels.append("Defaite :(")
        self.text(textLabels)
        self.buttons(textButtons)
        option = self.click(len(textButtons), 4)
        self.option(option)

    def text(self, text):
        font = p.font.SysFont("arial", 20)
        for i in range(len(text)):#affichage des boutons
            textAffiché = font.render(text[i], True, 'white')
            self.window.blit(textAffiché, (50,300-i*45))
        p.display.flip()
    def buttons(self, textButtons):
        font = p.font.SysFont("arial", 20)
        for i in range(len(textButtons)):#affichage des boutons
            text = font.render(textButtons[i], True, 'white')
            self.window.blit(text, (400,585-i*45))
            p.draw.rect(self.window, "white", (400,585-i*45, 285,35), 3)
        p.display.flip()
    def click(self, nbButtons, nbOptions = None):
        action = None
        while action is None:
            pos = self.__click_detection()
            if pos is None:
                return None
            action = self.__click_action(pos, nbButtons, nbOptions)
        return action
    def __click_detection(self):
        run = True
        while run :
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
                    pos = None
                if event.type == p.MOUSEBUTTONDOWN :
                        pos = p.mouse.get_pos()
                        run = False
        return pos
    def __click_action(self, pos, nbButtons, nbOptions = None):
        option = 0
        clickedOnButton = False
        for i in range (nbButtons):
            if 355 < pos[0] < 672 and 585-i*45 < pos[1] < 615-i*45:
                option = i
                clickedOnButton = True
        if not clickedOnButton:
            return None
        if option == 0:
            return 0
        elif nbOptions is not None:
            return nbOptions - option
        return nbButtons - option 
    

    def option(self,option):
        if option == 0:
            self.nothing = True
        elif option == 1:
            self.option1= True
        elif option == 2:
            self.option2 = True
        elif option == 3:
             self.option3 = True
        elif option is None:
            self.quit()
    def reset(self):
        self.nothing = False
        self.option1 = False
        self.option2 = False
        self.option3 = False
        p.display.update(self.window.fill([35,39,42]))
    def quit(self):
        p.quit()