string = input("Enter here. : ")
num = string.count(",")
num += 1
check = "abcdefghigklmnopqrstuvwxyz"
i = 0
find = -1
find2 = 0

while (i < num):
    if (i == 0):
        letter = string[find + 1]
        find2 = string.find(",",find + 1,)
        word = string[find + 1 : find2]
    if (i > 0):
        find = find2
        find2 = string.find(",",find + 1,)
        letter2 = string[find + 1]
        word2 = string[find:find2]
        x = string.find(letter)
        x2 = string.find(letter2)
        if (x > x2):
            word = word2
    i += 1
word = "," + word + ","
string = string.replace(word,",")
print (word + "," + string)

