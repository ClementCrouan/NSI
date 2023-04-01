print("--------------------Ex n°1 a--------------------")
for n in range(5):
    print(n)
print("FIN")

print("--------------------Ex n°1 b--------------------")
for n in range(1,5):
    print(n)
print("FIN")

print("--------------------Ex n°1 c--------------------")
for n in range(1,5,2):
    print(n)
print("FIN")

print("--------------------Ex n°1 d--------------------")
for n in range(5,20,5):
    print(n)
print("FIN")

print("--------------------Ex n°1 e--------------------")
#for n in range(1,5):
    #Res += n
    #print(Res)
#print("FIN")
print("Erreur")

print("--------------------Ex n°1 f--------------------")
Res = 0

for n in range(1,3):
    Res += n
    print(Res)
print("FIN")

print("--------------------Ex n°1 g--------------------")
Res = 0

for letter in "bien":
    print(letter)

print("--------------------Ex n°2--------------------")
for loop in range(101):
    print("ceci est un test")

print("--------------------Ex n°3--------------------")
total = 0
nb = 0

for loop in range (total>10):
    nb += 1
    if nb%7 == 0:
        print(nb)
        total += 1
        
print("--------------------Ex n°4--------------------")
total = 0
nb = 0

for loop in range(total < 16):
    nb += 1
    if nb%2 == 0:
        print(2**total)
        total += 1

print("--------------------Ex n°5--------------------")
total = 0
nb = 0

for loop in range(total < 20):
    nb += 1
    if nb%7 == 0:
        if nb%2 == 0:
            print(nb)
            total += 1

print("--------------------Ex n°6--------------------")
text = input("Ecrivez une phrase :")
total = 0

for n in text:
    if n == "e":
        total += 1
print("il y a", total,"e dans votre phrase")
        
print("--------------------Ex n°7--------------------")
text = input("Ecrivez un mot :")
mot = ""

for n in text:
    if n == "a":
        mot += "x"
    else:
        mot += n
print(mot)

print("--------------------Ex n°8--------------------")
total = 0
nb = 1
total1 = 0

for i in range(1,64):
    total1 = total
    nb *= 2
    total += nb
print(total)


print("--------------------Ex n°9--------------------")
p1 = 1000
p2 = 1000
total = 0

for n in range(1970,2018):
    p2 *= 2000
total = p2/p1
print("Un ordinateur de 2018 est", total, "fois plus puissant qu'un ordinateur de 1970")

print("--------------------Ex n°10 a--------------------")
n=0

while n<4:
    print(n)
    n+=1
print("FIN")

print("--------------------Ex n°10 b--------------------")
while n<4:
    print(n)
    n+=1
#print("FIN")
print("Erreur")

print("--------------------Ex n°11--------------------")
n=1

while n<180:
    if n%7 == 0:
        print(n)
    n+=1

print("--------------------Ex n°12--------------------")
a = int(input("valeur choisie :"))

while a != 14:
    print("Perdu")
    a = int(input("valeur choisie :"))
print("Gagné")

print("--------------------Ex n°13--------------------")
totalInvites = 2
saveInvites = 0
nbInvitesHeure = 0
heures = 0
nbHeures = int(input("Nombre d'heures :"))

while heures < nbHeures:
    nbInvitesHeure = totalInvites - saveInvites
    saveInvites = totalInvites
    nbInvitesHeure *= 2
    totalInvites += nbInvitesHeure
    heures += 1
print("Il y aura", totalInvites,"invités.")

print("--------------------Ex n°14 a--------------------")
for letter in "bonjour":
        print(letter)

print("--------------------Ex n°14 b--------------------")
for letter in "bonjour":
    if letter == "j":
        break
    print(letter)

print("--------------------Ex n°14 c--------------------")
for letter in "bonjour":
    if letter == "j":
        continue
    print(letter)

print("--------------------Ex n°15 a--------------------")
i = 0

while i < 6:
    print(i)
    i += 1
print("fin")

print("--------------------Ex n°15 b--------------------")
i = 0

while True:
    if i < 6:
        print(i)
        i += 1
    else:
        break
print("fin")

print("--------------------Ex n°16--------------------")
text = input("ecrivez un mot")
resultat = ""

for n in text:
    if n == "a":
        continue
    if n == "g":
        break
    resultat += n
print(resultat)
