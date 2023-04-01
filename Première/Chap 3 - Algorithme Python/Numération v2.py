nb = int(input("Quel nombre voulez-vous convertir?"))
base = int(input("Sur quel base voulez-vous le convertir?"))
nbD = 0
nbZ = 0
nbResultat = 0
reste = ""
i = 0
resultat = ""
while i < nb:
    reste = format(nb%base)
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
    resultat = reste + resultat
    nbResultat += 1
    nbD = nbResultat%4
    if base == 2:
        if nbD == 0:
            resultat = " " + resultat
    nb = nb // base
nbZ = 4 - nbResultat
if base == 2:
    for loop in range(nbZ):
        resultat = "0" + resultat
print(resultat)
