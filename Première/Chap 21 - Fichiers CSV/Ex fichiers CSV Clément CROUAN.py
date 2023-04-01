from os import chdir, getcwd
import csv

fichier=open('fable.txt','w')
fichier.write("LE RENARD ET LES RAISINS\n\
Certain Renard gascon, d'autres disent normand,\n\
Mourant presque de faim, vit au haut  d'une treille\n\
    Des raisins mûrs apparemment,\n\
    Et couverts d'une peau vermeille.\n\
Le Galand en eut fait volontiers un repas ;\n\
    Mais comme il n'y pouvait point atteindre :\n\
Ils sont trop verts, dit-il, et bons pour des goujats.\n\
    Fit-il pas mieux que de se plaindre?")
fichier.close()

res = ""
fichier=open('fable 2.0.txt','r')
contenuFichier=fichier.read()
for n in range(len(contenuFichier)):
    if (n+1)%10 == 0:
        res += "*"
    res += contenuFichier[n]
fichier=open('fable 2.0.txt','w')
fichier.write(res)
fichier.close()

#Ex Titanic
fichier=open("titanic.csv","r")
reader=csv.DictReader(fichier,delimiter=",")
listRow = []
"""dico = {}
dico["Passengerld"] = 0
dico["Survived"] = 0
dico["Pclass"] = 0
dico["Name"] = 0
dico["Sex"] = 0
dico["Age"] = 0"""
for row in reader:
    listRow += row
print(listRow)
fichier.close()



