from itertools import permutations

words = permutations('abikolun', r=8)
s = set()
for w in words:
    word = ''.join(w)
    k = word.replace('i', 'a').replace('o', 'a').replace('u', 'a')
    k = k.replace('k', 'b').replace('l', 'b').replace('n', 'b')
    if 'aa' not in k and 'bb' not in k:
        s.add(word)
print(len(s))