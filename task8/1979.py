from itertools import product

words = product('kreslo', repeat=4)
s = set()
for w in words:
    word = ''.join(w)
    if word[0] in 'krsl' and word[-1] in 'eo':
        s.add(word)
print(len(s))