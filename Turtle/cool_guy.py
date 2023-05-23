from turtle import *
import turtle as t

t.speed(0)
t.hideturtle()

def drawning(x):
    for i in range (x//5*-4, x, x//5):
        t.penup()
        t.goto(0,x)
        t.pendown()
        t.goto(i,0)
    for i in range (x//5*4, x*-1, x//-5):
        t.penup()
        t.goto(x,0)
        t.pendown()
        t.goto(0,i)
    for i in range (x//5*4, x*-1, x//-5):
        t.penup()
        t.goto(-1*x,0)
        t.pendown()
        t.goto(0,i)
    for i in range (x//5*-4, x, x//5):
        t.penup()
        t.goto(0,-1*x)
        t.pendown()
        t.goto(i,0)
    t.exitonclick()

drawning(int(input("Enter the size parameter: ")))
