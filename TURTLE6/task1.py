import turtle
import random

a = turtle.Pen()

def settings(width, speed, pencolor, fillcolor):
    a.width(width)
    a.speed(speed)
    a.color(pencolor, fillcolor)
    

def square(x):
    a.begin_fill()
    for i in range (4):
        a.forward(x)
        a.left(90)
    a.end_fill()
    a.up()
    a.goto(random.randint(-200,200),random.randint(-200,200))
    a.down()

settings(int(input("width: ")),
        int(input("speed: ")),
        input("pencolor: "),
        input("fill color: "))
        
for l in range (3):
    square(int(input("square_size: ")))

