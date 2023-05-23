string = input("Enter a three words separated by spaces. : ")
x = string.find(" ")
print (string.count("a",0,x))
x2 = string.rfind(" ")
check = string.count("a",x,x2)
if (check == -1):
    print ("Error message.")
else:
    num = string.count("a",0,x)
    num2 = string.count("a",x,x2)
    num3 = num + num2
    string2 = string.replace("a","A",num3)
    string2 = string2.replace("A","a",num)
    print (string2)
third_word = string[x2 + 1:]
print (len(third_word))

    
