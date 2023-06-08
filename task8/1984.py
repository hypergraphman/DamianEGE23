from itertools import permutations

words = permutations('igrok', r=5)
s = set()
for w in words:
    word = ''.join(w)
    if word[0] != 'k' and 'rok' not in word:
        s.add(word)
print(len(s))