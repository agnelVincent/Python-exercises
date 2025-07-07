# Count frequency of letters in "scarface" (case-insensitive)

word = "scarface"

freq = {i.lower():word.count(i.lower()) for i in word}

print(freq)