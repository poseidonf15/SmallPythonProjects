import turtle
a = turtle.Pen()
a.speed(0)

def x():
    num2 = 0
    while (num2 < 5):
        num2 += 1
        a.forward(100)
        a.left(72)
    

i = 100
num = 0
while (i > 0):
    
    a.left(num)
    x()
    num +=5

    

    
    
    
