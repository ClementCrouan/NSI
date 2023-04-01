                        # -*- coding: utf-8 -*-
"""
Ex n°1.
"""
from random import randint
def jeu(n):
    x = 0
    nbSix = 0
    for loop in range(n):
        x = randint(1,6)
        if x == 6:
            nbSix += 1
    result = nbSix / n * 100
    return result, nbSix

print(jeu(10))
print(jeu(100))
print(jeu(1000))

#Ex n°2

def lettres(n):
    n = str(n)
    res = ""
    for i in n:
        res += i * 2
    return res
        
    
#Ex n°3 part 2
    
def dernier(n):
    n = str(n)
    first = n[0].lower()
    last = n[-1].lower()
    if first == last:
        return True
    else:
        return False
    
#Ex n°3 part 2
        
def double_text(n,f):
    n = str(n)
    f = str(f)
    firstWord1 = n[0].lower()
    firstWord2 = f[0].lower()
    lastWord1 = n[-1].lower()
    lastWord2 = f[-1].lower()
    if lastWord1 == lastWord2 and firstWord1 == firstWord2:
        return True
    else:
        return False
    
#Ex n°4

def commence(n):
    result = []
    for i in range(10, n):
        g = str(i)
        first = g[0]
        last = g[-1]
        if first == last:
            result += [int(i)]
    return result