elements = input().split()
num = 0
i = 0
check = 0
element2 = 0

for element in elements:
    if (i > 0):
        if (element.isalpha() and element2.isalpha()):
            check += 1
            print (element + " " + element2)
    element2 = element
    i = 1
if (check <= 0):
    print ("Not enough words!")
