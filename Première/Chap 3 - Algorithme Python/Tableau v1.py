def bin(s):
    reste = 0
    nbResultat = 0
    resultat = ""
    nbZ = 0
    while i < s:
        reste = s%2
        if resultat != "":
            resultat = format(reste) + " " + resultat
        else:
            resultat = format(reste)
        s = s // 2
        nbResultat += 1
    nbZ = 8 - nbResultat
    for loop in range(nbZ):
        if resultat != "":
            resultat = "0 " + resultat
        else:
            resultat = "0"
    return(resultat)

def hexad(s):
    reste = ""
    nbResultat = 0
    resultat = ""
    nbZ = 0
    while i < s:
        reste = format(s%16)
        if reste == "10":
            reste = "A"
        if reste == "11":
            reste = "B"
        if reste == "12":
            reste = "C"
        if reste == "13":
            reste = "D"
        if reste == "14":
            reste = "E"
        if reste == "15":
            reste = "F"
        resultat = format(reste) + resultat
        nbResultat += 1
        s = s // 16
    nbZ = 2 - nbResultat
    for loop in range(nbZ):
            resultat = "0" + resultat
    return(resultat)

i = 0
dec = 0
binaire = ""
hexa = ""
txt = ""

##Contour du tableau
for loop in range(30):
    print("-", end="")
print()
print("|dec | b i n a i r e  | hexa |")
print("|", end="")
for loop in range(28):
    print("-", end="")
print("|")

for loop in range(256):
    txt = format(dec) + "|"
    if dec < 10:
        print("|  ", txt, end=" ")
        binaire = bin(dec)
    elif dec < 100:
        print("| ", txt,end=" ")
        binaire = bin(dec)
    else:
        print("|", txt, end=" ")
        binaire = bin(dec)
    print(binaire, end="|")
    
    hexa = "0x " + hexad(dec)
    print(hexa,"|")
    dec += 1
