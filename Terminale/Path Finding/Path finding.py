# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:29:58 2023

@author: ccrouan
"""

import enum
import random

class TileType(enum.Enum):
    Land = 1
    River = 2
    Tree = 3
    
class Tile:
    def __init__(self,tileType, cost):
        self.TileType = tileType
        self.Cost = cost
        
class Land(Tile):
    def __init__(self, cost = 1):
        Tile.__init__(self, TileType.Land, cost)
    def __str__(self):
        return f"\033[92mL\033[00m"

class River(Tile):
    def __init__(self, cost = 3):
        Tile.__init__(self, TileType.River,cost)
    def __str__(self):
        return f"\033[96mR\033[00m"

class Tree(Tile):
    def __init__(self, cost = 99999999999):
        Tile.__init__(self, TileType.Tree,cost)
    def __str__(self):
        return f"\033[98mT\033[00m"

class Board:
    def __init__(self, width, height, player = None):
        self.Width = width
        self.Height = height
        self.Player = player
        self.Board = []
        for i in range(width):
            row = []
            for j in range(height):
                if 2 * i == j or 2 * i == j + 1:
                    row.append(River())
                else:
                    row.append(Land())
            self.Board.append(row)
        self.add_tree(15)
    def __str__(self):
        toReturn = ""
        for i in range(self.Width):
            for j in range(self.Height):
                tile = self.Board[i][j]
                toReturn += str(tile)
            toReturn += "\n"
        return toReturn
    
    def __repr__(self):
        return str(self)
    
    def path_to(self, x, y):
        open_list =  []
        closed_list = []
        startF = self.dist(self.Player.X, self.Player.Y, x,y)
        start = Node(self.Player.X, self.Player.Y, startF, 0, startF, None)
        open_list.append(start)
        
        while len(open_list) > 0:
            minF = self.__get_lowest_f(open_list)
            node = open_list[minF]
            if node.X == x and node.Y == y:
                return self.__reconstruct_path(node)
            open_list.pop(minF)
            closed_list.append(node)
            self.__visit_neighbours(open_list, closed_list, node, x, y)
        
            
    def add_tree(self, nb):
        while nb > 0:
            x = random.randint(0, self.Width - 1)
            y = random.randint(0, self.Height - 1)
            if self.Board[x][y].TileType != TileType.River:
                self.Board[x][y] = Tree()
                nb -= 1
        
            
    def __visit_neighbours(self, open_list, closed_list, node, x_goal, y_goal):
        for x in range(node.X - 1, node.X +2):
            for y in range(node.Y - 1, node.Y + 2):
                if x == node.X and y == node.Y and self.__valid_coord(x,y):
                    continue
                g = self.Board[x][y].Cost
                h = self.dist(x, y, x_goal, y_goal)
                neighbour = Node(x, y, g + h, g, h, node)
                
                if self.__contain(neighbour, open_list) or self.__contain(neighbour, closed_list):
                    continue
                open_list.append(neighbour)
    def __reconstruct_path(self, node):
        path = []
        while node.Parent is not None:
            path.insert(0, (node.X, node.Y))
            node = node.Parent
        return path
                
    def __contain(self, node, L):
        for n in L:
            if n.X == node.X and n.Y == node.Y and n.F <= node.F:
                return True
        return False
                
    def __valid_coord(self, x, y):
        return 0 <= x < self.Width and 0 <= y < self.Height
    
            
    def __get_lowest_f(self, L):
        mini = 0
        for i in range(1, len(L)):
            if L[i].F < L[mini].F:
                mini = i
        return mini
    
    def dist(self, x1, y1, x2, y2):
        x = x1 - x2
        y = y1 - y2
        return(x*x+y*y) ** 0.5
        
class Player:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class Node:
    def __init__(self, x, y, f, g, h, parent):
        self.X = x
        self.Y = y
        self.G = g
        self.H = h
        self.F = f
        self.Parent = parent
    
        

if __name__ == "__main__":
    player = Player(0, 0)
    board = Board(10,20, player)
    print(board)
    print(board.path_to(9,9))
            