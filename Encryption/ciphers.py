alphabet = "abcdefghijklmnopqrstuvwxyz"

def calculate_divisors(alphabet):
    divisors = []
    for i in range (2, len(alphabet) + 1):
        if (len(alphabet) % i == 0):
            divisors.append(i)
    return divisors

def caesar_encrypt(plaintext, key):
    global alphabet
    key %= 26
    ciphertext = ""
    for i in range (0, len(plaintext)):
        if (plaintext[i].isalpha()):
            if (plaintext[i].isupper()):
                index = alphabet.find(plaintext[i].lower())
                new_index = (index + key) % len(alphabet)
                new_letter = alphabet[new_index]
                ciphertext += new_letter.upper()
            else:
                index = alphabet.find(plaintext[i])
                new_index = (index + key) % len(alphabet)
                new_letter = alphabet[new_index]
                ciphertext += new_letter
        else:
            ciphertext += plaintext[i]
    return ciphertext

def atbash_encrypt(plaintext):
    global alphabet
    ciphertext = ""
    for letter in plaintext:
        if (letter.isalpha()):
            if (letter.isupper()):
                index = alphabet.find(letter.lower())
                new_letter = alphabet[26 - index - 1]
                ciphertext += new_letter.upper()
            else:
                index = alphabet.find(letter)
                new_letter = alphabet[26 - index - 1]
                ciphertext += new_letter
        else:
            ciphertext += plaintext[i]
    return ciphertext

def caesar_affine_encrypt(plaintext, key, key2):
    global alphabet

    divisors = calculate_divisors(alphabet)
    for y in range (len(divisors)):
        if (key2 % divisors[y] == 0):
            return "wrong key"
    else:
        key %= 26
        ciphertext = ""
        for i in range (0, len(plaintext)):
            if (plaintext[i].isalpha()):
                if (plaintext[i].isupper()):
                    index = alphabet.find(plaintext[i].lower())
                    new_index = (index * key2 + key) % len(alphabet)
                    new_letter = alphabet[new_index]
                    ciphertext += new_letter.upper()
                else:
                    index = alphabet.find(plaintext[i])
                    new_index = (index * key2 + key) % len(alphabet)
                    new_letter = alphabet[new_index]
                    ciphertext += new_letter
            else:
                ciphertext += plaintext[i]
        return ciphertext









    

