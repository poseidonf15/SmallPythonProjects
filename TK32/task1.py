from tkinter import *
import time
import random

window = Tk()
window.geometry("500x500")
window.title("Canvas")
window.resizable(False, False)

ball = ""

canvas = Canvas(window, height  = 450, width = 450, relief = SOLID, bd = 1, bg = "white")
canvas.pack(expand = True)

y = 20
clicks = 0
total = []

def main():
    global ball
    ball = canvas.create_oval(175, 175, 275, 275, fill = "black")
    if (clicks > 4):
        canvas.delete(ball)
        num = 0
        for number in total:
            num += number
        num = num / 5 * 1000 // 1 / 1000
        canvas.create_text(225, 225,
                           anchor = "center",
                           font = "Arial 24",
                           text = f"Your reaction time: {num}")
        window.after(3000, restart)
    else:
        window.after(random.randint(3000, 7000), start)
    
def start():
    global start_time
    start_time = time.time()
    canvas.itemconfig(ball, fill = "green", outline = "green")
    canvas.tag_bind(ball, "<Button-1>", click)

def click(event):
    global y
    global start_time
    global score
    global clicks
    global total
    clicks += 1
    end_time = time.time()
    player_time = end_time - start_time
    seconds = player_time * 1000 // 1 / 1000
    total.append(seconds)
    score = canvas.create_text(40, y, font = "Arial 14", text = seconds)
    y += 20
    canvas.delete(ball)
    window.after(500, main)

def restart():
    global y
    global clicks
    global total
    canvas.delete("all")
    y = 20
    clicks = 0
    total = []
    main()

main()

window.mainloop()
