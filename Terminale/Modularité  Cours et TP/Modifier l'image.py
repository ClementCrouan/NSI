# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:43:35 2022

@author: ccrouan
"""
from PIL import Image, ImageDraw
import numpy as np

print("------Nuance------")
# On charge l'image et on la transforme en tableau contenant les couleurs
image_entrée = Image.open("Info/Lenna.jpg")
image = np.asarray(image_entrée)
nb_lignes,nb_colonnes,_ = image.shape
# Partie à compléter
image_sortie = np.copy(image)
for ligne in range(nb_lignes):
    for col in range(nb_colonnes):
        r = image_sortie[ligne, col] * (1, 0, 0)
        g = image_sortie[ligne, col] * (0, 1, 0)
        b = image_sortie[ligne, col] * (0, 0, 1)
        luminance = (0.2126 * r[0] + 0.7152 * g[1] + 0.0722 * b[2])
        image_sortie[ligne,col] = (luminance, luminance, luminance)
# On sauvegarde les images pour pouvoir les afficher
Image.fromarray(image).save("Info/image_entree.png")
Image.fromarray(image_sortie).save("Info/image_sortie.png")