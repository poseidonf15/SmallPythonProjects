import turtle
a = turtle.Pen()

num = 0

while (num < 3):
    
    num = num + 1
    
    a.color("green","green")
    a.begin_fill()

    num2 = 0
    a.left(60)

    while (num2 < 3):
        
        num2 = num2 + 1

        a.forward(50)
        a.left(120)

    a.end_fill()

    a.color("red","red")
    a.begin_fill()
    
    num2 = 0
    a.left(60)

    while (num2 < 3):
        
        num2 = num2 + 1

        a.forward(50)
        a.left(120)

    a.end_fill()
