from itertools import product

words = product('pula', repeat=6)
s = set()
for w in words:
    word = ''.join(w)
    if word.count('u') == 2:
        s.add(word)
print(len(s))