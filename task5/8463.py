a = []
for n in range(1000, 100000):
    s1 = bin(n)[2:]
    if n % 5 == 0:
        s2 = s1[:3] + s1
    else:
        t = n % 3 * 5
        s2 = s1 + bin(t)[2:]
    r = int(s2, 2)
    if r > 39000:
        a.append(r)
print(min(a))