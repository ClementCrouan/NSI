Dico1 = { "Table":"Meuble composé d'un plateau horizontal reposant sur un ou plusieurs pieds ou supports. \
Servant notamment pour les repas" , \
"Chaise":"Siège à dossier, sans bras" , \
"Fauteuil":"Siège à dossier et à bras pour une personne" , \
"Commode":"Meuble à hauteur d'appui garni, le plus souvent, de tiroirs"}
 
Dico2 = {"Imprimante":"Matériel d'impression" ,\
"Routeur":"matériel de routage" ,\
"NAS":"Matériel de stockage" ,\
"PC":"Ordinateur personnel" }
 
def plus_longue_definition(dico):
    m = ""
    l = 0
    for (mot,definition) in dico.items():
        if len(dico[mot]) > l:
            l = len(dico[mot])
            m = mot
            print(m,"-",l)
    return m
        
# Jeu d'essai
print("Pass test1 --> ",plus_longue_definition(Dico1)=="Table")
print("Pass test2 --> ",plus_longue_definition(Dico2)=="Imprimante")

Dico = {"chat":"cat","chien":"dog","sous":"under","soleil":"sun","le":"the","et":"and"}

def translate(dico,phrase):
    l = []
    t = -1
    #phrase = split(phrase)
    res = ""
    
    for i in range (len(phrase)):
        if phrase[i] == " ":
            mot = ""
            for n in range (t + 1, i):
                mot += phrase[n]
            l += [mot]
            t = i
    
    for j in range (len(l)):
        trad = False
        for (mot, traduction) in dico.items():
            if mot == l[j] and trad != True:
                res += traduction + " "
                trad = True
        if trad == False:
            res += "2" + l[j] + "2" + " "
    
    return res
    
print(translate(Dico, "J'ai un chat et un chien qui dorment sous le soleil "))
