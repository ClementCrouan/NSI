nb = 11
n = 0
i = 0
e = 0
while 0 != nb%10:
    nb = int(input("Entrez le nombre:"))
    i+= 1
    if nb > n & 0 != nb%10:
        n = nb
        e = i
print("Le plus grand nombre est",n, "c'est le nombre n°",e)
    
