from tkinter import *
import random

window = Tk()
window.title("tk")
window.geometry("250x350")

alarmsnum = 10

def generate_alarms():
    global alarmsnum
    alarmsnum = 10
    alarmbox.delete(0, END)
    alarms = []
    a = 0
    b = 5
    for i in range (10):
        num = random.randint(a,b)
        if (num < 10):
            clock = "07:0" + str(num)
        else:
            clock = "07:" + str(num)
        alarms.append(clock)
        a += 6
        b += 6
    alarmbox.insert(END, *alarms)
    size.config(text = sizex + str(alarmsnum))

def delete_alarms():
    global alarmsnum
    indexes = alarmbox.curselection()
    indexesSort = sorted(indexes, reverse = True)
    for index in (indexesSort):
        alarmsnum -= 1
        alarmbox.delete(index)
    size.config(text = sizex + str(alarmsnum))
    

title = Label(text = "Alarmclock")
title.pack(side = TOP, pady = 10)

sizex = "Number of alarmclocks: "
size = Label(text = "Number of alarmclocks: ")
size.pack(side = TOP, pady = 10)

alarmbox = Listbox(width = 30, height = 10, justify = CENTER, selectmode = EXTENDED)
alarmbox.pack(side = TOP, pady = 10)

randombutton = Button(text = "Random alarm", width = 30, command = generate_alarms)
randombutton.pack(side = TOP)

deletebutton = Button(text = "Delete an alarm", width = 30, command = delete_alarms)
deletebutton.pack(side = BOTTOM, pady = 10)

window.mainloop()
