string = input(": ")
count1 = string.count("(")
count1b = string.count(")")
count2 = string.count("]")
count2b = string.count("[")
count3 = string.count("}")
count3b = string.count("{")

if (count1 == count1b and count2 == count2b and count3 == count3b):
    print ("YES")
else:
    print ("NO")
