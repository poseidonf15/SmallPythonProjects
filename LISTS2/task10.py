words = input().split()
find = input().split()

i = 0
for word in find:
    if (i % 2 == 0):
        x = word
    if (i % 2 == 1):
        x2 = word
    if (i >= 1):
        if (words.find(x) < words.find(x2)):
            check = True
        else:
            check = False
            break
    i += 1
if (check):
    print ("Yes")
else:
    print ("No")
    
