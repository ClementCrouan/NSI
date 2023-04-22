import binaryTree as b
import graphismes as g
import rewards as r
import save as s

class Main:
    def __init__(self, engine = True, rewards = r.Rewards(234234, 232323)) -> None:
        """Initialise les variables de la classe"""
        save = s.Save("money.csv")
        data = save.read()
        rewards = r.Rewards(int(data[0]),int(data[1]))
        self.rewards = rewards
        self.engine = engine#true = tkinter,  false = pygame
        if not self.engine:
            self.window = g.Pygame()

    def game(self, tree, previous = None):
        if self.engine:
            self.window = g.Tkinter()
        else:
            self.window.reset()
        if tree.right is not None :
            self.window.game(tree.question, tree.left.reponse, tree.right.reponse, tree.result, self.rewards.flashbacks)
        elif tree.left is not None :
            self.window.game(tree.question, tree.left.reponse, None, tree.result, self.rewards.flashbacks)
            
        else :
            self.window.game(tree.question, None, None, tree.result, self.rewards.flashbacks)
        if self.window.option1:
            self.game(tree.left, tree)
        elif self.window.option2 and tree.right is not None:
            self.game(tree.right, tree)
        elif self.window.option3 :
            if previous is None:
                self.game(tree)
            elif self.rewards.flashbacks > 0:
                print("ratio")
                self.rewards.add_flashbacks(-1)
                self.game(previous)
            else : 
                self.game(tree, previous)
        else : 
            self.menu()
        
    def choose_character(self):
        if self.engine:
            self.window = g.Tkinter()
        else:
            self.window.reset()
        self.window.choose_character()
        if not self.window.nothing :
            if self.window.option1:
                tree = b.character_chimie()
            elif self.window.option2 :
                tree = b.character_nerd()   
            elif self.window.option3:
                tree = b.character_commercial()   
            self.game(tree)
        else: 
            self.menu()

    def shop(self):
        if self.engine:
            self.window = g.Tkinter()
        else:
            self.window.reset()
        self.window.shop(self.rewards)
        if self.window.option1:
            self.rewards.add_flashbacks(1)
            self.shop()
        elif self.window.option2:
            self.rewards.add_boussoles(1)
            self.shop()
        else :
            self.menu()

    def switch_engine(self):
        if self.engine: 
            ALLTHEGAME_RATIOCLEMENT = Main(False, self.rewards)
            
        else: 
            self.window.quit()
            ALLTHEGAME_RATIOCLEMENT = Main(True, self.rewards)
        ALLTHEGAME_RATIOCLEMENT.menu()
    def check_switch_engine(self):
        if self.engine:
            self.window = g.Tkinter()
            self.window.warning()
            if self.window.option3:
                self.switch_engine()
            else:
                self.menu()
        else:
            self.switch_engine()

    def menu(self):
        if self.engine:
            self.window = g.Tkinter()
        else:
            self.window.reset()
        self.window.menu()
        if self.window.option1 :
            self.choose_character()
        elif self.window.option2 :
            self.shop()
        elif self.window.option3 :
            self.check_switch_engine()
        elif self.window.nothing:
            self.window.quit()
ALLTHEGAME_RATIOCLEMENT = Main()
ALLTHEGAME_RATIOCLEMENT.menu()