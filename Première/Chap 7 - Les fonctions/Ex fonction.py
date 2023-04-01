from turtle import *
speed(100)
print("----------Ex n°1----------")
up()
goto(-200,200)
down()
for loop in range(5):
    forward(400)
    up()
    left(-90)
    forward(40)
    down()
    left(90)
    backward(400)
    up()
    left(90)
    backward(40)
    down()
    left(-90)
forward(400)

from turtle import *
print("----------Ex n°2----------")
up()
goto(-100,100)
down()
côté = 200
for loop in range(20):
    for loop in range(4):
        forward(côté)
        left(-90)
    côté-=10

from turtle import *
print("----------Ex n°3----------")
left(90)
up()
goto(-100,100)
down()
begin_fill()
fillcolor("cyan")
circle(100,180)
left(90)
forward(200)
right(105)
end_fill()
begin_fill()
fillcolor("orange")
forward(387)
right(150)
forward(387)
hideturtle()
end_fill()
   
print("----------Ex n°1 a----------")
def repet(mot):
    for loop in range(10):
        print(mot)


repet("bonjour")

print("----------Ex n°1 b----------")
def repets(mot):
	for loop in range(10):
		print(mot)
userWord = input("Ecriver un mot :")
repets(userWord)
