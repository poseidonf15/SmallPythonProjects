alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_encrypt(plaintext, key):
    global alphabet
    key %= 26
    ciphertext = ""
    for i in range (0, len(plaintext)):
        if (plaintext[i].isalpha()):
            if (plaintext[i].isupper()):
                index = alphabet.find(plaintext[i].lower())
                if (index + key > 25):
                    new_index = key - (26 - index)
                else:
                    new_index = index + key
                new_letter = alphabet[new_index]
                ciphertext += new_letter.upper()
            else:
                index = alphabet.find(plaintext[i])
                if (index + key > 25):
                    new_index = key - (26 - index)
                else:
                    new_index = index + key
                new_letter = alphabet[new_index]
                ciphertext += new_letter
        else:
            ciphertext += plaintext[i]
    return ciphertext

def decrypt(plaintext, key):
    global alphabet
    key %= 26
    ciphertext = ""
    for i in range (0, len(plaintext)):
        if (plaintext[i].isalpha()):
            if (plaintext[i].isupper()):
                index = alphabet.find(plaintext[i].lower())
                if (index + key > 25):
                    new_index = key - (26 - index)
                else:
                    new_index = index + key
                new_letter = alphabet[new_index]
                ciphertext += new_letter.upper()
            else:
                index = alphabet.find(plaintext[i])
                if (index + key > 25):
                    new_index = key - (26 - index)
                else:
                    new_index = index + key
                new_letter = alphabet[new_index]
                ciphertext += new_letter
        else:
            ciphertext += plaintext[i]
    return ciphertext

num = int(input())
x = caesar_encrypt(input(), num)
print (x)
print (decrypt(x, 26 - num))

    
