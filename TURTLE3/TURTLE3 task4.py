import turtle
a = turtle.Pen()
import random
x = 0
k = 100
a.width(2)
while (x < 10):
    a.fillcolor(random.random(), random.random(), random.random())
    a.pencolor(random.random(), random.random(), random.random())
    a.begin_fill()
    a.circle(k)
    a.end_fill()
    k = k - 10
    x = x + 1
