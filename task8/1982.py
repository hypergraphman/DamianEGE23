from itertools import product

words = product('lodka', repeat=4)
s = set()
for w in words:
    word = ''.join(w)
    if word.count('o') >= 2:
        s.add(word)
print(len(s))