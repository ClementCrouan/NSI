S = float(input("Le capital est égal à :"))
A = float(input("Le taux de rémunération est égal à :"))
while S < 1000:
    S = 1.03 * S
    A = A + 1
print(A)
