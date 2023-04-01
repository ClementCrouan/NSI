class Morpion:
    def __init__(self):
        """
        Creation de la grille du morpion
        """
        self.infosGrille = [[0,0,0] for i in range(3)]

    def round(self, player, pos):
        """
        Pose pion sur case
        """
        self.infosGrille[pos[0]][pos[1]] = player
        
    def print_table_terminal(self):
        """
        Affiche la grille sur le terminal (version sans pygame)
        """
        print(' _ _ _')
        for i in range(3):
            for j in range(3):
                if self.infosGrille[i][j] == 1:
                    print('|x', end = '')
                elif self.infosGrille[i][j] == 2:
                    print('|o', end = '')
                else :
                    print('|_', end = '')
            print('|')

    def check_win(self):
        """
        Verifie si un joueur a gagne
        """
        for i in range(3):
            var = self.infosGrille[i][0]
            if var == self.infosGrille[i][1] and var == self.infosGrille[i][2] and var != 0:
                return var, [[i,0],[i,1],[i,2]] 
            var = self.infosGrille[0][i]
            if var == self.infosGrille[1][i] and var == self.infosGrille[2][i] and var != 0:
                return var, [[0,i],[1,i],[2,i]] 
        if self.infosGrille[1][1] != 0:
            if self.infosGrille[0][0] == self.infosGrille[1][1] and self.infosGrille[0][0] == self.infosGrille[2][2]:
                return self.infosGrille[0][0], [[0,0],[1,1],[2,2]] 
            elif self.infosGrille[0][2] == self.infosGrille[1][1] and self.infosGrille[0][2] == self.infosGrille[2][0]:
                return self.infosGrille[0][2], [[0,2],[1,1],[2,0]]
        return 0, 0

    def check_case(self, pos):
        """
        Verifie s'il y a déjà un pion sur la case
        """
        if self.infosGrille[pos[0]][pos[1]] == 0: 
            return True
        return False
