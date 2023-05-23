string = input("Enter here. : ")
alphabet = "abcdefghijklmnopqrstuvwxyz. "
num = len(alphabet)
num2 = 0
num3 = 0

while (num2 < num):
    word = string.count(alphabet[num3])
    print (f"'{alphabet[num3]}': {word}")
    num2 += 1
    num3 += 1
