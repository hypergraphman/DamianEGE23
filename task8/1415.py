from itertools import product

words = product('ab1234567890', repeat=10)
s = set()
for w in words:
    word = ''.join(w)
    if word.count('a') + word.count('b') == 2:
        s.add(word)
    # k = word.replace('b', 'a')
    # if k.count('a') == 2:
    #     s.add(word)
print(len(s))