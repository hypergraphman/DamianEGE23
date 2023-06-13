from fnmatch import fnmatch


def f(n):
    r = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)


for i in range(65000, 706000):
    if fnmatch(str(i), '6*97*5?'):
        c = 0
        s = 0
        for el in f(i):
            if el % 2 == 0:
                c += 1
                s += el
        if c >= 4:
            print(i, s)