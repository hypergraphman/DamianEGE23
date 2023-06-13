x = 64 ** 30 + 2 ** 300 - 4
p = 16
r = ''
while x > 0:
    r = '0123456789ABCDEF'[x % p] + r
    x //= p
print(r)
print(r.count('F'))