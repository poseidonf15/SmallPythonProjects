from tkinter import *
import time
import random

window = Tk()
window.geometry("500x500")
window.title("Click the ball")
window.resizable(False, False)

ball = ""
after = ""

canvas = Canvas(window, height  = 450, width = 450, relief = SOLID, bd = 1, bg = "white")
canvas.pack(expand = True)

points = 0
score = canvas.create_text(10, 20, anchor = W, font = "Arial 24", text = points)

def new_ball():
    global after_id
    global x
    global y
    global ball
    after_id = window.after(1000, lose)
    ball = canvas.create_oval(x, y, x + 50, y + 50,
                                             fill = f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")

def click(event):
    global after_id
    global points
    global x
    global y 
    global ball
    x = random.randint(0, 405)
    y = random.randint(0,405) 
    if ball in canvas.find_overlapping(event.x, event.y, event.x + 50, event.y + 50):
        window.after_cancel(after_id)
        points += 1
        canvas.itemconfig(score, text = points)
        canvas.delete(ball)
        new_ball()
    else:
        canvas.itemconfig(score, text = points)

def lose():
    global x
    global y
    global after_id
    global points
    x = random.randint(0, 405)
    y = random.randint(0,405) 
    window.after_cancel(after_id)
    points -= 1
    canvas.itemconfig(score, text = points)
    canvas.delete(ball)
    new_ball()

x = random.randint(0, 405)
y = random.randint(0,405)  
new_ball()
canvas.bind("<Button-1>", click)










