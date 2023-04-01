print("Question n°1")
#Fonction retournant le prix avec la promo A
#La fonction requiert deux float représentant le prix du parfum un et du parfum deux
def promoA(prix1, prix2):
    if prix1 >= prix2:
        prix2 /=  2
    elif prix2 > prix1:
        prix1 /= 2
    return(prix1 + prix2)

#Affiche les deux exemples
print("pour prix1 = 20 et prix2 = 10:", promoA(20,10))
print("pour prix1 = 10 et prix2 = 20:", promoA(10,20))

print("Question n°2")
#Fonction retournant le prix avec la promo B
#La fonction requiert deux float représentant le prix du parfum un et du parfum deux
def promoB(prix1, prix2):
    return((prix1 + prix2) * 0.8)
#Affiche les deux exemples
print("pour prix1 = 20 et prix2 = 10:", promoB(20,10))
print("pour prix1 = 10 et prix2 = 20:", promoB(10,20))

print("Question n°3")
#Variable contenant le prix du premier parfum
p1 = float(input("prix du parfum numéro 1:"))
#Variable contenant le prix du deuxième parfum
p2 = float(input("prix du parfum numéro 2:"))
#Variable constante représentant l'argent dont dispose Nicolas
argent = 50
#Variable contenant le nom de la promo la plus avantageuse
promo = ""

#Affiche le prix avec la promo A
print("Avec la promo A:", promoA(p1,p2))

#Affiche le prix avec la promo B
print("Avec la promo B:", promoB(p1,p2))

#Affiche la promo la plus rentable
#Et déféni la variable "promo"
if promoA(p1,p2) < promoB(p1,p2):
    print("La promo A est plus avantageuse")
    promo = "A"
elif promoA(p1,p2) > promoB(p1, p2):
    print("La promo B est plus avantageuse")
    promo = "B"
elif promoA(p1,p2) == promoB(p1,p2):
    print("La promo A et la promo B apporte les mêmes avantages")

#Détermine si Nicolas peut acheter les deux parfums
if promo == "A":
    if promoA(p1,p2) <= argent:
        print("Nicolas poura acheter les deux parfum")
    else:
        print("Nicolas ne poura pas acheter les deux parfum")
elif promo == "B":
    if promoB(p1,p2) <= argent:
        print("Nicolas poura acheter les deux parfum")
    else:
        print("Nicolas ne poura pas acheter les deux parfum")
else:
    if promoA(p1,p2) <= argent:
        print("Nicolas poura acheter les deux parfum")
    else:
        print("Nicolas ne pourra pas acheter les deux parfum")
