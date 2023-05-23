import turtle
import random

a = turtle.Pen()

a.speed(0)

def stars(n,m):
    a.pencolor(random.random (), random.random (), random.random ())
    for i in range(n):
        a.forward(m / 2)
        a.backward(m / 2)
        a.left(360 / n)

for l in range(50):
    a.up()
    a.goto(random.randint(-200,200), random.randint(-200,200))
    a.down()
    stars(random.randint(6,20),random.randint(20,40))
    





