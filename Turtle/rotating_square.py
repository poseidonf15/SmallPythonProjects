import turtle as t

t.speed(0)
t.hideturtle()

for l in range(1,100):
    for i in range (4):
        t.forward(l*5)
        t.right(90)
    t.right(5)

t.exitonclick()