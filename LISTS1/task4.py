capitals = input().split(" ")
print (capitals)
capitals.append(input("Enter a capitale what are not in the list yet. : "))
print (capitals)
for capital in capitals:
    if (len(capital) < 5):
        capitals.remove(capital)
print (capitals)
        
