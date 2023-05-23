import random

adjectives = ["blue", "dark", "warm", "happy", "good", "fast"]
nouns = ["sister", "friend", "Alex", "Stephanie", "mom", "dog"]
verbs = ["sing", "watch", "play", "sleep", "study", "walk", "eat"]
numbers = [0,1,2,3,4,5,6,7,8,9]
nouns2 = ["songs","apples", "chairs", "books", "homes", "cakes"]

def sentence():
    global adjectives
    global nouns
    global verbs
    global numbers
    global nouns2
    num = 0
    adj = adjectives[random.randint(0,5)]
    n = nouns[random.randint(0,len(nouns) - 1)]
    v = verbs[random.randint(0,len(verbs) - 1)]
    for i in range (1, random.randint(1,3)):
        num = num * 10 + numbers[random.randint(0,9)]
    n2 = nouns2[random.randint(0,len(nouns2) - 1)]
    print (f"my {adj} {n} {v} {num} {n2}")

for l in range (10):
    sentence()
        
