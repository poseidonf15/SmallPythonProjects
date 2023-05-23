import turtle
a = turtle.Pen()
a.color("red","red")
a.right(45)
a.speed(0)

def circle2():
    a.begin_fill()
    a.circle(12.5)
    a.end_fill()

num = 0
while (num < 4):
    num2 = 0
    a.backward(25)
    while(num2 < 6):
        a.forward(50)
        a.right(90)
        circle2()
        a.left(90)
        num2 += 1

    a.up()
    a.goto(0,0)
    a.down()
    a.right(90)
    num += 1
    
