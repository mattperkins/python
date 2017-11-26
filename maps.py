from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return " ".join(anagram)

words = ['dormshed']
anagrams = []

# map method 
print(list(map(jumble,words)))

# comprehension method
print([jumble(word)for word in words])

# for loop method
for word in words:
    anagrams.append(jumble(word))
print(anagrams)

