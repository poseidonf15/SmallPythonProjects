import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0
while (i < 3):
    x = random.randint(0,27)
    num = str(random.randint(0,9))
    x2 = random.randint(0,27)
    num2 = str(random.randint(0,9))
    x3 = random.randint(0,27)
    num3 = str(random.randint(0,9))
    x4 = random.randint(0,27)
    num4 = str(random.randint(0,9))

    print(alphabet[x] + num + alphabet[x2] + num2 + alphabet[x3] + num3 + alphabet[x4] + num4)
    i += 1
