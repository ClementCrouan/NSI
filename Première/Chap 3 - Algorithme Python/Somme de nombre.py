nb = 0
resultat = 0
n = 0
o = 0
while nb <= 1000:
    n = nb%3
    o = nb%5
    if (n != 0 & o != 0):
        resultat += nb
    nb += 1
print(nb)
        
    
