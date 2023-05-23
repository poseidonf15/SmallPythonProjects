string = input("Enter here. : ")
num = string.count(" ")
num += 1
find = 0
find2 = string.find(" ")
i = 0

while (i < num):
    if (i > 0 and i < num -1):
        find = find2 + 1
        find2 = string.find(" ",find + 1,)
    if (i == num - 1):
        find = find2
        print (f"word number {i + 1} long = {len(string[find + 1:])}")
    if (i < num -1 ):
        print (f"word number {i + 1} long = {len(string[find:find2])}")
    i += 1
    
    
