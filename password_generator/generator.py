import random


def generate_password(lowercase, uppercase, numbers, symbols, num1, num2, num3, num4):
    numbers_list = "0123456789"
    lower_letters = "abczdefghijklmnopqrstuvwyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
    symbols_list = "!@#$%^&*()?<>`~-_"
    password = []

    if (lowercase):
        for i in range(int(num1)):
            password.append(random.choice(lower_letters))

    if (numbers):
        for i in range(int(num2)):
            password.append(random.choice(numbers_list))

    if (uppercase):
        for i in range(int(num3)):
            password.append(random.choice(uppercase_letters))

    if (symbols):
        for i in range(int(num4)):
            password.append(random.choice(symbols_list))

    random.shuffle(password)
    password = ''.join(password)

    return password

##    new_password = []
##    if (lowercase and numbers):
##        x = 8
##    else:
##        x = 4
##    for i in range (x):
##        part = random.choice(password)
##        new_password.append(part)
##        password.remove(part)

##    new_password = "".join([str(item) for item in new_password])
##    return new_password


