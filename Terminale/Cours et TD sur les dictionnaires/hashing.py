# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:21:18 2023

@author: ccrouan
"""

import hashlib

def hashing(text):
    m = hashlib.md5()
    text = text.encode('utf-8')
    m.update(text)
    return m.hexdigest()

T = open('lorem.txt','r')
texte = T.read()
print(texte)
print()
print(hashing(texte))