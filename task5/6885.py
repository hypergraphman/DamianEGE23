a = []
for n in range(1, 190):
    s1 = bin(n)[2:]
    if n % 2 == 0:
        s2 = '1' + s1 + '00'
    else:
        s2 = s1 + bin(s1.count('1'))[2:]
    r = int(s2, 2)
    if r > 190:
        a.append((r, n))
print(min(a))
