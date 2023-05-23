from tkinter import *
from tkinter import messagebox
import random
import time

window = Tk()
window.geometry("550x300")
window.title("Schulte")

numbers_in_order = ""
game_frame = ""
start_time = ""

def restart():
    global start_time
    global game_frame
    global numbers_in_order
    ready = messagebox.askquestion("Are you ready", """After clicking "Yes" the time will start""")
    if (ready):
        greeting_frame.forget()
        numbers_in_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(random_numbers)
        game_frame = LabelFrame(relief = FLAT)
        game_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, padx = 115 , pady = 13)

        x = 0
        for i in range (0, 3):
            for l in range (0, 3):
                number = Button(game_frame, font=('Arial', 15, 'bold'), width=8, height=3, text=random_numbers[x])
                number.grid(row = i, column = l)
                window.bind("<Button-1>", click)
                x += 1
        start_time = time.time()

def click(event):
    global start_time
    global game_frame
    global numbers_in_order
    if (numbers_in_order[0] == int(event.widget["text"])):
        event.widget.unbind("<Button-1>")
        (event.widget).config(bg = "green", state = (DISABLED))
        numbers_in_order = numbers_in_order[1:]
        if numbers_in_order[0] == 10 :
            end_time = time.time()
            user_time = end_time - start_time
            messagebox.showinfo("Congratulations!", f"You won! \nYour time: {user_time * 100 // 1 / 100}")
            game_frame.destroy()
            greeting_frame.pack(expand = True)
    else:
        messagebox.showerror("Oops", "You made a mistake! Starting over...")
        game_frame.destroy()
        restart()

def Esc(event):
    answer = messagebox.askquestion("The question", "Are you sure you want to restart the game?")
    if (answer):
        game_frame.destroy()
        restart()

greeting_frame = LabelFrame(relief = FLAT)
greeting_frame.pack(side = TOP, padx = 15)

label = Label(greeting_frame, text = """Schulte is a simple game that develops peripheral vision, reading speed and reaction!
Rules of the game:
1. A player have to pick all the numbers in order from 1 to 9 faster than anyone else.
2. If a player makes a mistake, the game starts over again.
3. The winner is the one who copes with the task the fastest.
""", font = ("Arial", 10), justify = LEFT)
label.pack(side = TOP, pady = 50)

button = Button(greeting_frame, text = "Start the game", command = restart)
button.pack(side = TOP)

window.bind("<Escape>", Esc)

window.mainloop()
