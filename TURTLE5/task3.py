import random
import turtle
t = turtle.Pen()
t.width(3)
t.speed(0)

for i in range (72):
    t.left(5)
    t.pencolor (random.random (), random.random (), random.random ())
    t.fillcolor (random.random (), random.random (), random.random ())
    t.begin_fill()
    t.circle(150)
    t.end_fill()

