import turtle as t

def rectangle(L,l,color):
    color1 = t.pencolor()
    t.pencolor(color)
    for i in range(2):
        t.forward(L)
        t.right(90)
        t.forward(l)
        t.right(90)
    formule(L,l*L)
    t.pencolor(color1)

def triangle(l,color):
    color1 = t.pencolor()
    t.pencolor(color)
    for i in range(3):
        t.forward(l)
        t.right(120)
    formule(l,l**2/2)
    t.pencolor(color1)

def cercle(r,color):
    color1 = t.pencolor()
    t.pencolor(color)
    t.circle(r)
    formule(r, 3.14*r**2)
    t.pencolor(color1)

def formule(l, f):
    t.up()
    t.forward(l)
    t.down()
    A = 'aire = ' + str(f)
    t.write(A)
    t.up()
    t.backward(l)
    t.down()