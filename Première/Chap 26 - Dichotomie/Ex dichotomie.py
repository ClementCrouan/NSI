print("-------- Exercice 1 --------")
a = int(input("Nombre :"))
liste = [22, 53, 78, 100, 143, 177, 202]

for i in range (len(liste)):
    print('+',i)
    if liste[i] == a:
        print("La position du nombre rechercher est :" ,i+1)
