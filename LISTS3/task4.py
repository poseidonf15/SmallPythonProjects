words = input().split()

count = 0
for word in words:
    count2 = words.count(word)
    if (count2 > count):
        x = word
print (x)
    
