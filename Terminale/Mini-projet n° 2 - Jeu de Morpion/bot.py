from random import randint

class Bot: 
    def __init__(self, difficulty = '2', active = False, NoPlayer = 2):
        """
        Cree le bot avec comme parametres :
            difficultee(1 ou 2)/activation(bot on/off)/tour(joueur 1/2)
        """
        self.difficulty = difficulty
        self.active = active
        self.NoPlayer = NoPlayer

    def play(self, tour, infosGrille):
        """
        Fais jouer le bot
        """
        if self.difficulty == 1: #choisi le bon programme en fonction de la difficultee du bot
            return self.clement()
        elif self.difficulty == 2:
            return self.medium(infosGrille)
        else :
            return self.hard(tour, infosGrille)

    def clement(self):
        """
        bot facile, action aleatoires
        """
        a = randint(0,2)
        b = randint(0,2)
        return (a,b)

    def medium(self, infosGrille):
        """
        bot difficile
        """
        if self.NoPlayer == 1:
            player = self.winnable(infosGrille, 2)
        else:
            player = self.winnable(infosGrille, 1)
        if player != 0:
            return player
        else:
            a = randint(0,2)
            b = randint(0,2)
            return (a,b)

    def hard(self, tour, infosGrille):
        """
        bot imossible
        """
        if tour == 1:
            return (1,1)
        elif tour == 2 or tour == 3:
            if infosGrille[1][1] == 0:
                return (1,1)
            else:
                sidePos = [[0,0],[0,2],[2,0],[2,2]]
                i = randint(0,3)
                return sidePos[i]
        else:
            bot = self.winnable(infosGrille, self.NoPlayer)
            if self.NoPlayer == 1:
                player = self.winnable(infosGrille, 2)
            else:
                player = self.winnable(infosGrille, 1)
            if bot != 0:
                return bot
            elif player != 0:
                return player
            else:
                a = randint(0,2)
                b = randint(0,2)
                return (a,b)
            
    def winnable(self, infosGrille, NoPlayer):
        for i in range(3):
            pos = self.line(infosGrille,NoPlayer,i)
            if pos != 0:
                return pos
            pos = self.colonne(infosGrille,NoPlayer,i)
            if pos != 0:
                return pos
        pos = self.diago1(infosGrille,NoPlayer)
        if pos != 0:
            return pos
        pos = self.diago2(infosGrille,NoPlayer)
        if pos != 0:
            return pos
        return 0
    
    def line(self, infosGrille, NoPlayer, i):
        isAligned = 0
        pos = []
        if NoPlayer == infosGrille[i][1] or infosGrille[i][1] == 0:
            if infosGrille[i][1] == 0:
                isAligned += 1
                pos = [i,1]
            if NoPlayer == infosGrille[i][2] or infosGrille[i][2] == 0:
                if infosGrille[i][2] == 0:
                    isAligned += 1
                    pos = [i,2]
                if infosGrille[i][0] == 0 and isAligned == 0:
                    pos = [i,0]
                    return pos
                elif infosGrille[i][0] == NoPlayer and isAligned != 2:
                    return pos
        return 0
                
    def colonne(self, infosGrille, NoPlayer, i):
        isAligned = 0
        pos = []
        if NoPlayer == infosGrille[1][i] or infosGrille[1][i] == 0:
            if infosGrille[1][i] == 0:
                isAligned += 1
                pos = [1,i]
            if NoPlayer == infosGrille[2][i] or infosGrille[2][i] == 0:
                if infosGrille[2][i] == 0:
                    isAligned += 1
                    pos = [2,i]
                if infosGrille[0][i] == 0 and isAligned == 0:
                    pos = [0,i]
                    return pos
                elif infosGrille[0][i] == NoPlayer and isAligned != 2:
                    return pos
        return 0
            
    def diago1(self, infosGrille, NoPlayer):
        isAligned = 0
        pos = []
        if infosGrille[1][1] == 0 or infosGrille[1][1] == NoPlayer:
            if infosGrille[1][1] == 0:
                isAligned += 1
                pos = [1,1]
            if infosGrille[2][2] == 0 or infosGrille[2][2] == NoPlayer:
                if infosGrille[2][2] == 0:
                    isAligned += 1
                    pos = [2,2]
                if infosGrille[0][0] == 0 and isAligned == 0:
                    pos = [0,0]
                    return pos
                elif infosGrille[0][0] == NoPlayer and isAligned != 2:
                    return pos
        return 0

    def diago2(self, infosGrille, NoPlayer):
        isAligned = 0
        pos = []
        if infosGrille[1][1] == 0 or infosGrille[1][1] == NoPlayer:
            if infosGrille[1][1] == 0:
                isAligned += 1
                pos = [1,1]
            if infosGrille[0][2] == 0 or infosGrille[0][2] == NoPlayer:
                if infosGrille[0][2] == 0:
                    isAligned += 1
                    pos = [0,2]
                if infosGrille[2][0] == 0 and isAligned == 0:
                    pos = [2,0]
                    return pos
                elif infosGrille[2][0] == NoPlayer and isAligned != 2:
                    return pos
        return 0
