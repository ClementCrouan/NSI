# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:25:40 2023

@author: ccrouan
"""


def chiffrage(M):
    chiffree = ""
    for c in M:
        resultat = (3 * ord(c) - 61) % 91 + 33
        c1 = chr(resultat)
    
        if resultat % 2 == 0:
            resultat2 = (2 * ord(c) - 31) % 91 + 33
            c2 = chr(resultat2)
            chiffree += c1 + c2
        else:
            resultat2 = (2 * ord(c) - 32) % 91 + 33
            c2 = chr(resultat2)
            resultat3 = (3  * ord(c) - 60) % 91 + 33
            c3 = chr(resultat3)
            chiffree += c1 + c2 + c3
    
    return chiffree
    

print(chiffrage("informatique"))