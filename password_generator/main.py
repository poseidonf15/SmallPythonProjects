import interface
import generator
from generator import generate_password

def generate():

    interface.password_box.delete(0, "end")
    for i in range (5):
        password = generate_password(interface.lowercase.get(),interface.uppercase.get(), interface.numbers.get(), interface.symbols.get(),
                                     interface.entry1.get(), interface.entry2.get(), interface.entry3.get(), interface.entry4.get())
        interface.password_box.insert(0, password)

interface.generate_password.config(command = generate)

interface.window.mainloop()
