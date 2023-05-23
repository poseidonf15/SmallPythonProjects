import turtle
a = turtle.Pen()
a.speed(0)

num = 1
num2 = 120

while (num2 > 0):
    i2 = 0
    a.left(num)
    
    while (i2 < 4):
        
        i2 +=1
        a.forward(num2)
        a.left(90)

    num += 1
    num2 -= 5
