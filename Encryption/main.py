import interface
from ciphers import caesar_encrypt
from ciphers import atbash_encrypt
from ciphers import caesar_affine_encrypt

currentcipher = 0
interface.ciphername.config(padx = 97)

def change_cipher():
    global currentcipher
    currentcipher = interface.choice.get()
    if (currentcipher == 0):
        interface.ciphername.config(text = "Caesar's cipher:")
        interface.keybox.config(state = "normal")
        interface.key2box.config(state = "disabled")
        interface.label2.config(state = "normal")
        interface.label3.config(state = "disabled")
        interface.ciphername.config(padx = 97)
    elif (currentcipher == 1):
        interface.ciphername.config(text = "Atbash cipher:  ")
        interface.keybox.config(state = "disabled")
        interface.key2box.config(state = "disabled")
        interface.label2.config(state = "disabled")
        interface.label3.config(state = "disabled")
        interface.ciphername.config(padx = 97)
    else:
        interface.ciphername.config(text = "Caesar's affine cipher:")
        interface.keybox.config(state = "normal")
        interface.key2box.config(state = "normal")
        interface.label2.config(state = "normal")
        interface.label3.config(state = "normal")
        interface.ciphername.config(padx = 70)

interface.radiocaesar.config(command = change_cipher)
interface.radioatbash.config(command = change_cipher)
interface.radiocaesar_affine.config(command = change_cipher)
interface.choice.set(0)

def encrypt():
    global currentcipher
    if (currentcipher == 0):
        plaintext = interface.plaintextbox.get()
        key = int(interface.keybox.get())
        interface.ciphermessage.config(text = caesar_encrypt(plaintext, key))
        interface.plaintextbox.delete(0, "end")
        interface.keybox.delete(0, "end")
    elif (currentcipher == 1):
        plaintext = interface.plaintextbox.get()
        interface.ciphermessage.config(text = atbash_encrypt(plaintext))
        interface.plaintextbox.delete(0, "end")
    else:
        plaintext = interface.plaintextbox.get()
        key = int(interface.keybox.get())
        key2 = int(interface.key2box.get())
        interface.ciphermessage.config(text = caesar_affine_encrypt(plaintext, key, key2))
        interface.plaintextbox.delete(0, "end")
        interface.keybox.delete(0, "end")
        interface.key2box.delete(0, "end")

interface.encryptB.config(command = encrypt)

interface.window.mainloop()




