nb = int(input())
base = 2
reste = 0
i = 0
resultat = ""
while i < nb:
    reste = nb%base
    resultat = format(reste) + resultat
    nb = nb // base
print(resultat)
