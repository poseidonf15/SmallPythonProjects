import turtle
import random
a = turtle.Pen()
a.speed(0)
a.width(3)

def square(x,y):
    a.up()
    a.goto(x,y)
    a.down()
    i = (random.random (), random.random (), random.random ())
    a.color(i,i)
    a.begin_fill()
    a.circle(random.randint(5,50))
    a.end_fill()

turtle.onscreenclick(square)
