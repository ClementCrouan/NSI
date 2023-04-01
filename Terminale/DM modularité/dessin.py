import turtle as t
import MaussionAuxenceFigures as f

t.up()
t.goto(50,-60)
t.down()
f.rectangle(100,75,'red')

t.up()
t.goto(-80,20)
t.down()
f.triangle(85,'blue')

t.up()
t.goto(20,60)
t.down()
f.cercle(60,'green')

t.exitonclick()