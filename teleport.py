from tkinter import *
import random
import time

window = Tk()
window.geometry("400x400")

def teleport():
    global start_time
    end_time = time.time()
    user_time = end_time - start_time
    start_time = time.time()
    if (user_time > 1):
        button.config(text = "You lose!", state = DISABLED)
    button.place(x  = random.randint(0,200), y = random.randint(0,200))
    start_time = time.time()

start_time = time.time()
button = Button(bg = "black", width = 15, command = teleport)
button.place(y  = random.randint(0,200), x = random.randint(0,200))


window.mainloop()
