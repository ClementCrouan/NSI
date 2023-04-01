def cube(n):
    cube = n**3
    return(cube)
nb = int(input("Choisissez un nombre suppérieur à 10:"))
i = 5
if nb > 10:
    while i <= nb:
        print(cube(i))
        i+=1
