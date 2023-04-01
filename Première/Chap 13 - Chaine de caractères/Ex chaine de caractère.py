print("------------Ex n°1------------")
mot = input("Mot:")
pal = True

for i in range(len(mot)//2):
    if mot[i] != mot[-i]:
        print("Non")
        pal = False
        break
if pal == True:
    print("palindrome")

print("------------Ex n°2------------")
text = input("Mot:")
lettre = input("Lettre:")
pos = []

for i in range(len(text)):
    if text[i] == lettre:
        pos += [i]
        print("le", lettre, "est présent à la position:", i+1)
if pos == []:
    print("il n'y a pas de", lettre, "dans", text)
    
print("------------Ex n°3------------")
text = input("Mot:")
lettre = input("Lettre:")
res = ""

for i in text:
    if i == lettre:
        res += i
    else:
        res += "*"
print(res)

print("------------Ex n°4------------")
mot = input("Phrase:")
rang = int(input("Rang de décalage:"))
al = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
res = ""

for i in range(len(mot)):
    for t in range(len(al)):
        if mot[i] == al[t]:
            if t + rang <= 25:        
                res += str(al[t + rang])
            else:
                res += str(al[t + rang - 26])
            break
        elif t == 25:
            res += mot[i]
print(res)

print("------------Ex n°5------------")
for i in range(1,20):
    if 7 * i % 3 == 0:
        print(7 * i, end = "! ")
    else:
        print(7 * i, end = " ")
print()

print("------------Ex n°6------------")
secondes = int(input("Secondes:"))
minutes = secondes // 60
seconde = secondes % 60
heure = minutes // 60
minutes = minutes % 60
jour = heure // 24
heure = heure % 24
années = jour // 365
jour = jour % 365
mois = jour // 30
jour = jour % 30
print("il y a", années,"années", mois,"mois",jour,"jours",heure,"heures",minutes,"minutes",seconde,"secondes dans",secondes,"secondes")   

print("------------Ex n°7------------")
a = float(input("entrer le nombre a:"))
b = float(input("entrer le nombre b:"))
a = str(a)
b = str(b)
p1 = 0
p2 = 0
for i in range(len(a)):
    if a[i] == ".":
        p1 = len(a) - i
        
for i in range(len(b)):
    if b[i] == ".":
        p2 = len(b) - i
if p1 >= p2:
    a = float(a) * 10 ** p1
    b = float(b) * 10 ** p1
else:
    a = float(a1) * 10 ** p2
    b = float(b1) * 10 ** p2
r = a
q = 0

if b == 0:
    print("ERREUR cette division ne pas être efectué car le diviseur est égal à 0")
elif a != b:
    while r > b:
        r -= b
        q += 1
else:
    q = 1
    r = 0
    
if p1 >= p2:
    a = a / 10 ** p1
    b = b / 10 ** p1
    r = r / 10 ** p1
else:
    a = a / 10 ** p2
    b = b / 10 ** p2
    r = r / 10 ** p2

if b != 0:
    print("le quotient de",a,"par",b,"est",q,"et le reste est",r) 
