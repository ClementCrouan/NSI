# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:37:51 2022

@author: ccrouan
"""


from Stylo import *

pen = Stylo("Rouge")
print(pen.getCouleur())
pen.setCouleur("Bleu")
print(pen.reservoir.getCouleur())