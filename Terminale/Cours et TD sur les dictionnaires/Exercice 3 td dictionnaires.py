# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:51:04 2023

@author: ccrouan
"""

dico={}
tailles = ["XS","S","M","L","XL","XLL"]


for i in range(len(tailles)):
    if i == 0:
        dico[tailles[0]]=8
    else:
        dico[tailles[i]]